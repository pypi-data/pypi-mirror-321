import pandas as pd
import numpy as np
import tifffile
from scipy import ndimage
from skimage import measure
import cv2
import concurrent.futures
from scipy.ndimage import zoom
import multiprocessing as mp
import os
import copy
import statistics as stats
import plotly.graph_objects as go
import networkx as nx
from scipy.signal import find_peaks
try:
    import cupy as cp
except:
    pass
from . import node_draw
from . import network_draw
from skimage.morphology import skeletonize_3d
#from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from concurrent.futures import ThreadPoolExecutor, as_completed
from . import smart_dilate
from . import modularity
from . import simple_network
from . import hub_getter
from . import community_extractor
from . import network_analysis
from . import morphology
from . import proximity


#These next several methods relate to searching with 3D objects by dilating each one in a subarray around their neighborhood although I don't explicitly use this anywhere... can call them deprecated although I may want to use them later again so I have them still written out here.


def get_reslice_indices(args):
    """Internal method used for the secondary algorithm that finds dimensions for subarrays around nodes"""

    indices, dilate_xy, dilate_z, array_shape = args
    try:
        max_indices = np.amax(indices, axis = 0) #Get the max/min of each index.
    except ValueError: #Return Nones if this error is encountered
        return None, None, None
    min_indices = np.amin(indices, axis = 0)

    z_max, y_max, x_max = max_indices[0], max_indices[1], max_indices[2]

    z_min, y_min, x_min = min_indices[0], min_indices[1], min_indices[2]

    y_max = y_max + ((dilate_xy-1)/2) + 1 #Establish dimensions of intended subarray, expanding the max/min indices to include
    y_min = y_min - ((dilate_xy-1)/2) - 1 #the future dilation space (by adding/subtracting half the dilation kernel for each axis)
    x_max = x_max + ((dilate_xy-1)/2) + 1 #an additional index is added in each direction to make sure nothing is discluded.
    x_min = x_min - ((dilate_xy-1)/2) - 1
    z_max = z_max + ((dilate_z-1)/2) + 1
    z_min = z_min - ((dilate_z-1)/2) - 1

    if y_max > (array_shape[1] - 1): #Some if statements to make sure the subarray will not cause an indexerror
        y_max = (array_shape[1] - 1)
    if x_max > (array_shape[2] - 1):
        x_max = (array_shape[2] - 1)
    if z_max > (array_shape[0] - 1):
        z_max = (array_shape[0] - 1)
    if y_min < 0:
        y_min = 0
    if x_min < 0:
        x_min = 0
    if z_min < 0:
        z_min = 0

    y_vals = [y_min, y_max] #Return the subarray dimensions as lists
    x_vals = [x_min, x_max]
    z_vals = [z_min, z_max]

    return z_vals, y_vals, x_vals

def reslice_3d_array(args):
    """Internal method used for the secondary algorithm to reslice subarrays around nodes."""

    input_array, z_range, y_range, x_range = args
    z_start, z_end = z_range
    z_start, z_end = int(z_start), int(z_end)
    y_start, y_end = y_range
    y_start, y_end = int(y_start), int(y_end)
    x_start, x_end = x_range
    x_start, x_end = int(x_start), int(x_end)
    
    # Reslice the array
    resliced_array = input_array[z_start:z_end+1, y_start:y_end+1, x_start:x_end+1]
    
    return resliced_array



def _get_node_edge_dict(label_array, edge_array, label, dilate_xy, dilate_z):
    """Internal method used for the secondary algorithm to find which nodes interact with which edges."""
    
    # Create a boolean mask where elements with the specified label are True
    label_array = label_array == label
    label_array = dilate_3D(label_array, dilate_xy, dilate_xy, dilate_z) #Dilate the label to see where the dilated label overlaps
    edge_array = edge_array * label_array  # Filter the edges by the label in question
    edge_array = edge_array.flatten()  # Convert 3d array to 1d array
    edge_array = remove_zeros(edge_array)  # Remove zeros
    edge_array = set(edge_array)  # Remove duplicates
    edge_array = list(edge_array)  # Back to list

    return edge_array

def process_label(args):
    """Internal method used for the secondary algorithm to process a particular node."""
    nodes, edges, label, dilate_xy, dilate_z, array_shape = args
    print(f"Processing node {label}")
    indices = np.argwhere(nodes == label)
    z_vals, y_vals, x_vals = get_reslice_indices((indices, dilate_xy, dilate_z, array_shape))
    if z_vals is None: #If get_reslice_indices ran into a ValueError, nothing is returned.
        return None, None, None
    sub_nodes = reslice_3d_array((nodes, z_vals, y_vals, x_vals))
    sub_edges = reslice_3d_array((edges, z_vals, y_vals, x_vals))
    return label, sub_nodes, sub_edges


def create_node_dictionary(nodes, edges, num_nodes, dilate_xy, dilate_z):
    """Internal method used for the secondary algorithm to process nodes in parallel."""
    # Initialize the dictionary to be returned
    node_dict = {}

    array_shape = nodes.shape

    # Use ThreadPoolExecutor for parallel execution
    with ThreadPoolExecutor(max_workers=mp.cpu_count()) as executor:
        # First parallel section to process labels
        # List of arguments for each parallel task
        args_list = [(nodes, edges, i, dilate_xy, dilate_z, array_shape) for i in range(1, num_nodes + 1)]

        # Execute parallel tasks to process labels
        results = executor.map(process_label, args_list)

        # Second parallel section to create dictionary entries
        for label, sub_nodes, sub_edges in results:
            executor.submit(create_dict_entry, node_dict, label, sub_nodes, sub_edges, dilate_xy, dilate_z)

    return node_dict

def create_dict_entry(node_dict, label, sub_nodes, sub_edges, dilate_xy, dilate_z):
    """Internal method used for the secondary algorithm to pass around args in parallel."""

    if label is None:
        pass
    else:
        node_dict[label] = _get_node_edge_dict(sub_nodes, sub_edges, label, dilate_xy, dilate_z)

def find_shared_value_pairs(input_dict):
    """Internal method used for the secondary algorithm to look through discrete node-node connections in the various node dictionaries"""

    master_list = []
    compare_dict = input_dict.copy()

    # Iterate through each key in the dictionary
    for key1, values1 in input_dict.items():
        # Iterate through each other key in the dictionary
        for key2, values2 in compare_dict.items():
            # Avoid comparing the same key to itself
            if key1 != key2:
                # Find the intersection of values between the two keys
                shared_values = set(values1) & set(values2)
                # If there are shared values, create pairs and add to master list
                if shared_values:
                    for value in shared_values:
                        master_list.append([key1, key2, value])
        del compare_dict[key1]

    return master_list



#Below are helper methods that are used for the main algorithm (calculate_all)

def array_trim(edge_array, node_array):
    """Internal method used by the primary algorithm to efficiently and massively reduce extraneous search regions for edge-node intersections"""
    edge_list = edge_array.flatten() #Turn arrays into lists
    node_list = node_array.flatten()

    edge_bools = edge_list != 0 #establish where edges/nodes exist by converting to a boolean list
    node_bools = node_list != 0

    overlaps = edge_bools * node_bools #Establish boolean list where edges and nodes intersect.

    edge_overlaps = overlaps * edge_list #Set all vals in the edges/nodes to 0 where intersections are not occurring
    node_overlaps = overlaps * node_list

    edge_overlaps = remove_zeros(edge_overlaps) #Remove all values where intersections are not present, so we don't have to iterate through them later
    node_overlaps = remove_zeros(node_overlaps)

    return edge_overlaps, node_overlaps

def establish_connections_parallel(edge_labels, num_edge, node_labels):
    """Internal method used by the primary algorithm to look at dilated edges array and nodes array. Iterates through edges. 
    Each edge will see what nodes it overlaps. It will put these in a list."""
    print("Processing edge connections...")
    
    all_connections = []

    def process_edge(label):

        if label not in edge_labels:
            return None

        edge_connections = []

        # Get the indices corresponding to the current edge label
        indices = np.argwhere(edge_labels == label).flatten()

        for index in indices:

            edge_connections.append(node_labels[index])

        #the set() wrapper removes duplicates from the same sublist
        my_connections = list(set(edge_connections))


        edge_connections = [my_connections, label]


        #Edges only interacting with one node are not used:
        if len(my_connections) > 1:

            return edge_connections
        else:
            return None

    #These lines makes CPU run for loop iterations simultaneously, speeding up the program:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_edge, range(1, num_edge + 1)))

    all_connections = [result for result in results if result is not None]

    return all_connections


def extract_pairwise_connections(connections):
    """Parallelized method to break lists of edge interactions into trios."""
    def chunk_data_pairs(data, num_chunks):
        """Helper function to divide data into roughly equal chunks."""
        chunk_size = len(data) // num_chunks
        remainder = len(data) % num_chunks
        chunks = []
        start = 0
        for i in range(num_chunks):
            extra = 1 if i < remainder else 0  # Distribute remainder across the first few chunks
            end = start + chunk_size + extra
            chunks.append(data[start:end])
            start = end
        return chunks

    def process_sublist_pairs(connections):
        """Helper function to process each sublist and generate unique pairs."""
        pairwise_connections = []
        for connection in connections:
            nodes = connection[0]  # Get the list of nodes
            edge_ID = connection[1]  # Get the edge ID
            pairs_within_sublist = [(nodes[i], nodes[j], edge_ID) for i in range(len(nodes))
                                  for j in range(i + 1, len(nodes))]
            pairwise_connections.extend(set(map(tuple, pairs_within_sublist)))
        pairwise_connections = [list(pair) for pair in pairwise_connections]
        return pairwise_connections

    pairwise_connections = []
    num_cpus = mp.cpu_count()  # Get the number of CPUs available
    
    # Chunk the data
    connection_chunks = chunk_data_pairs(connections, num_cpus)
    
    # Use ThreadPoolExecutor to parallelize the processing of the chunks
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cpus) as executor:
        # Submit the chunks for processing in parallel
        futures = [executor.submit(process_sublist_pairs, chunk) for chunk in connection_chunks]
        # Retrieve the results as they are completed
        for future in concurrent.futures.as_completed(futures):
            pairwise_connections.extend(future.result())
    
    return pairwise_connections


#Saving outputs

def create_and_save_dataframe(pairwise_connections, excel_filename = None):
    """Internal method used to convert lists of discrete connections into an excel output"""
    # Determine the length of the input list
    length = len(pairwise_connections)
    
    # Initialize counters for column assignment
    col_start = 0
    
    # Initialize master list to store sublists
    master_list = []
    
    # Split the input list into sublists of maximum length 1 million
    while col_start < length:
        # Determine the end index for the current sublist
        col_end = min(col_start + 1000000, length)
        
        # Append the current sublist to the master list
        master_list.append(pairwise_connections[col_start:col_end])
        
        # Update column indices for the next sublist
        col_start = col_end
    
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Assign trios to columns in the DataFrame
    for i, sublist in enumerate(master_list):
        # Determine column names for the current sublist
        column_names = ['Node {}A'.format(i+1), 'Node {}B'.format(i+1), 'Edge {}C'.format(i+1)]
        
        # Create a DataFrame from the current sublist
        temp_df = pd.DataFrame(sublist, columns=column_names)
        
        # Concatenate the DataFrame with the master DataFrame
        df = pd.concat([df, temp_df], axis=1)

    if excel_filename is not None:
        # Remove file extension if present to use as base path
        base_path = excel_filename.rsplit('.', 1)[0]
        
        # First try to save as CSV
        try:
            csv_path = f"{base_path}.csv"
            df.to_csv(csv_path, index=False)
            print(f"Network file saved to {csv_path}")
            return
        except Exception as e:
            print(f"Could not save as CSV: {str(e)}")
            
            # If CSV fails, try to save as Excel
            try:
                xlsx_path = f"{base_path}.xlsx"
                df.to_excel(xlsx_path, index=False)
                print(f"Network file saved to {xlsx_path}")
            except Exception as e:
                print(f"Unable to write network file to disk... please make sure that {base_path}.xlsx is being saved to a valid directory and try again")

    else:
        return df




#General supporting methods below:

def invert_array(array):
    """Internal method used to flip node array indices. 0 becomes 255 and vice versa."""
    inverted_array = np.where(array == 0, 255, 0).astype(np.uint8)
    return inverted_array

def invert_boolean(array):
    """Internal method to flip a boolean array"""
    inverted_array = np.where(array == False, True, False).astype(np.uint8)
    return inverted_array

def establish_edges(nodes, edge):
    """Internal  method used to black out where edges interact with nodes"""
    invert_nodes = invert_array(nodes)
    edges = edge * invert_nodes
    return edges

def establish_inner_edges(nodes, edge):
    """Internal method to find inner edges that may exist betwixt dilated nodes."""
    inner_edges = edge * nodes
    return inner_edges


def upsample_with_padding(data, factor=None, original_shape=None):
    """
    Upsample a 3D or 4D array with optional different scaling factors per dimension.
    
    Parameters:
    -----------
    data : ndarray
        Input 3D array or 4D array (where 4th dimension is RGB) to be upsampled
    factor : float or tuple, optional
        Upsampling factor. If float, same factor is applied to all dimensions.
        If tuple, should contain three values for z, y, x dimensions respectively.
        If None, factor is calculated from original_shape.
    original_shape : tuple, optional
        Target shape for the output array. Used to calculate factors if factor is None.
        
    Returns:
    --------
    ndarray
        Upsampled and padded array matching the original shape
    """
    if original_shape is None:
        raise ValueError("original_shape must be provided")
        
    # Handle 4D color arrays
    is_color = len(data.shape) == 4 and data.shape[-1] == 3
    if is_color:
        # Split into separate color channels
        channels = [data[..., i] for i in range(3)]
        upsampled_channels = []
        
        for channel in channels:
            # Upsample each channel separately
            upsampled_channel = _upsample_3d_array(channel, factor, original_shape)
            upsampled_channels.append(upsampled_channel)
            
        # Stack the channels back together
        return np.stack(upsampled_channels, axis=-1)
    else:
        # Handle regular 3D array
        return _upsample_3d_array(data, factor, original_shape)

def _upsample_3d_array(data, factor, original_shape):
    """Helper function to handle the upsampling of a single 3D array"""
    original_shape = np.array(original_shape)
    current_shape = np.array(data.shape)
    
    # Calculate factors if not provided
    if factor is None:
        # Compute the ratio between original and current shape for each dimension
        factors = [os / cs for os, cs in zip(original_shape, current_shape)]
        # If all factors are the same, use a single number for efficiency
        if len(set(factors)) == 1:
            factor = factors[0]
        else:
            factor = tuple(factors)
    elif isinstance(factor, (int, float)):
        factor = factor  # Keep it as a single number
        
    # Upsample the input array
    binary_array = zoom(data, factor, order=0)
    upsampled_shape = np.array(binary_array.shape)
    
    # Calculate the positive differences in dimensions
    difference_dims = original_shape - upsampled_shape
    
    # Calculate the padding amounts for each dimension
    padding_dims = np.maximum(difference_dims, 0)
    padding_before = padding_dims // 2
    padding_after = padding_dims - padding_before
    
    # Pad the binary array along each dimension
    padded_array = np.pad(binary_array, 
                         [(padding_before[0], padding_after[0]),
                          (padding_before[1], padding_after[1]),
                          (padding_before[2], padding_after[2])],
                         mode='constant',
                         constant_values=0)
    
    # Calculate the subtraction amounts for each dimension
    sub_dims = np.maximum(-difference_dims, 0)
    sub_before = sub_dims // 2
    sub_after = sub_dims - sub_before
    
    # Remove excess dimensions sequentially
    # Remove planes from the beginning and end
    if sub_dims[0] == 0:
        trimmed_planes = padded_array
    else:
        trimmed_planes = padded_array[sub_before[0]:-sub_after[0], :, :]
    
    # Remove rows from the beginning and end
    if sub_dims[1] == 0:
        trimmed_rows = trimmed_planes
    else:
        trimmed_rows = trimmed_planes[:, sub_before[1]:-sub_after[1], :]
    
    # Remove columns from the beginning and end
    if sub_dims[2] == 0:
        trimmed_array = trimmed_rows
    else:
        trimmed_array = trimmed_rows[:, :, sub_before[2]:-sub_after[2]]
    
    return trimmed_array

def remove_branches(skeleton, length):
    """Used to compensate for overly-branched skeletons resulting from the scipy 3d skeletonization algorithm"""

    def find_coordinate_difference(arr):
        try:
            arr[1,1,1] = 0
            # Find the indices of non-zero elements
            indices = np.array(np.nonzero(arr)).T
            
            # Calculate the difference
            diff = np.array([1,1,1]) - indices[0]
            
            return diff
        except:
            return


    skeleton = np.pad(skeleton, pad_width=1, mode='constant', constant_values=0) #Add black planes over the 3d space to avoid index errors

    # Find all nonzero voxel coordinates
    nonzero_coords = np.transpose(np.nonzero(skeleton))
    x, y, z = nonzero_coords[0]
    threshold = 2 * skeleton[x, y, z]
    nubs = []

    for b in range(length):

        new_coords = []

        # Create a copy of the image to modify
        image_copy = np.copy(skeleton)


        # Iterate through each nonzero voxel
        for x, y, z in nonzero_coords: #We are looking for endpoints, which designate a branch terminus, that will be removed and move onto the next endpoint equal for iterations equal to user length param

            # Count nearby pixels including diagonals
            mini = skeleton[x-1:x+2, y-1:y+2, z-1:z+2]
            nearby_sum = np.sum(mini)
            
            # If sum is one, remove this endpoint
            if nearby_sum <= threshold:

                try:

                    dif = find_coordinate_difference(mini)
                    new_coord = [x - dif[0], y - dif[1], z - dif[2]]
                    new_coords.append(new_coord)
                except:
                    pass
                    
                nonzero_coords = new_coords

                image_copy[x, y, z] = 0
            elif b > 0:
                nub = [x, y, z]
                nubs.append(nub)

        if b == length - 1:
            for item in nubs: #The nubs are endpoints of length = 1. They appear a bit different in the array so we just note when one is created and remove them all at the end in a batch.
                #x, y, z = item[0], item[1], item[2]
                image_copy[item[0], item[1], item[2]] = 0
                #image_copy[x-1:x+2, y-1:y+2, z-1:z+2] = 0



        skeleton = image_copy

    image_copy = (image_copy[1:-1, 1:-1, 1:-1]).astype(np.uint8)

    return image_copy


def break_and_label_skeleton(skeleton, peaks = 1, branch_removal = 0, comp_dil = 0, max_vol = 0, directory = None, return_skele = False, nodes = None):
    """Internal method to break open a skeleton at its branchpoints and label the remaining components, for an 8bit binary array"""

    if type(skeleton) == str:
        broken_skele = skeleton
        skeleton = tifffile.imread(skeleton)
    else:
        broken_skele = None

    if nodes is None:

        verts = label_vertices(skeleton, peaks = peaks, branch_removal = branch_removal, comp_dil = comp_dil, max_vol = max_vol, return_skele = return_skele)

    else:
        verts = nodes

    verts = invert_array(verts)

    image_copy = skeleton * verts

 
    # Label the modified image to assign new labels for each branch
    #labeled_image, num_labels = measure.label(image_copy, connectivity=2, return_num=True)
    labeled_image, num_labels = label_objects(image_copy)

    if type(broken_skele) == str:
        if directory is None:
            filename = f'broken_skeleton_with_labels.tif'
        else:
            filename = f'{directory}/broken_skeleton_with_labels.tif'

        tifffile.imwrite(filename, labeled_image, photometric='minisblack')
        print(f"Broken skeleton saved to {filename}")

    return labeled_image



def threshold(arr, proportion, custom_rad = None):

    """Internal method to apply a proportional threshold on an image"""

    def find_closest_index(target: float, num_list: list[float]) -> int:
       return min(range(len(num_list)), key=lambda i: abs(num_list[i] - target))

    # Step 1: Flatten the array
    flattened = arr.flatten()

    # Step 2: Filter out the zero values
    non_zero_values = list(set(flattened[flattened > 0]))

    # Step 3: Sort the remaining values
    sorted_values = np.sort(non_zero_values)

    # Step 4: Determine the threshold for the top proportion%

    if custom_rad is None:

        threshold_index = int(len(sorted_values) * proportion)
        threshold_value = sorted_values[threshold_index]

    else:

        targ = int(find_closest_index(custom_rad, sorted_values) - (0.02 * len(sorted_values)))

        threshold_value = sorted_values[targ]
        print(f"Suggested proportion for rad {custom_rad} -> {targ/len(sorted_values)}")

    mask = arr > threshold_value

    arr = arr * mask

    return arr

def z_project(array3d, method='max'):
    """
    Project a 3D numpy array along the Z axis to create a 2D array.
    
    Parameters:
        array3d (numpy.ndarray): 3D input array with shape (Z, Y, X)
        method (str): Projection method - 'max', 'mean', 'min', 'sum', or 'std'
    
    Returns:
        numpy.ndarray: 2D projected array with shape (Y, X)
    """
    if not isinstance(array3d, np.ndarray) or array3d.ndim != 3:
        raise ValueError("Input must be a 3D numpy array")
        
    if method == 'max':
        return np.max(array3d, axis=0)
    elif method == 'mean':
        return np.mean(array3d, axis=0)
    elif method == 'min':
        return np.min(array3d, axis=0)
    elif method == 'sum':
        return np.sum(array3d, axis=0)
    elif method == 'std':
        return np.std(array3d, axis=0)
    else:
        raise ValueError("Method must be one of: 'max', 'mean', 'min', 'sum', 'std'")

def fill_holes_3d(array):

    def process_slice(slice_2d, border_threshold=0.08):
        """
        Process a 2D slice, considering components that touch less than border_threshold
        of any border length as potential holes.
        
        Args:
            slice_2d: 2D binary array
            border_threshold: proportion of border that must be touched to be considered background
        """
        slice_2d = slice_2d.astype(np.uint8)
        labels, num_features = ndimage.label(slice_2d)
        
        if num_features == 0:
            return np.zeros_like(slice_2d)
        
        # Get dimensions for threshold calculations
        height, width = slice_2d.shape
        
        # Dictionary to store border intersection lengths for each label
        border_proportions = {}
        
        for label in range(1, num_features + 1):
            mask = labels == label
            
            # Calculate proportion of each border this component touches
            top_prop = np.sum(mask[0, :]) / width
            bottom_prop = np.sum(mask[-1, :]) / width
            left_prop = np.sum(mask[:, 0]) / height
            right_prop = np.sum(mask[:, -1]) / height
            
            # If it touches any border significantly, consider it background
            border_proportions[label] = max(top_prop, bottom_prop, left_prop, right_prop)
        
        # Create mask of components that either don't touch borders
        # or touch less than the threshold proportion
        background_labels = {label for label, prop in border_proportions.items() 
                            if prop > border_threshold}
        
        holes_mask = ~np.isin(labels, list(background_labels))
        
        return holes_mask

    array = binarize(array)
    inv_array = invert_array(array)

    
    # Create arrays for all three planes
    array_xy = np.zeros_like(inv_array, dtype=np.uint8)
    array_xz = np.zeros_like(inv_array, dtype=np.uint8)
    array_yz = np.zeros_like(inv_array, dtype=np.uint8)


    # Process XY plane
    for z in range(inv_array.shape[0]):
        array_xy[z] = process_slice(inv_array[z])

    if array.shape[0] > 3: #only use these dimensions for sufficiently large zstacks
        
        # Process XZ plane    
        for y in range(inv_array.shape[1]):
            slice_xz = inv_array[:, y, :]
            array_xz[:, y, :] = process_slice(slice_xz)
            
        # Process YZ plane
        for x in range(inv_array.shape[2]):
            slice_yz = inv_array[:, :, x]
            array_yz[:, :, x] = process_slice(slice_yz)
        
        # Combine results from all three planes
        filled = (array_xy | array_xz | array_yz) * 255
        return array + filled
    else:
        return array_xy * 255





def resize(array, factor, order = 0):
    """Simply resizes an array by a factor"""

    array = zoom(array, (factor), order = order)

    return array



def _rescale(array, original_shape, xy_scale, z_scale):
    """Internal method to help 3D visualization"""
    if xy_scale != 1 or z_scale != 1: #Handle seperate voxel scalings by resizing array dimensions
        if z_scale > xy_scale:
            array = zoom(array, (xy_scale/z_scale, 1, 1), order = 3)
        elif xy_scale > z_scale:
            array = zoom(array, (1, z_scale/xy_scale, z_scale/xy_scale))
    return array

def visualize_3D(array, other_arrays=None, xy_scale = 1, z_scale = 1):
    """
    Mostly internal method for 3D visualization, although can be run directly on tif files to view them. Uses plotly to visualize
    a 3D, binarized isosurface of data. Note this method likely requires downsampling on objects before running.
    :param array: (Mandatory; string or ndarray) - Either a path to a .tif file to visualize in 3D binary, or a ndarray of the same.
    :param other_arrays: (Optional - Val = None; string, ndarray, or list) - Either a path to a an additional .tif file to visualize in 3D binary or an ndarray containing the same,
    or otherwise a path to a directory containing ONLY other .tif files to visualize, or a list of ndarrays containing the same.
    :param xy_scale: (Optional - Val = 1; float) - The xy pixel scaling of an image to visualize.
    :param z_scale: (Optional - Val = 1; float) - The z voxel depth of an image to visualize.
    """

    if isinstance(array, str):
        array = tifffile.imread(array)

    original_shape = array.shape[1]

    array = _rescale(array, original_shape, xy_scale, z_scale)
    array = binarize(array)

    # Create a meshgrid for coordinates
    x, y, z = np.indices(array.shape)

    # Create a figure
    fig = go.Figure()

    # Plot the main array
    _plot_3D(fig, x, y, z, array, 'red')

    if other_arrays is not None and ((type(other_arrays) == str) or (type(other_arrays) == list)):
        try: #Presume single tif
            array = tifffile.imread(other_arrays)
            if array.shape[1] != original_shape:
                array = downsample(array, array.shape[1]/original_shape)
            array = _rescale(array, original_shape, xy_scale, z_scale)
            array = binarize(array)
            _plot_3D(fig, x, y, z, array, 'green')
        except: #presume directory or list
            basic_colors = ['blue', 'yellow', 'cyan', 'magenta', 'black', 'white', 'gray', 'orange', 'brown', 'pink', 'purple', 'lime', 'teal', 'navy', 'maroon', 'olive', 'silver', 'red', 'green']
            try: #presume directory
                arrays = directory_info(other_arrays)
                directory = other_arrays
            except: #presume list
                arrays = other_arrays
            for i, array_path in enumerate(arrays): 
                try: #presume tif
                    array = tifffile.imread(f"{directory}/{array_path}")
                    if array.shape[1] != original_shape:
                        array = downsample(array, array.shape[1]/original_shape)
                    array = _rescale(array, original_shape, xy_scale, z_scale)
                    array = binarize(array)
                except: #presume array
                    array = array_path
                    del array_path
                    if array is not None:
                        if array.shape[1] != original_shape:
                            array = downsample(array, array.shape[1]/original_shape)
                        array = _rescale(array, original_shape, xy_scale, z_scale)
                        array = binarize(array)
                color = basic_colors[i % len(basic_colors)]  # Ensure color index wraps around if more arrays than colors
                if array is not None:
                    _plot_3D(fig, x, y, z, array, color)
    else:
        try:
            other_arrays = _rescale(other_arrays, original_shape, xy_scale, z_scale)
            other_arrays = binarize(other_arrays)
            _plot_3D(fig, x, y, z, other_arrays, 'green')
        except:
            pass

    # Set the layout for better visualization
    fig.update_layout(scene=dict(
        xaxis_title='Z Axis',
        yaxis_title='Y Axis',
        zaxis_title='X Axis'
    ))

    fig.show()

def _plot_3D(fig, x, y, z, array, color):
    """Internal method used for 3D visualization"""
    # Define the isosurface level
    level = 0.5  

    # Add the isosurface to the figure
    fig.add_trace(go.Isosurface(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        value=array.flatten(),
        isomin=level,
        isomax=level,
        opacity=0.6,  # Adjust opacity
        surface_count=1,  # Show only the isosurface
        colorscale=[[0, color], [1, color]],  # Set uniform color
        showscale=False  # Hide color scale bar
    ))


def remove_trunk(edges):
    """
    Internal method used to remove the edge trunk. Essentially removes the largest object from
    a binary array.
    """
     # Label connected components in the binary array
    labeled_array = measure.label(edges)

    # Get unique labels and their counts
    unique_labels, label_counts = np.unique(labeled_array, return_counts=True)

    # Find the label corresponding to the largest object
    largest_label = unique_labels[np.argmax(label_counts[1:]) + 1]

    # Set indices of the largest object to 0
    edges[labeled_array == largest_label] = 0

    return edges

def hash_inners(search_region, inner_edges, GPU = True):
    """Internal method used to help sort out inner edge connections. The inner edges of the array will not differentiate between what nodes they contact if those nodes themselves directly touch each other.
    This method allows these elements to be efficiently seperated from each other"""

    print("Performing gaussian blur to hash inner edges.")

    blurred_search = smart_dilate.gaussian(search_region, GPU = GPU) 

    borders = binarize((blurred_search - search_region)) #By subtracting the original image from the guassian blurred version, we set all non-border regions to 0

    del blurred_search

    inner_edges = inner_edges * borders #And as a result, we can mask out only 'inner edges' that themselves exist within borders

    inner_edges = dilate_3D_old(inner_edges, 3, 3, 3) #Not sure if dilating is necessary. Want to ensure that the inner edge pieces still overlap with the proper nodes after the masking.

    return inner_edges

def dilate_3D(tiff_array, dilated_x, dilated_y, dilated_z):
    """Internal method to dilate an array in 3D. Dilation this way is much faster than using a distance transform although the latter is theoretically more accurate.
    Arguments are an array,  and the desired pixel dilation amounts in X, Y, Z."""

    def create_circular_kernel(diameter):
        """Create a 2D circular kernel with a given radius.

        Parameters:
        radius (int or float): The radius of the circle.

        Returns:
        numpy.ndarray: A 2D numpy array representing the circular kernel.
        """
        # Determine the size of the kernel
        radius = diameter/2
        size = radius  # Diameter of the circle
        size = int(np.ceil(size))  # Ensure size is an integer
        
        # Create a grid of (x, y) coordinates
        y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
        
        # Calculate the distance from the center (0,0)
        distance = np.sqrt(x**2 + y**2)
        
        # Create the circular kernel: points within the radius are 1, others are 0
        kernel = distance <= radius
        
        # Convert the boolean array to integer (0 and 1)
        return kernel.astype(np.uint8)

    def create_ellipsoidal_kernel(long_axis, short_axis):
        """Create a 2D ellipsoidal kernel with specified axis lengths and orientation.

        Parameters:
        long_axis (int or float): The length of the long axis.
        short_axis (int or float): The length of the short axis.

        Returns:
        numpy.ndarray: A 2D numpy array representing the ellipsoidal kernel.
        """
        semi_major, semi_minor = long_axis / 2, short_axis / 2

        # Determine the size of the kernel

        size_y = int(np.ceil(semi_minor))
        size_x = int(np.ceil(semi_major))
        
        # Create a grid of (x, y) coordinates centered at (0,0)
        y, x = np.ogrid[-semi_minor:semi_minor+1, -semi_major:semi_major+1]
        
        # Ellipsoid equation: (x/a)^2 + (y/b)^2 <= 1
        ellipse = (x**2 / semi_major**2) + (y**2 / semi_minor**2) <= 1
        
        return ellipse.astype(np.uint8)


    # Function to process each slice
    def process_slice(z):
        tiff_slice = tiff_array[z].astype(np.uint8)
        dilated_slice = cv2.dilate(tiff_slice, kernel, iterations=1)
        return z, dilated_slice

    def process_slice_other(y):
        tiff_slice = tiff_array[:, y, :].astype(np.uint8)
        dilated_slice = cv2.dilate(tiff_slice, kernel, iterations=1)
        return y, dilated_slice

    # Create empty arrays to store the dilated results for the XY and XZ planes
    dilated_xy = np.zeros_like(tiff_array, dtype=np.uint8)
    dilated_xz = np.zeros_like(tiff_array, dtype=np.uint8)

    kernel_x = int(dilated_x)
    kernel = create_circular_kernel(kernel_x)

    num_cores = mp.cpu_count()

    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = {executor.submit(process_slice, z): z for z in range(tiff_array.shape[0])}

        for future in as_completed(futures):
            z, dilated_slice = future.result()
            dilated_xy[z] = dilated_slice

    kernel_x = int(dilated_x)
    kernel_z = int(dilated_z)

    kernel = create_ellipsoidal_kernel(kernel_x, kernel_z)

    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = {executor.submit(process_slice_other, y): y for y in range(tiff_array.shape[1])}
        
        for future in as_completed(futures):
            y, dilated_slice = future.result()
            dilated_xz[:, y, :] = dilated_slice


    # Overlay the results
    final_result = dilated_xy | dilated_xz

    return final_result

def dilate_3D_recursive(tiff_array, dilated_x, dilated_y, dilated_z, step_size=None):
    """Recursive 3D dilation method that handles odd-numbered dilations properly.
    
    Args:
        tiff_array: Input 3D array
        dilated_x, dilated_y, dilated_z: Odd numbers representing total dilation size
        step_size: Size of dilation step for this iteration
    
    Each dilation parameter represents (n-1)/2 steps outward from the object.
    """
    # Calculate the smallest dimension of the array
    min_dim = min(tiff_array.shape)
    
    # For small dilations relative to array size, don't use recursion
    max_dilation = max(dilated_x, dilated_y, dilated_z)
    if max_dilation < (0.2 * min_dim):
        return dilate_3D_recursive(tiff_array, dilated_x, dilated_y, dilated_z, step_size=1)
    
    # Initialize step_size for first call
    if step_size is None:
        # Start with a reasonable step size based on the largest dilation
        step_size = min(5, max((max_dilation - 1) // 2 // 3, 1))
    
    # Base case: if step_size is 1 or we've achieved full dilation
    if step_size == 1 or (dilated_x <= 1 and dilated_y <= 1 and dilated_z <= 1):
        def create_circular_kernel(diameter):
            radius = diameter/2
            size = radius
            size = int(np.ceil(size))
            y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
            distance = np.sqrt(x**2 + y**2)
            kernel = distance <= radius
            return kernel.astype(np.uint8)

        def create_ellipsoidal_kernel(long_axis, short_axis):
            semi_major, semi_minor = long_axis / 2, short_axis / 2
            size_y = int(np.ceil(semi_minor))
            size_x = int(np.ceil(semi_major))
            y, x = np.ogrid[-semi_minor:semi_minor+1, -semi_major:semi_major+1]
            ellipse = (x**2 / semi_major**2) + (y**2 / semi_minor**2) <= 1
            return ellipse.astype(np.uint8)

        def process_slice(z):
            tiff_slice = tiff_array[z].astype(np.uint8)
            dilated_slice = cv2.dilate(tiff_slice, kernel, iterations=1)
            return z, dilated_slice

        def process_slice_other(y):
            tiff_slice = tiff_array[:, y, :].astype(np.uint8)
            dilated_slice = cv2.dilate(tiff_slice, kernel, iterations=1)
            return y, dilated_slice

        # Create empty arrays for the dilated results
        dilated_xy = np.zeros_like(tiff_array, dtype=np.uint8)
        dilated_xz = np.zeros_like(tiff_array, dtype=np.uint8)

        # Create kernels for final dilation
        kernel = create_circular_kernel(dilated_x)
        
        # Process XY plane
        num_cores = mp.cpu_count()
        with ThreadPoolExecutor(max_workers=num_cores) as executor:
            futures = {executor.submit(process_slice, z): z for z in range(tiff_array.shape[0])}
            for future in as_completed(futures):
                z, dilated_slice = future.result()
                dilated_xy[z] = dilated_slice

        # Process XZ plane
        kernel = create_ellipsoidal_kernel(dilated_x, dilated_z)
        with ThreadPoolExecutor(max_workers=num_cores) as executor:
            futures = {executor.submit(process_slice_other, y): y for y in range(tiff_array.shape[1])}
            for future in as_completed(futures):
                y, dilated_slice = future.result()
                dilated_xz[:, y, :] = dilated_slice

        return dilated_xy | dilated_xz

    # Calculate current iteration's dilation sizes (must be odd numbers)
    current_x_steps = min((dilated_x - 1) // 2, step_size)
    current_y_steps = min((dilated_y - 1) // 2, step_size)
    current_z_steps = min((dilated_z - 1) // 2, step_size)
    
    current_x_dilation = current_x_steps * 2 + 1
    current_y_dilation = current_y_steps * 2 + 1
    current_z_dilation = current_z_steps * 2 + 1
    
    # Perform current iteration's dilation
    current_result = dilate_3D_recursive(tiff_array, current_x_dilation, current_y_dilation, current_z_dilation, step_size=1)
    
    # Calculate remaining dilation needed
    # For X and Y, use the circle radius (current_x_steps)
    # For Z, use the ellipse short axis (current_z_steps)
    remaining_x = max(1, dilated_x - (current_x_steps * 2))
    remaining_y = max(1, dilated_y - (current_y_steps * 2))
    remaining_z = max(1, dilated_z - (current_z_steps * 2))
    
    # If no more dilation needed, return current result
    if remaining_x == 1 and remaining_y == 1 and remaining_z == 1:
        return current_result
    
    # Recursive call with remaining dilation and decreased step size
    return dilate_3D_recursive(current_result, remaining_x, remaining_y, remaining_z, step_size=max(1, step_size - 1))

def erode_3D(tiff_array, eroded_x, eroded_y, eroded_z):
    """Internal method to erode an array in 3D. Erosion this way is much faster than using a distance transform although the latter is theoretically more accurate.
    Arguments are an array, and the desired pixel erosion amounts in X, Y, Z."""
    def create_circular_kernel(diameter):
        """Create a 2D circular kernel with a given radius.
        Parameters:
        radius (int or float): The radius of the circle.
        Returns:
        numpy.ndarray: A 2D numpy array representing the circular kernel.
        """
        # Determine the size of the kernel
        radius = diameter/2
        size = radius  # Diameter of the circle
        size = int(np.ceil(size))  # Ensure size is an integer
        
        # Create a grid of (x, y) coordinates
        y, x = np.ogrid[-radius:radius+1, -radius:radius+1]
        
        # Calculate the distance from the center (0,0)
        distance = np.sqrt(x**2 + y**2)
        
        # Create the circular kernel: points within the radius are 1, others are 0
        kernel = distance <= radius
        
        # Convert the boolean array to integer (0 and 1)
        return kernel.astype(np.uint8)

    def create_ellipsoidal_kernel(long_axis, short_axis):
        """Create a 2D ellipsoidal kernel with specified axis lengths and orientation.
        Parameters:
        long_axis (int or float): The length of the long axis.
        short_axis (int or float): The length of the short axis.
        Returns:
        numpy.ndarray: A 2D numpy array representing the ellipsoidal kernel.
        """
        semi_major, semi_minor = long_axis / 2, short_axis / 2
        # Determine the size of the kernel
        size_y = int(np.ceil(semi_minor))
        size_x = int(np.ceil(semi_major))
        
        # Create a grid of (x, y) coordinates centered at (0,0)
        y, x = np.ogrid[-semi_minor:semi_minor+1, -semi_major:semi_major+1]
        
        # Ellipsoid equation: (x/a)^2 + (y/b)^2 <= 1
        ellipse = (x**2 / semi_major**2) + (y**2 / semi_minor**2) <= 1
        
        return ellipse.astype(np.uint8)

    z_depth = tiff_array.shape[0]

    # Function to process each slice
    def process_slice(z):
        tiff_slice = tiff_array[z].astype(np.uint8)
        eroded_slice = cv2.erode(tiff_slice, kernel, iterations=1)
        return z, eroded_slice

    def process_slice_other(y):
        tiff_slice = tiff_array[:, y, :].astype(np.uint8)
        eroded_slice = cv2.erode(tiff_slice, kernel, iterations=1)
        return y, eroded_slice

    # Create empty arrays to store the eroded results for the XY and XZ planes
    eroded_xy = np.zeros_like(tiff_array, dtype=np.uint8)
    eroded_xz = np.zeros_like(tiff_array, dtype=np.uint8)

    kernel_x = int(eroded_x)
    kernel = create_circular_kernel(kernel_x)

    num_cores = mp.cpu_count()
    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = {executor.submit(process_slice, z): z for z in range(tiff_array.shape[0])}
        for future in as_completed(futures):
            z, eroded_slice = future.result()
            eroded_xy[z] = eroded_slice

    kernel_x = int(eroded_x)
    kernel_z = int(eroded_z)
    kernel = create_ellipsoidal_kernel(kernel_x, kernel_z)

    if z_depth != 2:

        with ThreadPoolExecutor(max_workers=num_cores) as executor:
            futures = {executor.submit(process_slice_other, y): y for y in range(tiff_array.shape[1])}
            
            for future in as_completed(futures):
                y, eroded_slice = future.result()
                eroded_xz[:, y, :] = eroded_slice

    # Overlay the results using AND operation instead of OR for erosion
    if z_depth != 2:
        final_result = eroded_xy & eroded_xz
    else:
        return eroded_xy
    
    return final_result


def dilate_3D_old(tiff_array, dilated_x, dilated_y, dilated_z):
    """(For cubey dilation only). Internal method to dilate an array in 3D.
    Arguments are an array,  and the desired pixel dilation amounts in X, Y, Z."""

    # Create empty arrays to store the dilated results for the XY and XZ planes
    dilated_xy = np.zeros_like(tiff_array, dtype=np.uint8)
    dilated_xz = np.zeros_like(tiff_array, dtype=np.uint8)

    # Perform 2D dilation in the XY plane
    for z in range(tiff_array.shape[0]):
        kernel_x = int(dilated_x)
        kernel_y = int(dilated_y)
        kernel = np.ones((kernel_y, kernel_x), dtype=np.uint8)

        # Convert the slice to the appropriate data type
        tiff_slice = tiff_array[z].astype(np.uint8)

        dilated_slice = cv2.dilate(tiff_slice, kernel, iterations=1)
        dilated_xy[z] = dilated_slice

    # Perform 2D dilation in the XZ plane
    for y in range(tiff_array.shape[1]):
        kernel_x = int(dilated_x)
        kernel_z = int(dilated_z)
        kernel = np.ones((kernel_z, kernel_x), dtype=np.uint8)

        # Convert the slice to the appropriate data type
        tiff_slice = tiff_array[:, y, :].astype(np.uint8)

        dilated_slice = cv2.dilate(tiff_slice, kernel, iterations=1)
        dilated_xz[:, y, :] = dilated_slice

    # Overlay the results
    final_result = dilated_xy | dilated_xz

    return final_result

def dilation_length_to_pixels(xy_scaling, z_scaling, micronx, micronz):
    """Internal method to find XY and Z dilation parameters based on voxel micron scaling"""
    dilate_xy = 2 * int(round(micronx/xy_scaling))

    # Ensure the dilation param is odd to have a center pixel
    dilate_xy += 1 if dilate_xy % 2 == 0 else 0

    dilate_z = 2 * int(round(micronz/z_scaling))

    # Ensure the dilation param is odd to have a center pixel
    dilate_z += 1 if dilate_z % 2 == 0 else 0

    return dilate_xy, dilate_z

def label_objects(nodes, dtype=int):
    """Internal method to labels objects with cubic 3D labelling scheme"""
    if len(nodes.shape) == 3:
        structure_3d = np.ones((3, 3, 3), dtype=int)

    elif len(nodes.shape) == 2:
        structure_3d = np.ones((3, 3), dtype = int)
    nodes, num_nodes = ndimage.label(nodes, structure = structure_3d)

    # Choose a suitable data type based on the number of labels
    if num_nodes < 256:
        dtype = np.uint8
    elif num_nodes < 65536:
        dtype = np.uint16
    else:
        dtype = np.uint32

    # Convert the labeled array to the chosen data type
    nodes = nodes.astype(dtype)

    return nodes, num_nodes


def remove_zeros(input_list):
    """Internal method to remove zeroes from an array"""
    # Use boolean indexing to filter out zeros
    result_array = input_list[input_list != 0] #note - presumes your list is an np array

    return result_array



def combine_edges(edge_labels_1, edge_labels_2):
    """Internal method to combine the edges and 'inner edges' into a single array while preserving their IDs. Prioritizes 'edge_labels_1' when overlapped"""

    edge_labels_1 = edge_labels_1.astype(np.uint32)
    edge_labels_2 = edge_labels_2.astype(np.uint32)

    max_val = np.max(edge_labels_1) 
    edge_bools_1 = edge_labels_1 == 0 #Get boolean mask where edges do not exist.
    edge_bools_2 = edge_labels_2 > 0 #Get boolean mask where inner edges exist.
    edge_labels_2 = edge_labels_2 + max_val #Add the maximum edge ID to all inner edges so the two can be merged without overriding eachother
    edge_labels_2 = edge_labels_2 * edge_bools_2 #Eliminate any indices that should be 0 from inner edges.
    edge_labels_2 = edge_labels_2 * edge_bools_1 #Eliminate any indices where outer edges overlap inner edges (Outer edges are giving overlap priority)
    edge_labels = edge_labels_1 + edge_labels_2 #Combine the outer edges with the inner edges modified via the above steps

    return edge_labels


def combine_nodes(root_nodes, other_nodes, other_ID, identity_dict, root_ID = None):

    """Internal method to merge two labelled node arrays into one"""

    print("Combining node arrays")

    root_nodes = root_nodes.astype(np.uint32)
    other_nodes = other_nodes.astype(np.uint32)

    max_val = np.max(root_nodes) 
    root_bools = root_nodes == 0 #Get boolean mask where root nodes do not exist.
    other_bools = other_nodes > 0 #Get boolean mask where other nodes exist.
    other_nodes = other_nodes + max_val #Add the maximum root node labels to other nodes so the two can be merged without overriding eachother
    other_nodes = other_nodes * other_bools #Eliminate any indices that should be 0 from other_nodes.
    other_nodes = other_nodes * root_bools #Eliminate any indices where other nodes overlap root nodes (root node are giving overlap priority)

    if root_ID is not None:
        rootIDs = list(np.unique(root_nodes)) #Sets up adding these vals to the identitiy dictionary. Gets skipped if this has already been done.

        if rootIDs[0] == 0: #np unique can include 0 which we don't want.
            del rootIDs[0]

    otherIDs = list(np.unique(other_nodes)) #Sets up adding other vals to the identity dictionary.

    if otherIDs[0] == 0:
        del otherIDs[0]

    if root_ID is not None: #Adds the root vals to the dictionary if it hasn't already

        for item in rootIDs:
            identity_dict[item] = root_ID

    for item in otherIDs: #Always adds the other vals to the dictionary
        try:
            other_ID = os.path.basename(other_ID)
        except:
            pass
        identity_dict[item] = other_ID

    nodes = root_nodes + other_nodes #Combine the outer edges with the inner edges modified via the above steps

    return nodes, identity_dict

def directory_info(directory = None):
    """Internal method to get the files in a directory, optionally the current directory if nothing passed"""
    
    if directory is None:
        items = os.listdir()
    else:
        # Get the list of all items in the directory
        items = os.listdir(directory)
    
    return items



#CLASSLESS FUNCTIONS THAT MAY BE USEFUL TO USERS TO RUN DIRECTLY THAT SUPPORT ANALYSIS IN SOME WAY. NOTE THESE METHODS SOMETIMES ARE USED INTERNALLY AS WELL:

def downsample(data, factor, directory=None, order=0):
    """
    Can be used to downsample an image by some arbitrary factor. Downsampled output will be saved to the active directory if none is specified.
    
    :param data: (Mandatory, string or ndarray) - If string, a path to a tif file to downsample. Note that the ndarray alternative is for internal use mainly and will not save its output.
    :param factor: (Mandatory, int) - A factor by which to downsample the image.
    :param directory: (Optional - Val = None, string) - A filepath to save outputs.
    :param order: (Optional - Val = 0, int) - The order of interpolation for scipy.ndimage.zoom
    :returns: a downsampled ndarray.
    """
    # Load the data if it's a file path
    if isinstance(data, str):
        data2 = data
        data = tifffile.imread(data)
    else:
        data2 = None
    
    # Check if Z dimension is too small relative to downsample factor
    if data.ndim == 3 and data.shape[0] < factor * 4:
        print(f"Warning: Z dimension ({data.shape[0]}) is less than 4x the downsample factor ({factor}). "
              f"Skipping Z-axis downsampling to preserve resolution.")
        zoom_factors = (1, 1/factor, 1/factor)
    else:
        zoom_factors = 1/factor

    # Apply downsampling
    data = zoom(data, zoom_factors, order=order)
    
    # Save if input was a file path
    if isinstance(data2, str):
        if directory is None:
            filename = "downsampled.tif"
        else:
            filename = f"{directory}/downsampled.tif"
        tifffile.imwrite(filename, data)
    
    return data
    
def binarize(arrayimage, directory = None):
    """
    Can be used to binarize an image. Binary output will be saved to the active directory if none is specified.
    :param arrayimage: (Mandatory, string or ndarray) - If string, a path to a tif file to binarize. Output will be 8bit with 0 representing background and 255 representing signal. Note that the ndarray alternative is for internal use mainly and will not save its output, and will also contain vals of 0 and 1.
    :param directory: (Optional - Val = None, string) - A filepath to save outputs.
    :returns: a binary ndarray.
    """
    if type(arrayimage) == str:
        print("Binarizing...")
        image = arrayimage
        arrayimage = tifffile.imread(arrayimage)

    arrayimage = arrayimage != 0

    arrayimage = arrayimage.astype(np.uint8)

    arrayimage = arrayimage * 255

    if type(arrayimage) == str:
        arrayimage = arrayimage * 255
        if directory is None:
            tifffile.imwrite(f"binary.tif", arrayimage)
        else:
            tifffile.imwrite(f"{directory}/binary.tif", arrayimage)


    return arrayimage

def dilate(arrayimage, amount, xy_scale = 1, z_scale = 1, directory = None, fast_dil = False, recursive = False):
    """
    Can be used to dilate a binary image in 3D. Dilated output will be saved to the active directory if none is specified. Note that dilation is done with single-instance kernels and not iterations, and therefore
    objects will lose their shape somewhat and become cube-ish if the 'amount' param is ever significantly larger than the objects in quesiton.
    :param arrayimage: (Mandatory, string or ndarray) - If string, a path to a tif file to dilate. Note that the ndarray alternative is for internal use mainly and will not save its output.
    :param amount: (Mandatory, int) - The amount to dilate the array. Note that if xy_scale and z_scale params are not passed, this will correspond one-to-one with voxels. Otherwise, it will correspond with what voxels represent (ie microns).
    :param xy_scale: (Optional; Val = 1, float) - The scaling of pixels.
    :param z_scale: (Optional - Val = 1; float) - The depth of voxels.
    :param directory: (Optional - Val = None, string) - A filepath to save outputs.
    :param fast_dil: (Optional - Val = False, boolean) - A boolean that when True will utilize faster cube dilation but when false will use slower spheroid dilation.
    :returns: a dilated ndarray.
    """

    if type(arrayimage) == str:
        print("Dilating...")
        image = arrayimage
        arrayimage = tifffile.imread(arrayimage).astype(np.uint8)
    else:
        image = None

    dilate_xy, dilate_z = dilation_length_to_pixels(xy_scale, z_scale, amount, amount)

    if len(np.unique(arrayimage)) > 2: #binarize
        arrayimage = binarize(arrayimage)

    if not fast_dil and not recursive:
        arrayimage = (dilate_3D(arrayimage, dilate_xy, dilate_xy, dilate_z)) * 255
        if np.max(arrayimage) == 1:
            arrayimage = arrayimage * 255
    elif not recursive:
        arrayimage = (dilate_3D_old(arrayimage, dilate_xy, dilate_xy, dilate_z)) * 255
    else:
        arrayimage = (dilate_3D_recursive(arrayimage, dilate_xy, dilate_xy, dilate_z)) * 255



    if type(image) == str:
        if directory is None:
            filename = f'dilated.tif'
        else:
            filename = f'{directory}/dilated.tif'

        tifffile.imwrite(filename, arrayimage)
        print(f"Dilated array saved to {filename}")

    return arrayimage

def erode(arrayimage, amount, xy_scale = 1, z_scale = 1):
    if len(np.unique(arrayimage)) > 2: #binarize
        arrayimage = binarize(arrayimage)
    erode_xy, erode_z = dilation_length_to_pixels(xy_scale, z_scale, amount, amount)

    if len(np.unique(arrayimage)) > 2: #binarize
        arrayimage = binarize(arrayimage)

    arrayimage = (erode_3D(arrayimage, erode_xy, erode_xy, erode_z)) * 255
    if np.max(arrayimage) == 1:
        arrayimage = arrayimage * 255

    return arrayimage





def skeletonize(arrayimage, directory = None):
    """
    Can be used to 3D skeletonize a binary image. Skeletonized output will be saved to the active directory if none is specified. Note this works better on already thin filaments and may make mistakes on larger trunkish objects.
    :param arrayimage: (Mandatory, string or ndarray) - If string, a path to a tif file to skeletonize. Note that the ndarray alternative is for internal use mainly and will not save its output.
    :param directory: (Optional - Val = None, string) - A filepath to save outputs.
    :returns: a skeletonized ndarray.
    """
    print("Skeletonizing...")


    if type(arrayimage) == str:
        image = arrayimage
        arrayimage = tifffile.imread(arrayimage).astype(np.uint8)
    else:
        image = None

    arrayimage = (skeletonize_3d(arrayimage))

    if type(image) == str:
        if directory is None:
            filename = f'skeletonized.tif'
        else:
            filename = f'{directory}/skeletonized.tif'

        tifffile.imwrite(filename, arrayimage)
        print(f"Skeletonized array saved to {filename}")

    return arrayimage

def label_branches(array, peaks = 0, branch_removal = 0, comp_dil = 0, max_vol = 0, down_factor = None, directory = None, nodes = None, bonus_array = None, GPU = True):
    """
    Can be used to label branches a binary image. Labelled output will be saved to the active directory if none is specified. Note this works better on already thin filaments and may over-divide larger trunkish objects.
    :param array: (Mandatory, string or ndarray) - If string, a path to a tif file to label. Note that the ndarray alternative is for internal use mainly and will not save its output.
    :param branch_removal: (Optional, Val = None; int) - An optional into to specify what size of pixels to remove branches. Use this if the skeleton is branchy and you want to remove the branches from the larger filaments.
    :param comp_dil: (Optional, Val = 0; int) - An optional value to merge nearby vertices. This algorithm may be prone to leaving a few, disconnected vertices next to each other that otherwise represent the same branch point but will confound the network a bit. These can be combined into a single object by dilation. Note this dilation will be applied post downsample, so take that into account when assigning a value, as the value will not take resampling into account and will just apply as is on a downsample.
    :param max_vol: (Optional, Val = 0, int) - An optional value of the largest volume of an object to keep in the vertices output. Will only filter if > 0.
    :param down_factor: (Optional, Val = None; int) - An optional factor to downsample internally to speed up computation. Note that this method will try to use the GPU if one is available, which may
    default to some internal downsampling.
    :param directory: (Optional - Val = None; string) - A filepath to save outputs.
    :returns: an ndarray with labelled branches.
    """
    if type(array) == str:
        stringbool = True
        array = tifffile.imread(array)
    else:
        stringbool = False

    if down_factor is not None and nodes is None:
        array = downsample(array, down_factor)
        arrayshape = array.shape
    else:
        arrayshape = bonus_array.shape


    if nodes is None:

        array = array > 0

        other_array = skeletonize(array)

        other_array = break_and_label_skeleton(other_array, peaks = peaks, branch_removal = branch_removal, comp_dil = comp_dil, max_vol = max_vol, nodes = nodes)

    else:
        array = break_and_label_skeleton(array, peaks = peaks, branch_removal = branch_removal, comp_dil = comp_dil, max_vol = max_vol, nodes = nodes)

    if nodes is not None and down_factor is not None:
        array = upsample_with_padding(array, down_factor, arrayshape)


    if nodes is None:

        array = smart_dilate.smart_label(array, other_array, GPU = GPU)

    else:
        if down_factor is not None:
            array = smart_dilate.smart_label(bonus_array, array, GPU = GPU, predownsample = down_factor)
        else:

            array = smart_dilate.smart_label(bonus_array, array, GPU = GPU)



    if down_factor is not None and nodes is None:
        array = upsample_with_padding(array, down_factor, arrayshape)

    if stringbool:
        if directory is not None:
            filename = f'{directory}/labelled_branches.tif'
        else:
            filename = f'labelled_branches.tif'

        tifffile.imwrite(filename, other_array)
        print(f"Labelled branches saved to {filename}")
    else:
        print("Branches labelled")


    return array

def label_vertices(array, peaks = 0, branch_removal = 0, comp_dil = 0, max_vol = 0, down_factor = 0, directory = None, return_skele = False):
    """
    Can be used to label vertices (where multiple branches connect) a binary image. Labelled output will be saved to the active directory if none is specified. Note this works better on already thin filaments and may over-divide larger trunkish objects.
    Note that this can be used in tandem with an edge segmentation to create an image containing 'pseudo-nodes', meaning we can make a network out of just a single edge file.
    :param array: (Mandatory, string or ndarray) - If string, a path to a tif file to label. Note that the ndarray alternative is for internal use mainly and will not save its output.
    :param peaks: (Optional, Val = 0; int) - An optional value on what size of peaks to keep. A peak is peak in the histogram of volumes of objects in the array. The number of peaks that will be kept start on the left (low volume). The point of this is to remove large, erroneous vertices that may result from skeletonizing large objects. 
    :param branch_removal: (Optional, Val = 0; int) - An optional into to specify what size of pixels to remove branches. Use this if the skeleton is branchy and you want to remove the branches from the larger filaments. Large objects tend to produce branches when skeletonized. Enabling this in the right situations will make the output significantly more accurate.
    :param comp_dil: (Optional, Val = 0; int) - An optional value to merge nearby vertices. This algorithm may be prone to leaving a few, disconnected vertices next to each other that otherwise represent the same branch point but will confound the network a bit. These can be combined into a single object by dilation. Note this dilation will be applied post downsample, so take that into account when assigning a value, as the value will not take resampling into account and will just apply as is on a downsample.
    :param max_vol: (Optional, Val = 0, int) - An optional value of the largest volume of an object to keep in the vertices output. Will only filter if > 0.
    :param directory: (Optional - Val = None; string) - A filepath to save outputs.
    :returns: an ndarray with labelled vertices.
    """    
    print("Breaking Skeleton...")

    if type(array) == str:
        broken_skele = array
        array = tifffile.imread(array)
    else:
        broken_skele = None

    if down_factor > 0:
        array_shape = array.shape
        array = downsample(array, down_factor)

    array = array > 0

    array = skeletonize(array)

    if branch_removal > 0:
        array = remove_branches(array, branch_removal)

    array = np.pad(array, pad_width=1, mode='constant', constant_values=0)

    # Find all nonzero voxel coordinates
    nonzero_coords = np.transpose(np.nonzero(array))
    x, y, z = nonzero_coords[0]
    threshold = 3 * array[x, y, z]

    # Create a copy of the image to modify
    image_copy = np.zeros_like(array)

    # Iterate through each nonzero voxel
    for x, y, z in nonzero_coords:

        # Count nearby pixels including diagonals
        mini = array[x-1:x+2, y-1:y+2, z-1:z+2]
        nearby_sum = np.sum(mini)
        
        if nearby_sum > threshold:
            mini = mini.copy()
            mini[1, 1, 1] = 0
            _, test_num = ndimage.label(mini)
            if test_num > 2:
                image_copy[x-1:x+2, y-1:y+2, z-1:z+2] = 1

    image_copy = (image_copy[1:-1, 1:-1, 1:-1]).astype(np.uint8)


    # Label the modified image to assign new labels for each branch
    #labeled_image, num_labels = measure.label(image_copy, connectivity=2, return_num=True)

    if peaks > 0:
        image_copy = filter_size_by_peaks(image_copy, peaks)
        if comp_dil > 0:
            image_copy = dilate(image_copy, comp_dil)

        labeled_image, num_labels = label_objects(image_copy)
    elif max_vol > 0:
        image_copy = filter_size_by_vol(image_copy, max_vol)
        if comp_dil > 0:
            image_copy = dilate(image_copy, comp_dil)

        labeled_image, num_labels = label_objects(image_copy)
    else:

        if comp_dil > 0:
            image_copy = dilate(image_copy, comp_dil)
        labeled_image, num_labels = label_objects(image_copy)

    #if down_factor > 0:
        #labeled_image = upsample_with_padding(labeled_image, down_factor, array_shape)

    if type(broken_skele) == str:
        if directory is None:
            filename = f'labelled_vertices.tif'
        else:
            filename = f'{directory}/labelled_vertices.tif'

        tifffile.imwrite(filename, labeled_image, photometric='minisblack')
        print(f"Broken skeleton saved to {filename}")

    if return_skele:

        return labeled_image, (array[1:-1, 1:-1, 1:-1]).astype(np.uint8)

    else:

        return labeled_image

def filter_size_by_peaks(binary_array, num_peaks_to_keep=1):

    binary_array = binary_array > 0
    # Label connected components
    labeled_array, num_features = ndimage.label(binary_array)
    
    # Calculate the volume of each object
    volumes = np.bincount(labeled_array.ravel())[1:]
    
    # Create a histogram of volumes
    hist, bin_edges = np.histogram(volumes, bins='auto')
    
    # Find peaks in the histogram
    peaks, _ = find_peaks(hist, distance=1)
    
    if len(peaks) < num_peaks_to_keep + 1:
        print(f"Warning: Found only {len(peaks)} peaks. Keeping all objects up to the last peak.")
        num_peaks_to_keep = len(peaks) - 1
    
    if num_peaks_to_keep < 1:
        print("Warning: Invalid number of peaks to keep. Keeping all objects.")
        return binary_array

    print(f"Keeping all peaks up to {num_peaks_to_keep} of {len(peaks)} peaks")
    
    # Find the valley after the last peak we want to keep
    if num_peaks_to_keep == len(peaks):
        # If we're keeping all peaks, set the threshold to the maximum volume
        volume_threshold = volumes.max()
    else:
        valley_start = peaks[num_peaks_to_keep - 1]
        valley_end = peaks[num_peaks_to_keep]
        valley = valley_start + np.argmin(hist[valley_start:valley_end])
        volume_threshold = bin_edges[valley + 1]
    
    # Create a mask for objects larger than the threshold
    mask = np.isin(labeled_array, np.where(volumes > volume_threshold)[0] + 1)
    
    # Set larger objects to 0
    result = binary_array.copy()
    result[mask] = 0
    
    return result

def filter_size_by_vol(binary_array, volume_threshold):

    binary_array = binary_array > 0
    # Label connected components
    labeled_array, num_features = ndimage.label(binary_array)
    
    # Calculate the volume of each object
    volumes = np.bincount(labeled_array.ravel())[1:]
    
    # Create a mask for objects larger than the threshold
    mask = np.isin(labeled_array, np.where(volumes > volume_threshold)[0] + 1)
    
    # Set larger objects to 0
    result = binary_array.copy()
    result[mask] = 0
    
    return result

def watershed(image, directory = None, proportion = 0.1, GPU = True, smallest_rad = None, predownsample = None, predownsample2 = None):
    """
    Can be used to 3D watershed a binary image. Watershedding attempts to use an algorithm to split touching objects into seperate labelled components. Labelled output will be saved to the active directory if none is specified.
    This watershed algo essentially uses the distance transform to decide where peaks are and then after thresholding out the non-peaks, uses the peaks as labelling kernels for a smart label. It runs semi slow without GPU accel since it requires two dts to be computed.
    :param image: (Mandatory, string or ndarray). - If string, a path to a binary .tif to watershed, or an ndarray containing the same.
    :param directory: (Optional - Val = None; string) - A filepath to save outputs.
    :param proportion: (Optional - Val = 0.1; float) - A zero to one value representing the proportion of watershed 'peaks' that are kept around for splitting objects. Essentially,
    making this value smaller makes the watershed break more things, however making it too small will result in some unusual failures where small objects all get the same label. 
    :param GPU: (Optional - Val = True; boolean). If True, GPU will be used to watershed. Please note this will result in internal downsampling most likely, and overall be very fast.
    However, this downsampling may kick small nodes out of the image. Do not use the GPU to watershed if your GPU wants to downsample beyond the size of the smallest node that you
    want to keep in the output. Set to False to use the CPU (no downsampling). Note using the GPU + downsample may take around a minute to process arrays that are a few GB while the CPU may take an hour or so.
    :param smallest_rad: (Optional - Val = None; int). The size (in voxels) of the radius of the smallest object you want to seperate with watershedding. Note that the
    'proportion' param is the affector of watershed outputs but itself may be confusing to tinker with. By inputting a smallest_rad, the algo will instead compute a custom proportion
    to use for your data.
    :returns: A watershedded, labelled ndarray.
    """ 

    if type(image) == str:
        image = tifffile.imread(image)

    image = image > 0

    original_shape = image.shape


    try:

        if GPU == True and cp.cuda.runtime.getDeviceCount() > 0:
            print("GPU detected. Using CuPy for distance transform.")

            try:

                if predownsample is None:
                    # Step 4: Find the nearest label for each voxel in the ring
                    distance = smart_dilate.compute_distance_transform_distance_GPU(image)
                else:
                    gotoexcept = 1/0

            except (cp.cuda.memory.OutOfMemoryError, ZeroDivisionError) as e:
                if predownsample is None:
                    down_factor = smart_dilate.catch_memory(e) #Obtain downsample amount based on memory missing
                else:
                    down_factor = (predownsample)**3

                while True:
                    downsample_needed = down_factor**(1./3.)
                    small_image = downsample(image, downsample_needed) #Apply downsample
                    try:
                        distance = smart_dilate.compute_distance_transform_distance_GPU(small_image) #Retry dt on downsample
                        print(f"Using {down_factor} downsample ({downsample_needed} in each dim - largest possible with this GPU)")
                        break
                    except cp.cuda.memory.OutOfMemoryError:
                        down_factor += 1
                old_mask = smart_dilate.binarize(image)
                image = small_image
                del small_image
        else:
            goto_except = 1/0
    except Exception as e:
        if GPU:
            print("GPU dt failed or did not detect GPU (cupy must be installed with a CUDA toolkit setup...). Computing CPU distance transform instead.")
            print(f"Error message: {str(e)}")
        distance = smart_dilate.compute_distance_transform_distance(image)


    distance = threshold(distance, proportion, custom_rad = smallest_rad)

    labels, _ = label_objects(distance)

    del distance

    if labels.shape[1] < original_shape[1]: #If downsample was used, upsample output
        labels = upsample_with_padding(labels, downsample_needed, original_shape)
        labels = labels * old_mask
        labels = smart_dilate.smart_label(old_mask, labels, GPU = GPU, predownsample = predownsample2)
    else:
        labels = smart_dilate.smart_label(image, labels, GPU = GPU, predownsample = predownsample2)

    if directory is None:
        tifffile.imwrite("Watershed_output.tif", labels)
        print("Watershed saved to 'Watershed_output.tif'")
    else:
        tifffile.imwrite(f"{directory}/Watershed_output.tif", labels)
        print(f"Watershed saved to {directory}/'Watershed_output.tif'")

    return labels

def filter_by_size(array, proportion=0.1, directory = None):
    """
    Threshold out objects below a certain proportion of the total volume in a 3D binary array.
    
    :param array: (Mandatory; string or ndarray) - A file path to a 3D binary tif image array with objects or an ndarray of the same.
    :param proportion: (Optional - Val = 0.1; float): Proportion of the total volume to use as the threshold. Objects smaller tha this proportion of the total volume will be removed.
    :param directory: (Optional - Val = None; string): Optional file path to a directory to save output, otherwise active directory will be used.

    :returns: A 3D binary numpy array with small objects removed.
    """

    if type(array) == str:
        array = tifffile.imread(array)

    # Label connected components
    labeled_array, num_features = label_objects(array)

    # Calculate the volume of each object
    object_slices = ndimage.find_objects(labeled_array)
    object_volumes = np.array([np.sum(labeled_array[slc] == i + 1) for i, slc in enumerate(object_slices)])

    # Determine the threshold volume
    total_volume = np.sum(object_volumes)
    threshold_volume = total_volume * proportion
    print(f"threshold_volume is {threshold_volume}")

    # Filter out small objects
    large_objects = np.zeros_like(array, dtype=np.uint8)
    for i, vol in enumerate(object_volumes):
        print(f"Obj {i+1} vol is {vol}")
        if vol >= threshold_volume:
            large_objects[labeled_array == i + 1] = 1

    if directory is None:
        tifffile.imwrite('filtered_array.tif', large_objects)
    else:
        tifffile.imwrite(f'{directory}/filtered_array.tif', large_objects)

    return large_objects


def mask(image, mask, directory = None):
    """
    Can be used to mask one image with another. Masked output will be saved to the active directory if none is specified.
    :param image: (Mandatory, string or ndarray) - If string, a path to a tif file to get masked, or an ndarray of the same.
    :param mask: (Mandatory, string or ndarray) - If string, a path to a tif file to be a mask, or an ndarray of the same.
    :param directory: (Optional - Val = None; string) - A filepath to save outputs.
    :returns: a masked ndarray.
    """    
    if type(image) == str or type(mask) == str:
        string_bool = True
    else:
        string_bool = False

    if type(image) == str:
        image = tifffile.imread(image)
    if type(mask) == str:
        mask = tifffile.imread(mask)

    mask = mask != 0

    image = image * mask

    if string_bool:
        if directory is None:
            filename = tifffile.imwrite("masked_image.tif", image)
        else:
            filename = tifffile.imwrite(f"{directory}/masked_image.tif", image)
        print(f"Masked image saved to masked_image.tif")

    return image

def inverted_mask(image, mask, directory = None):
    """
    Can be used to mask one image with the inversion of another. Masked output will be saved to the active directory if none is specified.
    :param image: (Mandatory, string or ndarray) - If string, a path to a tif file to get masked, or an ndarray of the same.
    :param mask: (Mandatory, string or ndarray) - If string, a path to a tif file to be a mask, or an ndarray of the same.
    :param directory: (Optional - Val = None; string) - A filepath to save outputs.
    :returns: a masked ndarray.
    """    
    if type(image) == str or type(mask) == str:
        string_bool = True
    else:
        string_bool = False

    if type(image) == str:
        image = tifffile.imread(image)
    if type(mask) == str:
        mask = tifffile.imread(mask)

    mask = invert_array(mask)
    mask = mask != 0

    image = image * mask

    if string_bool:
        if directory is None:
            filename = tifffile.imwrite("masked_image.tif", image)
        else:
            filename = tifffile.imwrite(f"{directory}/masked_image.tif", image)
        print(f"Masked image saved to masked_image.tif")

    return image


def label(image, directory = None):
    """
    Can be used to label a binary image, where each discrete object is assigned its own grayscale value. Labelled output will be saved to the active directory if none is specified.
    :param image: (Mandatory, string or ndarray) - If string, a path to a tif file to get masked, or an ndarray of the same.
    :param directory: (Optional - Val = None; string) - A filepath to save outputs.
    :returns: a labelled ndarray.
    """    
    if type(image) == str:
        image = tifffile.imread(image)
    image, _ = label_objects(image)
    if directory is None:
        image = tifffile.imwrite('labelled_image.tif', image)
    else:
        image = tifffile.imwrite(f'{directory}/labelled_image.tif', image)

    return image

def encapsulate(parent_dir = None, name = None):
    """Used for saving outputs to a new directory called my_network"""

    import os

    if name is None:
        name = 'my_network'
    
    # Use current directory if no parent_dir specified
    if parent_dir is None:
        parent_dir = os.getcwd()
        
    # Create the full path for the new folder
    new_folder_path = os.path.join(parent_dir, name)
    
    # Create the folder if it doesn't exist
    os.makedirs(new_folder_path, exist_ok=True)
    
    return new_folder_path




#THE 3D NETWORK CLASS

class Network_3D:
    """A class to store various components of the 3D networks, to make working with them easier"""
    def __init__(self, nodes = None, network = None, xy_scale = 1, z_scale = 1, network_lists = None, edges = None, search_region = None, node_identities = None, node_centroids = None, edge_centroids = None, communities = None, network_overlay = None, id_overlay = None):
        """
        Constructor that initiates a Network_3D object. Note that xy_scale and z_scale attributes will default to 1 while all others will default to None.
        :attribute 1: (ndarray) _nodes - a 3D numpy array containing labelled objects that represent nodes in a network
        :attribute 2: (G) _network - a networkx graph object
        :attribute 3: (float) _xy_scale - a float representing the scale of each pixel in the nodes array.
        :attribute 4: (float) _z_scale - a float representing the depth of each voxel in the nodes array.
        :attribute 5: (dict) _network_lists - an internal set of lists that keep network data
        :attribute 6: _edges - a 3D numpy array containing labelled objects that represent edges in a network.
        :attribute 7: _search_region - a 3D numpy array containing labelled objects that represent nodes that have been expanded by some amount to search for connections.
        :attribute 8: _node_identities - a dictionary that relates all nodes to some string identity that details what the node actually represents
        :attribute 9: _node_centroids - a dictionary containing a [Z, Y, x] centroid for all labelled objects in the nodes attribute.
        :attribute 10: _edge_centroids - a dictionary containing a [Z, Y, x] centroid for all labelled objects in the edges attribute.
        :returns: a Network-3D classs object. 
        """
        self._nodes = nodes
        self._network = network
        self._xy_scale = xy_scale
        self._z_scale = z_scale
        self._network_lists = network_lists
        self._edges = edges
        self._search_region = search_region
        self._node_identities = node_identities
        self._node_centroids = node_centroids
        self._edge_centroids = edge_centroids
        self._communities = communities
        self._network_overlay = network_overlay
        self._id_overlay = id_overlay
        self.normalized_weights = None

    def copy(self):
        """
        Copies a Network_3D object so the new object can be freely editted independent of a previous one
        :return: a deep copy of a Network_3D object
        """
        return copy.deepcopy(self)

    #Getters/Setters:

    @property    
    def nodes(self):
        """
        A 3D labelled array for nodes
        :returns: the nodes attribute
        """
        return self._nodes

    @nodes.setter
    def nodes(self, array):
        """Sets the nodes property"""
        if array is not None and not isinstance(array, np.ndarray):
            raise ValueError("nodes must be a (preferably labelled) numpy array.")
        if array is not None and len(array.shape) == 2: #For dealing with 2D images
            #array = np.stack((array, array), axis = 0)
            array = np.expand_dims(array, axis=0)
        self._nodes = array

    @nodes.deleter
    def nodes(self):
        """Eliminates nodes property by setting it to 'None'"""
        self._nodes = None

    @property
    def network(self):
        """
        A networkx graph
        :returns: the network attribute.
        """
        return self._network

    @network.setter
    def network(self, G):
        """Sets the network property, which is intended be a networkx graph object. Additionally alters the network_lists property which is primarily an internal attribute"""
        if G is not None and not isinstance(G, nx.Graph):
            print("network attribute was not set to a networkX undirected graph, which may produce unintended results")
        if G is None:
            self._network = None 
            self._network_lists = None
            self.communities = None
            return

        self._network = G
        self.communities = None
        node_pairings = list(G.edges(data=True)) #Assembling the network lists property.
        lista = []
        listb = []
        listc = []

        try:
            #Networks default to have a weighted attribute of 1 if not otherwise weighted. Here we update the weights
            for u, v, data in node_pairings:
                weight = data.get('weight', 1)  # Default weight is 1 if not specified
                for _ in range(weight):
                    lista.append(u)
                    listb.append(v)
                    listc.append(weight)
            
            self._network_lists = [lista, listb, listc]


        except:
            pass


    @network.deleter
    def network(self):
        """Removes the network property by setting it to none"""
        self._network = None

    @property
    def network_lists(self):
        """
        A list with three lists. The first two lists are paired nodes (matched by index), the third is the edge that joins them.
        :returns: the network_lists attribute.
        """
        return self._network_lists

    @network_lists.setter
    def network_lists(self, value):
        """Sets the network_lists attribute"""
        if value is not None and not isinstance(value, list):
            raise ValueError("network lists must be a list.")
        self._network_lists = value
        self._network, _ = network_analysis.weighted_network(self._network_lists)
        self.communities = None

    @network_lists.deleter
    def network_lists(self):
        """Removes the network_lists attribute by setting it to None"""

        self._network_lists = None

    @property
    def xy_scale(self):
        """
        Pixel scaling
        :returns: the xy_scale attribute.
        """
        return self._xy_scale

    @xy_scale.setter
    def xy_scale(self, value):
        """Sets the xy_scale property."""
        self._xy_scale = value

    @property
    def z_scale(self):
        """
        Voxel Depth
        :returns: the z_scale attribute.
        """
        return self._z_scale

    @z_scale.setter
    def z_scale(self, value):
        """Sets the z_scale property"""
        self._z_scale = value

    @property
    def edges(self):
        """
        A 3D labelled array for edges.
        :returns: the edges attribute.
        """
        return self._edges

    @edges.setter
    def edges(self, array):
        """Sets the edges property"""
        if array is not None and not isinstance(array, np.ndarray):
            raise ValueError("edges must be a (preferably labelled) numpy array.")
        if array is not None and len(array.shape) == 2: #For dealing with 2D images
            #array = np.stack((array, array), axis = 0)
            array = np.expand_dims(array, axis=0)
        self._edges = array

    @edges.deleter
    def edges(self):
        """Removes the edges attribute by setting it to None"""
        self._edges = None

    @property
    def search_region(self):
        """
        A 3D labelled array for node search regions.
        :returns: the search_region attribute.
        """
        return self._search_region

    @search_region.setter
    def search_region(self, array):
        """Sets the search_region property"""
        if array is not None and not isinstance(array, np.ndarray):
            raise ValueError("search_region must be a (preferably labelled) numpy array.")
        if array is not None and len(array.shape) == 2: #For dealing with 2D images
            #array = np.stack((array, array), axis = 0)
            array = np.expand_dims(array, axis=0)
        self._search_region = array

    @search_region.deleter
    def search_region(self):
        """Removes the search_region attribute by setting it to None"""
        del self._search_region

    @property
    def node_identities(self):
        """
        A dictionary defining what object each node label refers to (for nodes that index multiple distinct biological objects).
        :returns: the node_identities attribute.
        """
        return self._node_identities

    @node_identities.setter
    def node_identities(self, value):
        """Sets the node_identities attribute"""
        if value is not None and not isinstance(value, dict):
            raise ValueError("node_identities must be a dictionary.")
        self._node_identities = value

    @property
    def node_centroids(self):
        """
        A dictionary of centroids for each node.
        :returns: the node_centroids attribute
        """
        return self._node_centroids

    @node_centroids.setter
    def node_centroids(self, value):
        """Sets the node_centroids property"""
        if value is not None and not isinstance(value, dict):
            raise ValueError("centroids must be a dictionary.")
        self._node_centroids = value

    @property
    def edge_centroids(self):
        """
        A dictionary of centroids for each edge.
        :returns: The _edge_centroids attribute.
        """
        return self._edge_centroids

    @edge_centroids.setter
    def edge_centroids(self, value):
        """Sets the edge_centroids property"""
        if value is not None and not isinstance(value, dict):
            raise ValueError("centroids must be a dictionary.")
        self._edge_centroids = value

    @property
    def communities(self):
        """
        A dictionary of community each node.
        :returns: The _communities attribute.
        """
        return self._communities

    @communities.setter
    def communities(self, value):
        """Sets the communities property"""
        if value is not None and not isinstance(value, dict):
            raise ValueError("communities must be a dictionary.")
        self._communities = value

    @property    
    def network_overlay(self):
        """
        A 3D network overlay
        :returns: the network overlay
        """
        return self._network_overlay

    @network_overlay.setter
    def network_overlay(self, array):
        """Sets the nodes property"""
        if array is not None and not isinstance(array, np.ndarray):
            raise ValueError("network overlay must be a (preferably labelled) numpy array.")
        if array is not None and len(array.shape) == 2: #For dealing with 2D images
            #array = np.stack((array, array), axis = 0)
            array = np.expand_dims(array, axis=0)
 
        self._network_overlay = array

    @property    
    def id_overlay(self):
        """
        A 3D id overlay
        :returns: the id overlay
        """
        return self._id_overlay

    @id_overlay.setter
    def id_overlay(self, array):
        """Sets the nodes property"""
        if array is not None and not isinstance(array, np.ndarray):
            raise ValueError("id overlay must be a (preferably labelled) numpy array.")
        if array is not None and len(array.shape) == 2: #For dealing with 2D images
            #array = np.stack((array, array), axis = 0)
            array = np.expand_dims(array, axis=0)
 
        self._id_overlay = array



    #Saving components of the 3D_network to hard mem:

    def save_nodes(self, directory = None, filename = None):
        """
        Can be called on a Network_3D object to save the nodes property to hard mem as a tif. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an indended directory to save the nodes to.
        """
        if filename is None:
            filename = "labelled_nodes.tif"
        elif not filename.endswith(('.tif', '.tiff')):
            filename += '.tif'

        if self._nodes is not None:
            if directory is None:
                try:
                    tifffile.imwrite(f"{filename}", self._nodes)
                    print(f"Nodes saved to {filename}")
                except Exception as e:
                    print("Could not save nodes")
            if directory is not None:
                try:
                    tifffile.imwrite(f"{directory}/{filename}", self._nodes)
                    print(f"Nodes saved to {directory}/{filename}")
                except Exception as e:
                    print(f"Could not save nodes to {directory}")
        if self._nodes is None:
            print("Node attribute is empty, did not save...")

    def save_edges(self, directory = None, filename = None):
        """
        Can be called on a Network_3D object to save the edges property to hard mem as a tif. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an indended directory to save the edges to.
        """

        if filename is None:
            filename = "labelled_edges.tif"
        elif not filename.endswith(('.tif', '.tiff')):
            filename += '.tif'

        if self._edges is not None:
            if directory is None:
                tifffile.imwrite(f"{filename}", self._edges)
                print(f"Edges saved to {filename}")

            if directory is not None:
                tifffile.imwrite(f"{directory}/{filename}", self._edges)
                print(f"Edges saved to {directory}/{filename}")

        if self._edges is None:
            print("Edges attribute is empty, did not save...")

    def save_scaling(self, directory = None):
        """
        Can be called on a Network_3D object to save the xy_scale and z_scale properties to hard mem as a .txt. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an indended directory to save the scalings to.
        """
        output_string = f"xy_scale: {self._xy_scale} \nz_scale: {self._z_scale}"

        if directory is None:
            file_name = "voxel_scalings.txt"
        else:
            file_name = f"{directory}/voxel_scalings.txt"

        with open(file_name, "w") as file:
            file.write(output_string)

        print(f"Voxel scaling has been written to {file_name}")

    def save_node_centroids(self, directory = None):
        """
        Can be called on a Network_3D object to save the node centroids properties to hard mem as a .xlsx file. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an indended directory to save the centroids to.
        """
        if self._node_centroids is not None:
            if directory is None:
                network_analysis._save_centroid_dictionary(self._node_centroids, 'node_centroids.xlsx')
                print("Centroids saved to node_centroids.xlsx")

            if directory is not None:
                network_analysis._save_centroid_dictionary(self._node_centroids, f'{directory}/node_centroids.xlsx')
                print(f"Centroids saved to {directory}/node_centroids.xlsx")

        if self._node_centroids is None:
            print("Node centroids attribute is empty, did not save...")

    def save_edge_centroids(self, directory = None):
        """
        Can be called on a Network_3D object to save the edge centroids properties to hard mem as a .xlsx file. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an indended directory to save the centroids to.
        """
        if self._edge_centroids is not None:
            if directory is None:
                network_analysis._save_centroid_dictionary(self._edge_centroids, 'edge_centroids.xlsx', index = 'Edge ID')
                print("Centroids saved to edge_centroids.xlsx")

            if directory is not None:
                network_analysis._save_centroid_dictionary(self._edge_centroids, f'{directory}/edge_centroids.xlsx', index = 'Edge ID')
                print(f"Centroids saved to {directory}/edge_centroids.xlsx")

        if self._edge_centroids is None:
            print("Edge centroids attribute is empty, did not save...")

    def save_search_region(self, directory = None):
        """
        Can be called on a Network_3D object to save the search_region property to hard mem as a tif. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an indended directory to save the search_region to.
        """
        if self._search_region is not None:
            if directory is None:
                tifffile.imwrite("search_region.tif", self._search_region)
                print("Search region saved to search_region.tif")

            if directory is not None:
                tifffile.imwrite(f"{directory}/search_region.tif", self._search_region)
                print(f"Search region saved to {directory}/search_region.tif")

        if self._search_region is None:
            print("Search_region attribute is empty, did not save...")

    def save_network(self, directory = None):
        """
        Can be called on a Network_3D object to save the network_lists property to hard mem as a .xlsx. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an intended directory to save the network lists to.
        """
        if self._network_lists is not None:
            if directory is None:

                temp_list = network_analysis.combine_lists_to_sublists(self._network_lists)
                create_and_save_dataframe(temp_list, 'output_network.xlsx')

            if directory is not None:
                temp_list = network_analysis.combine_lists_to_sublists(self._network_lists)

                create_and_save_dataframe(temp_list, f'{directory}/output_network.xlsx')

        if self._network_lists is None:
            print("Network associated attributes are empty (must set network_lists property to save network)...")

    def save_node_identities(self, directory = None):
        """
        Can be called on a Network_3D object to save the node_identities property to hard mem as a .xlsx. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an intended directory to save the node_identities to.
        """
        if self._node_identities is not None:
            if directory is None:
                network_analysis.save_singval_dict(self._node_identities, 'NodeID', 'Identity', 'node_identities.xlsx')
                print("Node identities saved to node_identities.xlsx")

            if directory is not None:
                network_analysis.save_singval_dict(self._node_identities, 'NodeID', 'Identity', f'{directory}/node_identities.xlsx')
                print(f"Node identities saved to {directory}/node_identities.xlsx")

        if self._node_identities is None:
            print("Node identities attribute is empty...")

    def save_communities(self, directory = None):
        """
        Can be called on a Network_3D object to save the communities property to hard mem as a .xlsx. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an intended directory to save the communities to.
        """
        if self._communities is not None:
            if directory is None:
                network_analysis.save_singval_dict(self._communities, 'NodeID', 'Community', 'node_communities.xlsx')
                print("Communities saved to node_communities.xlsx")

            if directory is not None:
                network_analysis.save_singval_dict(self._communities, 'NodeID', 'Community', f'{directory}/node_communities.xlsx')
                print(f"Communities saved to {directory}/node_communities.xlsx")

        if self._communities is None:
            print("Communities attribute is empty...")


    def save_network_overlay(self, directory = None, filename = None):


        if filename is None:
            filename = "overlay_1.tif"
        elif not filename.endswith(('.tif', '.tiff')):
            filename += '.tif'

        if self._network_overlay is not None:
            if directory is None:
                tifffile.imwrite(f"{filename}", self._network_overlay)
                print(f"Network overlay saved to {filename}")

            if directory is not None:
                tifffile.imwrite(f"{directory}/{filename}", self._network_overlay)
                print(f"Network overlay saved to {directory}/{filename}")

    def save_id_overlay(self, directory = None, filename = None):

        if filename is None:
            filename = "overlay_2.tif"
        if not filename.endswith(('.tif', '.tiff')):
            filename += '.tif'

        if self._id_overlay is not None:
            if directory is None:
                tifffile.imwrite(f"{filename}", self._id_overlay)
                print(f"Network overlay saved to {filename}")

            if directory is not None:
                tifffile.imwrite(f"{directory}/{filename}", self._id_overlay)
                print(f"ID overlay saved to {directory}/{filename}")



    def dump(self, directory = None, parent_dir = None, name = None):
        """
        Can be called on a Network_3D object to save the all properties to hard mem. It will save to the active directory if none is specified.
        :param directory: (Optional - Val = None; String). The path to an intended directory to save the properties to.
        """

        directory = encapsulate(parent_dir = parent_dir, name = name)

        try:
            self.save_nodes(directory)
            self.save_edges(directory)
            self.save_node_centroids(directory)
            self.save_search_region(directory)
            self.save_network(directory)
            self.save_node_identities(directory)
            self.save_edge_centroids(directory)
            self.save_scaling(directory)
            self.save_communities(directory)
            self.save_network_overlay(directory)
            self.save_id_overlay(directory)

        except:
            self.save_nodes()
            self.save_edges()
            self.save_node_centroids()
            self.save_search_region()
            self.save_network()
            self.save_node_identities()
            self.save_edge_centroids()
            self.save_scaling()
            self.save_communities()
            self.save_network_overlay()
            self.save_id_overlay()


    def load_nodes(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a tif into the nodes property as an ndarray. It will look for a file called 'labelled_nodes.tif' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any tiff file may be passed to load into the nodes property.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'labelled_nodes.tif' file.
        :param file_path: (Optional - Val = None; String). A path to any tif to load into the nodes property.
        """

        if file_path is not None:
            self._nodes = tifffile.imread(file_path)
            print("Succesfully loaded nodes")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'labelled_nodes.tif':
                if directory is not None:
                    self._nodes = tifffile.imread(f'{directory}/{item}')
                    print("Succesfully loaded nodes")
                    return
                else:
                    self._nodes = tifffile.imread(item)
                    print("Succesfully loaded nodes")
                    return


        print("Could not find nodes. They must be in the specified directory and named 'labelled_nodes.tif'")

    def load_edges(self, directory = None, file_path = None):

        """
        Can be called on a Network_3D object to load a tif into the edges property as an ndarray. It will look for a file called 'labelled_edges.tif' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any tiff file may be passed to load into the edges property.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'labelled_edges.tif' file.
        :param file_path: (Optional - Val = None; String). A path to any tif to load into the edges property.
        """

        if file_path is not None:
            self._edges = tifffile.imread(file_path)
            print("Succesfully loaded edges")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'labelled_edges.tif':
                if directory is not None:
                    self._edges = tifffile.imread(f'{directory}/{item}')
                    print("Succesfully loaded edges")
                    return
                else:
                    self._edges = tifffile.imread(item)
                    print("Succesfully loaded edges")
                    return

        print("Could not find edges. They must be in the specified directory and named 'labelled_edges.tif'")

    def load_scaling(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a .txt into the xy_scale and z_scale properties as floats. It will look for a file called 'voxel_scalings.txt' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any txt file may be passed to load into the xy_scale/z_scale properties, however they must be formatted the same way as the 'voxel_scalings.txt' file.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'voxel_scalings.txt' file.
        :param file_path: (Optional - Val = None; String). A path to any txt to load into the xy_scale/z_scale properties.
        """
        def read_scalings(file_name):
            """Internal function for reading txt scalings"""
            # Initialize variables
            variable1 = 1
            variable2 = 1

            # Read the file and extract the variables
            with open(file_name, "r") as file:
                for line in file:
                    if "xy_scale:" in line:
                        variable1 = float(line.split(":")[1].strip())
                    elif "z_scale:" in line:
                        variable2 = float(line.split(":")[1].strip())

            return variable1, variable2

        if file_path is not None:
            self._xy_scale, self_z_scale = read_scalings(file_path)
            print("Succesfully loaded voxel_scalings")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'voxel_scalings.txt':
                if directory is not None:
                    self._xy_scale, self._z_scale = read_scalings(f"{directory}/{item}")
                    print("Succesfully loaded voxel_scalings")
                    return
                else:
                    self._xy_scale, self._z_scale = read_scalings(item)
                    print("Succesfully loaded voxel_scalings")
                    return

        print("Could not find voxel scalings. They must be in the specified directory and named 'voxel_scalings.txt'")

    def load_network(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a .xlsx into the network and network_lists properties as a networx graph and a list of lists, respecitvely. It will look for a file called 'output_network.xlsx' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any .xlsx file may be passed to load into the network/network_lists properties, however they must be formatted the same way as the 'output_network.xlsx' file.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'output_network.xlsx' file.
        :param file_path: (Optional - Val = None; String). A path to any .xlsx to load into the network/network_lists properties.
        """
        if file_path is not None:
            self._network, net_weights = network_analysis.weighted_network(file_path)
            self._network_lists = network_analysis.read_excel_to_lists(file_path)
            print("Succesfully loaded network")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'output_network.xlsx' or item == 'output_network.csv':
                if directory is not None:
                    self._network, net_weights = network_analysis.weighted_network(f'{directory}/{item}')
                    self._network_lists = network_analysis.read_excel_to_lists(f'{directory}/{item}')
                    print("Succesfully loaded network")
                    return
                else:
                    self._network, net_weights = network_analysis.weighted_network(item)
                    self._network_lists = network_analysis.read_excel_to_lists(item)
                    print("Succesfully loaded network")
                    return

        print("Could not find network. It must be stored in specified directory and named 'output_network.xlsx' or 'output_network.csv'")

    def load_search_region(self, directory = None, file_path = None):

        """
        Can be called on a Network_3D object to load a tif into the search_region property as an ndarray. It will look for a file called 'search_region.tif' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any tiff file may be passed to load into the search_region property.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'search_region.tif' file.
        :param file_path: (Optional - Val = None; String). A path to any tif to load into the search_region property.
        """

        if file_path is not None:
            self._search_region = tifffile.imread(file_path)
            print("Succesfully loaded search regions")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'search_region.tif':
                if directory is not None:
                    self._search_region = tifffile.imread(f'{directory}/{item}')
                    print("Succesfully loaded search regions")
                    return
                else:
                    self._search_region = tifffile.imread(item)
                    print("Succesfully loaded search regions")
                    return

        print("Could not find search region. It must be in the specified directory and named 'search_region.tif'")

    def load_node_centroids(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a .xlsx into the node_centroids property as a dictionary. It will look for a file called 'node_centroids.xlsx' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any .xlsx file may be passed to load into the node_centroids property, however they must be formatted the same way as the 'node_centroids.xlsx' file.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'node_centroids.xlsx' file.
        :param file_path: (Optional - Val = None; String). A path to any .xlsx to load into the node_centroids property.
        """

        if file_path is not None:
            self._node_centroids = network_analysis.read_centroids_to_dict(file_path)
            print("Succesfully loaded node centroids")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'node_centroids.xlsx' or item == 'node_centroids.csv':
                if directory is not None:
                    self._node_centroids = network_analysis.read_centroids_to_dict(f'{directory}/{item}')
                    print("Succesfully loaded node centroids")
                    return
                else:
                    self._node_centroids = network_analysis.read_centroids_to_dict(item)
                    print("Succesfully loaded node centroids")
                    return

        print("Could not find node centroids. They must be in the specified directory and named 'node_centroids.xlsx'")

    def load_node_identities(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a .xlsx into the node_identities property as a dictionary. It will look for a file called 'node_identities.xlsx' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any .xlsx file may be passed to load into the node_identities property, however they must be formatted the same way as the 'node_identities.xlsx' file.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'node_identities.xlsx' file.
        :param file_path: (Optional - Val = None; String). A path to any .xlsx to load into the node_identities property.
        """

        if file_path is not None:
            self._node_identities = network_analysis.read_excel_to_singval_dict(file_path)
            print("Succesfully loaded node identities")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'node_identities.xlsx' or item == 'node_identities.csv':
                if directory is not None:
                    self._node_identities = network_analysis.read_excel_to_singval_dict(f'{directory}/{item}')
                    print("Succesfully loaded node identities")
                    return
                else:
                    self._node_identities = network_analysis.read_excel_to_singval_dict(item)
                    print("Succesfully loaded node identities")
                    return

        print("Could not find node identities. They must be in the specified directory and named 'node_identities.xlsx'")

    def load_communities(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a .xlsx into the communities property as a dictionary. It will look for a file called 'node_communities.xlsx' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any .xlsx file may be passed to load into the node_communities property, however they must be formatted the same way as the 'node_communities.xlsx' file.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'node_identities.xlsx' file.
        :param file_path: (Optional - Val = None; String). A path to any .xlsx to load into the node_identities property.
        """

        if file_path is not None:
            self._node_identities = network_analysis.read_excel_to_singval_dict(file_path)
            print("Succesfully loaded communities")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'node_communities.xlsx' or item == 'node_communities.csv':
                if directory is not None:
                    self._communities = network_analysis.read_excel_to_singval_dict(f'{directory}/{item}')
                    print("Succesfully loaded communities")
                    return
                else:
                    self._communities = network_analysis.read_excel_to_singval_dict(item)
                    print("Succesfully loaded communities")
                    return

        print("Could not find communities. They must be in the specified directory and named 'node_communities.xlsx'")

    def load_edge_centroids(self, directory = None, file_path = None):
        """
        Can be called on a Network_3D object to load a .xlsx into the edge_centroids property as a dictionary. It will look for a file called 'edge_centroids.xlsx' in the specified directory,
        or the active directory if none has been selected. Alternatively, a file path to any .xlsx file may be passed to load into the edge_centroids property, however they must be formatted the same way as the 'edge_centroids.xlsx' file.
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the 'edge_centroids.xlsx' file.
        :param file_path: (Optional - Val = None; String). A path to any .xlsx to load into the edge_centroids property.
        """

        if file_path is not None:
            self._edge_centroids = network_analysis.read_centroids_to_dict(file_path)
            print("Succesfully loaded edge centroids")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'edge_centroids.xlsx' or item == 'edge_centroids.csv':
                if directory is not None:
                    self._edge_centroids = network_analysis.read_centroids_to_dict(f'{directory}/{item}')
                    print("Succesfully loaded edge centroids")
                    return
                else:
                    self._edge_centroids = network_analysis.read_centroids_to_dict(item)
                    print("Succesfully loaded edge centroids")
                    return

        print("Could not find edge centroids. They must be in the specified directory and named 'edge_centroids.xlsx', or otherwise specified")


    def load_network_overlay(self, directory = None, file_path = None):


        if file_path is not None:
            self._network_overlay = tifffile.imread(file_path)
            print("Succesfully loaded network overlay")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'overlay_1.tif':
                if directory is not None:
                    self._network_overlay = tifffile.imread(f'{directory}/{item}')
                    print("Succesfully loaded network overlay")
                    return
                else:
                    self._network_overlay = tifffile.imread(item)
                    print("Succesfully loaded network overlay")
                    return


        #print("Could not find network overlay. They must be in the specified directory and named 'drawn_network.tif'")


    def load_id_overlay(self, directory = None, file_path = None):


        if file_path is not None:
            self._id_overlay = tifffile.imread(file_path)
            print("Succesfully loaded network overlay")
            return

        items = directory_info(directory)

        for item in items:
            if item == 'overlay_2.tif':
                if directory is not None:
                    self._id_overlay = tifffile.imread(f'{directory}/{item}')
                    print("Succesfully loaded id overlay")
                    return
                else:
                    self._id_overlay = tifffile.imread(item)
                    print("Succesfully loaded id overlay")
                    return


        #print("Could not find id overlay. They must be in the specified directory and named 'labelled_node_indices.tif'")


    def assemble(self, directory = None, node_path = None, edge_path = None, search_region_path = None, network_path = None, node_centroids_path = None, node_identities_path = None, edge_centroids_path = None, scaling_path = None, net_overlay_path = None, id_overlay_path = None, community_path = None ):
        """
        Can be called on a Network_3D object to load all properties simultaneously from a specified directory. It will look for files with the names specified in the property loading methods, in the active directory if none is specified.
        Alternatively, for each property a filepath to any file may be passed to look there to load. This method is intended to be used together with the dump method to easily save and load the Network_3D objects once they had been calculated. 
        :param directory: (Optional - Val = None; String). The path to an intended directory to search for the all property files.
        :param node_path: (Optional - Val = None; String). A path to any .tif to load into the nodes property.
        :param edge_path: (Optional - Val = None; String). A path to any .tif to load into the edges property.
        :param search_region_path: (Optional - Val = None; String). A path to any .tif to load into the search_region property.
        :param network_path: (Optional - Val = None; String). A path to any .xlsx file to load into the network and network_lists properties.
        :param node_centroids_path: (Optional - Val = None; String). A path to any .xlsx to load into the node_centroids property.
        :param node_identities_path: (Optional - Val = None; String). A path to any .xlsx to load into the node_identities property.
        :param edge_centroids_path: (Optional - Val = None; String). A path to any .xlsx to load into the edge_centroids property.
        :param scaling_path: (Optional - Val = None; String). A path to any .txt to load into the xy_scale and z_scale properties.
        """

        print(f"Assembling Network_3D object from files stored in directory: {directory}")
        self.load_nodes(directory, node_path)
        self.load_edges(directory, edge_path)
        self.load_search_region(directory, search_region_path)
        self.load_network(directory, network_path)
        self.load_node_centroids(directory, node_centroids_path)
        self.load_node_identities(directory, node_identities_path)
        self.load_edge_centroids(directory, edge_centroids_path)
        self.load_scaling(directory, scaling_path)
        self.load_communities(directory, community_path)
        self.load_network_overlay(directory, net_overlay_path)
        self.load_id_overlay(directory, id_overlay_path)


    #Assembling additional Network_3D class attributes if they were not set when generating the network:

    def calculate_node_centroids(self, down_factor = None, GPU = False):

        """
        Method to obtain node centroids. Expects _nodes property to be set. Downsampling is optional to speed up the process. Centroids will be scaled to 'true' undownsampled location when downsampling is used.
        Sets the _node_centroids attribute.
        :param down_factor: (Optional - Val = None; int). Optional factor to downsample nodes during centroid calculation to increase speed.
        """

        if not hasattr(self, '_nodes') or self._nodes is None:
            print("Requires .nodes property to be set with a (preferably labelled) numpy array for node objects")
            raise AttributeError("._nodes property is not set")

        if not GPU:
            node_centroids = network_analysis._find_centroids(self._nodes, down_factor = down_factor)
        else:
            node_centroids = network_analysis._find_centroids_GPU(self._nodes, down_factor = down_factor)


        if down_factor is not None:
            for item in node_centroids:
                node_centroids[item] = node_centroids[item] * down_factor

        self._node_centroids = node_centroids

    def calculate_edge_centroids(self, down_factor = None):

        """
        Method to obtain edge centroids. Expects _edges property to be set. Downsampling is optional to speed up the process. Centroids will be scaled to 'true' undownsampled location when downsampling is used.
        Sets the _edge_centroids attribute.
        :param down_factor: (Optional - Val = None; int). Optional factor to downsample edges during centroid calculation to increase speed.
        """

        if not hasattr(self, '_edges') or self._edges is None:
            print("Requires .edges property to be set with a (preferably labelled) numpy array for node objects")
            raise AttributeError("._edges property is not set")


        edge_centroids = network_analysis._find_centroids(self._edges, down_factor = down_factor)

        if down_factor is not None:
            for item in edge_centroids:
                edge_centroids[item] = edge_centroids[item] * down_factor

        self._edge_centroids = edge_centroids

    def calculate_search_region(self, search_region_size, GPU = True, fast_dil = False, GPU_downsample = None):

        """
        Method to obtain the search region that will be used to assign connectivity between nodes. May be skipped if nodes do not want to search and only want to look for their 
        connections in their immediate overlap. Expects the nodes property to be set. Sets the search_region property.
        :param search_region_size: (Mandatory; int). Amount nodes should expand outward to search for connections. Note this value corresponds one-to-one with voxels unless voxel_scaling has been set, in which case it will correspond to whatever value the nodes array is measured in (microns, for example).
        :param GPU: (Optional - Val = True; boolean). Will use GPU if avaialble (including necessary downsampling for GPU RAM). Set to False to use CPU with no downsample.
        :param fast_dil: (Optional - Val = False, boolean) - A boolean that when True will utilize faster cube dilation but when false will use slower spheroid dilation.

        """

        dilate_xy, dilate_z = dilation_length_to_pixels(self._xy_scale, self._z_scale, search_region_size, search_region_size) #Get true dilation sizes based on voxel scaling and search region.

        if not hasattr(self, '_nodes') or self._nodes is None:
            print("Requires .nodes property to be set with a (preferably labelled) numpy array for node objects")
            raise AttributeError("._nodes property is not set")

        if search_region_size != 0:

            self._search_region = smart_dilate.smart_dilate(self._nodes, dilate_xy, dilate_z, GPU = GPU, fast_dil = fast_dil, predownsample = GPU_downsample) #Call the smart dilate function which essentially is a fast way to enlarge nodes into a 'search region' while keeping their unique IDs.

        else:

            self._search_region = self._nodes

    def calculate_edges(self, binary_edges, diledge = None, inners = True, hash_inner_edges = True, search = None, remove_edgetrunk = 0, GPU = True, fast_dil = False, skeletonized = False):
        """
        Method to calculate the edges that are used to directly connect nodes. May be done with or without the search region, however using search_region is recommended. 
        The search_region property must be set to use the search region, otherwise the nodes property must be set. Sets the edges property
        :param binary_edges: (Mandatory; String or ndarray). Filepath to a binary tif containing segmented edges, or a numpy array of the same. 
        :param diledge: (Optional - Val = None; int). Amount to dilate edges, to account for imaging and segmentation artifacts that have brokenup edges. Any edge masks that are within half the value of the 'diledge' param will become connected. Ideally edges should not have gaps,
        so some amount of dilation is recommended if there are any, but  not so much to create overconnectivity. This is a value that needs to be tuned by the user.
        :param inners: (Optional - Val = True; boolean). Will use inner edges if True, will not if False. Inner edges are parts of the edge mask that exist within search regions. If search regions overlap, 
        any edges that exist within the overlap will only assert connectivity if 'inners' is True.
        :param hash_inner_edges: (Optional - Val = True; boolean). If False, all search regions that contain an edge object connecting multiple nodes will be assigned as connected.
        If True, an extra processing step is used to sort the correct connectivity amongst these search_regions. Can only be computed when search_regions property is set.
        :param search: (Optional - Val = None; int). Amount for nodes to search for connections, assuming the search_regions are not being used. Assigning a value to this param will utilize the secondary algorithm and not the search_regions.
        :param remove_edgetrunk: (Optional - Val = 0; int). Amount of times to remove the 'Trunk' from the edges. A trunk in this case is the largest (by vol) edge object remaining after nodes have broken up the edges.
        Any 'Trunks' removed will be absent for connection calculations.
        :param GPU: (Optional - Val = True; boolean). Will use GPU (if available) for the hash_inner_edges step if True, if False will use CPU. Note that the speed is comparable either way.
        :param skeletonize: (Optional - Val = False, boolean) - A boolean of whether to skeletonize the edges when using them.
        """
        if not hasattr(self, '_search_region') or self._search_region is None:
            if not hasattr(self, '_nodes') or self._nodes is None:
                print("Requires .search_region property to be set with a (preferably labelled) numpy array for node search regions, or nodes property to be set and method to be passed a 'search = 'some float'' arg")
                raise AttributeError("._search_region/_nodes property is not set")

        if type(binary_edges) == str:
            binary_edges = tifffile.imread(binary_edges)

        if skeletonized:
            binary_edges = skeletonize(binary_edges)

        if search is not None and hasattr(self, '_nodes') and self._nodes is not None:
            search_region = binarize(self._nodes)
            dilate_xy, dilate_z = dilation_length_to_pixels(self._xy_scale, self._z_scale, search, search)
            if not fast_dil:
                search_region = dilate_3D(search_region, dilate_xy, dilate_xy, dilate_z)
            else:
                search_region = dilate_3D_old(search_region, dilate_xy, dilate_xy, dilate_z)

        else:
            search_region = binarize(self._search_region)

        outer_edges = establish_edges(search_region, binary_edges)

        if not inners:
            del binary_edges

        if remove_edgetrunk > 0:
            for i in range(remove_edgetrunk):
                print(f"Snipping trunk {i + 1}...")
                outer_edges = remove_trunk(outer_edges)

        if diledge is not None:
            dilate_xy, dilate_z = dilation_length_to_pixels(self._xy_scale, self._z_scale, diledge, diledge)
            if not fast_dil and dilate_xy > 3 and dilate_z > 3:
                outer_edges = dilate_3D(outer_edges, dilate_xy, dilate_xy, dilate_z)
            else:
                outer_edges = dilate_3D_old(outer_edges, dilate_xy, dilate_xy, dilate_z)

        else:
            outer_edges = dilate_3D_old(outer_edges, 3, 3, 3)

        labelled_edges, num_edge = label_objects(outer_edges)

        if inners:

            if search is None and hash_inner_edges is True:
                inner_edges = hash_inners(self._search_region, binary_edges, GPU = GPU)
            else:
                inner_edges = establish_inner_edges(search_region, binary_edges)

            del binary_edges

            inner_labels, num_edge = label_objects(inner_edges)

            del inner_edges

            labelled_edges = combine_edges(labelled_edges, inner_labels)

            num_edge = np.max(labelled_edges)

            if num_edge < 256:
                labelled_edges = labelled_edges.astype(np.uint8)
            elif num_edge < 65536:
                labelled_edges = labelled_edges.astype(np.uint16)

        self._edges = labelled_edges

    def label_nodes(self):
        """
        Method to assign a unique numerical label to all discrete objects contained in the ndarray in the nodes property.
        Expects the nodes property to be set to (presumably) a binary ndarray. Sets the nodes property.
        """
        self._nodes, num_nodes = label_objects(nodes, structure_3d)

    def merge_nodes(self, addn_nodes_name, label_nodes = True):
        """
        Merges the self._nodes attribute with alternate labelled node images. The alternate nodes can be inputted as a string for a filepath to a tif,
        or as a directory address containing only tif images, which will merge the _nodes attribute with all tifs in the folder. The _node_identities attribute
        meanwhile will keep track of which labels in the merged array refer to which objects, letting user track multiple seperate biological objects
        in a single network. Note that an optional param, 'label_nodes' is set to 'True' by default. This will cause the program to label any intended
        additional nodes based on seperation in the image. If your nodes a prelabelled, please input the argument 'label_nodes = False'
        :param addn_nodes_name: (Mandatory; String). Path to either a tif file or a directory containing only additional node files.
        :param label_nodes: (Optional - Val = True; Boolean). Will label all discrete objects in each node file being merged if True. If False, will not label.
        """

        nodes_name = 'Root_Nodes'

        identity_dict = {} #A dictionary to deliniate the node identities

        try: #Try presumes the input is a tif
            addn_nodes = tifffile.imread(addn_nodes_name) #If not this will fail and activate the except block

            if label_nodes is True:
                addn_nodes, num_nodes2 = label_objects(addn_nodes) # Label the node objects. Note this presumes no overlap between node masks.
                node_labels, identity_dict = combine_nodes(self._nodes, addn_nodes, addn_nodes_name, identity_dict, nodes_name) #This method stacks labelled arrays
                num_nodes = np.max(node_labels)

            else: #If nodes already labelled
                node_labels, identity_dict = combine_nodes(self._nodes, addn_nodes, addn_nodes_name, identity_dict, nodes_name)
                num_nodes = int(np.max(node_labels))

        except: #Exception presumes the input is a directory containing multiple tifs, to allow multi-node stackage.

            addn_nodes_list = directory_info(addn_nodes_name)

            for i, addn_nodes in enumerate(addn_nodes_list):
                try:
                    addn_nodes_ID = addn_nodes
                    addn_nodes = tifffile.imread(f'{addn_nodes_name}/{addn_nodes}')

                    if label_nodes is True:
                        addn_nodes, num_nodes2 = label_objects(addn_nodes)  # Label the node objects. Note this presumes no overlap between node masks.
                        if i == 0:
                            node_labels, identity_dict = combine_nodes(self._nodes, addn_nodes, addn_nodes_ID, identity_dict, nodes_name)

                        else:
                            node_labels, identity_dict = combine_nodes(node_labels, addn_nodes, addn_nodes_ID, identity_dict)

                    else:
                        if i == 0:
                            node_labels, identity_dict = combine_nodes(self._nodes, addn_nodes, addn_nodes_ID, identity_dict, nodes_name)
                        else:
                            node_labels, identity_dict = combine_nodes(node_labels, addn_nodes, addn_nodes_ID, identity_dict)
                except Exception as e:
                    print("Could not open additional nodes, verify they are being inputted correctly...")

        num_nodes = int(np.max(node_labels))

        self._node_identities = identity_dict

        if num_nodes < 256:
            dtype = np.uint8
        elif num_nodes < 65536:
            dtype = np.uint16
        else:
            dtype = np.uint32

        # Convert the labeled array to the chosen data type
        node_labels = node_labels.astype(dtype)

        self._nodes = node_labels

    def calculate_network(self, search = None, ignore_search_region = False):

        """
        Method to calculate the network from the labelled nodes and edge properties, once they have been calculated. Network connections are assigned based on node overlap along
        the same edge of some particular label. Sets the network and network_lists properties.
        :param search: (Optional - Val = None; Int). Amount for nodes to search for connections if not using the search_regions to find connections.
        :param ignore_search_region: (Optional - Val = False; Boolean). If False, will use primary algorithm (with search_regions property) to find connections. If True, will use secondary algorithm (with nodes) to find connections.
        """

        if not ignore_search_region and hasattr(self, '_search_region') and self._search_region is not None and hasattr(self, '_edges') and self._edges is not None:
            num_edge_1 = np.max(self._edges)
            edge_labels, trim_node_labels = array_trim(self._edges, self._search_region)
            connections_parallel = establish_connections_parallel(edge_labels, num_edge_1, trim_node_labels)
            del edge_labels
            connections_parallel = extract_pairwise_connections(connections_parallel)
            df = create_and_save_dataframe(connections_parallel)
            self._network_lists = network_analysis.read_excel_to_lists(df)
            self._network, net_weights = network_analysis.weighted_network(df)

        if ignore_search_region and hasattr(self, '_edges') and self._edges is not None and hasattr(self, '_nodes') and self._nodes is not None and search is not None:
            dilate_xy, dilate_z = dilation_length_to_pixels(self._xy_scale, self._z_scale, search, search)
            print(f"{dilate_xy}, {dilate_z}")
            num_nodes = np.max(self._nodes)
            connections_parallel = create_node_dictionary(self._nodes, self._edges, num_nodes, dilate_xy, dilate_z) #Find which edges connect which nodes and put them in a dictionary.
            connections_parallel = find_shared_value_pairs(connections_parallel) #Sort through the dictionary to find connected node pairs.
            df = create_and_save_dataframe(connections_parallel)
            self._network_lists = network_analysis.read_excel_to_lists(df)
            self._network, net_weights = network_analysis.weighted_network(df)

    def calculate_all(self, nodes, edges, xy_scale = 1, z_scale = 1, down_factor = None, search = None, diledge = None, inners = True, hash_inners = True, remove_trunk = 0, ignore_search_region = False, other_nodes = None, label_nodes = True, directory = None, GPU = True, fast_dil = False, skeletonize = False, GPU_downsample = None):
        """
        Method to calculate and save to mem all properties of a Network_3D object. In general, after initializing a Network_3D object, this method should be called on the node and edge masks that will be used to calculate the network.
        :param nodes: (Mandatory; String or ndarray). Filepath to segmented nodes mask or a numpy array containing the same.
        :param edges: (Mandatory; String or ndarray). Filepath to segmented edges mask or a numpy array containing the same.
        :param xy_scale: (Optional - Val = 1; Float). Pixel scaling to convert pixel sizes to some real value (such as microns).
        :param z_scale: (Optional - Val = 1; Float). Voxel depth to convert voxel depths to some real value (such as microns).
        :param down_factor: (Optional - Val = None; int). Optional factor to downsample nodes and edges during centroid calculation to increase speed. Note this only applies to centroid calculation and that the outputed centroids will correspond to the full-sized file. On-line general downsampling is not supported by this method and should be computed on masks before inputting them.
        :param search: (Optional - Val = None; int). Amount nodes should expand outward to search for connections. Note this value corresponds one-to-one with voxels unless voxel_scaling has been set, in which case it will correspond to whatever value the nodes array is measured in (microns, for example). If unset, only directly overlapping nodes and edges will find connections.
        :param diledge: (Optional - Val = None; int). Amount to dilate edges, to account for imaging and segmentation artifacts that have brokenup edges. Any edge masks that are within half the value of the 'diledge' param will become connected. Ideally edges should not have gaps,
        so some amount of dilation is recommended if there are any, but not so much to create overconnectivity. This is a value that needs to be tuned by the user.
        :param inners: (Optional - Val = True; boolean). Will use inner edges if True, will not if False. Inner edges are parts of the edge mask that exist within search regions. If search regions overlap, 
        any edges that exist within the overlap will only assert connectivity if 'inners' is True.
        :param hash_inners: (Optional - Val = True; boolean). If False, all search regions that contain an edge object connecting multiple nodes will be assigned as connected.
        If True, an extra processing step is used to sort the correct connectivity amongst these search_regions. Can only be computed when search_regions property is set.
        :param remove_trunk: (Optional - Val = 0; int). Amount of times to remove the 'Trunk' from the edges. A trunk in this case is the largest (by vol) edge object remaining after nodes have broken up the edges.
        Any 'Trunks' removed will be absent for connection calculations.
        :param ignore_search_region: (Optional - Val = False; boolean). If False, will use primary algorithm (with search_regions property) to find connections. If True, will use secondary algorithm (with nodes) to find connections.
        :param other_nodes: (Optional - Val = None; string). Path to either a tif file or a directory containing only additional node files to merge with the original nodes, assuming multiple 'types' of nodes need comparing. Node identities will be retained.
        :param label_nodes: (Optional - Val = True; boolean). If True, all discrete objects in the node param (and all those contained in the optional other_nodes param) will be assigned a label. If files a prelabelled, set this to False to avoid labelling.
        :param directory: (Optional - Val = None; string). Path to a directory to save to hard mem all Network_3D properties. If not set, these values will be saved to the active directory.
        :param GPU: (Optional - Val = True; boolean). Will use GPU if avaialble for calculating the search_region step (including necessary downsampling for GPU RAM). Set to False to use CPU with no downsample. Note this only affects the search_region step.
        :param fast_dil: (Optional - Val = False, boolean) - A boolean that when True will utilize faster cube dilation but when false will use slower spheroid dilation.
        :param skeletonize: (Optional - Val = False, boolean) - A boolean of whether to skeletonize the edges when using them.
        """


        directory = encapsulate()

        self._xy_scale = xy_scale
        self._z_scale = z_scale

        self.save_scaling(directory)

        if search is None and ignore_search_region == False:
            search = 0

        if type(nodes) == str:
            nodes = tifffile.imread(nodes)

        self._nodes = nodes
        del nodes

        if label_nodes:
            self._nodes, num_nodes = label_objects(self._nodes)
        if other_nodes is not None:
            self.merge_nodes(other_nodes, label_nodes)

        self.save_nodes(directory)
        self.save_node_identities(directory)

        if not ignore_search_region:
            self.calculate_search_region(search, GPU = GPU, fast_dil = fast_dil, GPU_downsample = GPU_downsample)
            self._nodes = None
            search = None
            self.save_search_region(directory)

        self.calculate_edges(edges, diledge = diledge, inners = inners, hash_inner_edges = hash_inners, search = search, remove_edgetrunk = remove_trunk, GPU = GPU, fast_dil = fast_dil, skeletonized = skeletonize)
        del edges
        self.save_edges(directory)

        self.calculate_network(search = search, ignore_search_region = ignore_search_region)
        self.save_network(directory)

        if self._nodes is None:
            self.load_nodes(directory)

        self.calculate_node_centroids(down_factor)
        self.save_node_centroids(directory)
        self.calculate_edge_centroids(down_factor)
        self.save_edge_centroids(directory)


    def draw_network(self, directory = None, down_factor = None, GPU = False):
        """
        Method that draws the 3D network lattice for a Network_3D object, to be used as an overlay for viewing network connections. 
        Lattice will be saved as a .tif to the active directory if none is specified. Will used the node_centroids property for faster computation, unless passed the down_factor param.
        :param directory: (Optional - Val = None; string). Path to a directory to save the network lattice to.
        :param down_factor: (Optional - Val = None; int).  Factor to downsample nodes by for calculating centroids. The node_centroids property will be used if this value is not set. If there are no node_centroids, this value must be set (to 1 or higher).
        """

        if down_factor is not None:
            nodes = downsample(self._nodes, down_factor)
            centroids = self._node_centroids.copy()

            for item in centroids:
                centroids[item] = np.round(centroids[item]/down_factor)

            output = network_draw.draw_network_from_centroids(nodes, self._network_lists, centroids, twod_bool = False, directory = directory)

        else:

            if not GPU:
                output = network_draw.draw_network_from_centroids(self._nodes, self._network_lists, self._node_centroids, twod_bool = False, directory = directory)
            else:
                output = network_draw.draw_network_from_centroids_GPU(self._nodes, self._network_lists, self._node_centroids, twod_bool = False, directory = directory)

        return output        

    def draw_node_indices(self, directory = None, down_factor = None):
        """
        Method that draws the numerical IDs for nodes in a Network_3D object, to be used as an overlay for viewing node IDs. 
        IDs will be saved as a .tif to the active directory if none is specified. Will used the node_centroids property for faster computation, unless passed the down_factor param.
        :param directory: (Optional - Val = None; string). Path to a directory to save the node_indicies to.
        :param down_factor: (Optional - Val = None; int).  Factor to downsample nodes by for calculating centroids. The node_centroids property will be used if this value is not set. If there are no node_centroids, this value must be set (to 1 or higher).
        """

        num_nodes = np.max(self._nodes)

        if down_factor is not None:
            nodes = downsample(self._nodes, down_factor)
            centroids = self._node_centroids.copy()

            for item in centroids:
                centroids[item] = np.round(centroids[item]/down_factor)

            output = node_draw.draw_from_centroids(nodes, num_nodes, centroids, twod_bool = False, directory = directory)

        else:

            output = node_draw.draw_from_centroids(self._nodes, num_nodes, self._node_centroids, twod_bool = False, directory = directory)

        return output

    def draw_edge_indices(self, directory = None, down_factor = None):
        """
        Method that draws the numerical IDs for edges in a Network_3D object, to be used as an overlay for viewing edge IDs. 
        IDs will be saved as a .tif to the active directory if none is specified. Will used the edge_centroids property for faster computation, unless passed the down_factor param.
        :param directory: (Optional - Val = None; string). Path to a directory to save the edge indices to.
        :param down_factor: (Optional - Val = None; int).  Factor to downsample edges by for calculating centroids. The edge_centroids property will be used if this value is not set. If there are no edgde_centroids, this value must be set (to 1 or higher).
        """

        num_edge = np.max(self._edges)

        if down_factor is not None:
            edges = downsample(self._edges, down_factor)
            centroids = self._edge_centroids.copy()

            for item in centroids:
                centroids[item] = np.round(centroids[item]/down_factor)

            output = node_draw.draw_from_centroids(edges, num_edge, centroids, twod_bool = False, directory = directory)

        else:

            output = node_draw.draw_from_centroids(self._edges, num_edge, self._edge_centroids, twod_bool = False, directory = directory)

        return output



    #Some methods that may be useful:

    def community_partition(self, weighted = False, style = 0, dostats = True):
        """
        Sets the communities attribute by splitting the network into communities
        """

        self._communities, self.normalized_weights, stats = modularity.community_partition(self._network_lists, weighted = weighted, style = style, dostats = dostats)

        return stats

    def remove_edge_weights(self):
        """
        Remove the weights from a network. Requires _network object to be calculated. Removes duplicates from network_list and removes weights from any network object.
        Note that by default, ALL nodes that have duplicate connections through alternative edges will have a network with weights that correspond to the number of
        these connections. This will effect some networkx calculations. This method may be called on a Network_3D object to eliminate these weights, assuming only discrete connections are wanted for analysis. 
        """

        self._network_lists = network_analysis.remove_dupes(self._network_lists)

        self._network = network_analysis.open_network(self._network_lists)


    def rescale(self, array, directory = None):
        """
        Scale a downsampled overlay or extracted image object back to the size that is present in either a Network_3D's node or edge properties.
        This will allow a user to create downsampled outputs to speed up certain methods when analyzing Network_3D objects, but then scale them back to the proper size of that corresponding object.
        This will be saved to the active directory if none is specified.
        :param array: (Mandatory; string or ndarray). A path to the .tif file to be rescaled, or an numpy array of the same.
        :param directory: (Optional - Val = None; string). A path to a directory to save the rescaled output. 
        """

        if type(array) == str:
            array_name = os.path.basename(array)

        if directory is not None and type(array) == str:
            filename = f'{directory}/rescaled.tif'
        elif directory is None and type(array) == str:
            filename = f'rescaled.tif'
        elif directory is not None and type(array) != str:
            filename = f"{directory}/rescaled_array.tif"
        elif directory is None and type(array) != str:
            filename = "rescaled_array.tif"

        if type(array) == str:
            array = tifffile.imread(array)

        targ_shape = self._nodes.shape

        factor = round(targ_shape[0]/array.shape[0])

        array = upsample_with_padding(array, factor, targ_shape)

        tifffile.imsave(filename, array)
        print(f"Rescaled array saved to {filename}")

    def edge_to_node(self):
        """
        Converts all edge objects to node objects. Oftentimes, one may wonder how nodes are connected by edges in a network. Converting nodes to edges permits this visualization.
        Essentially a nodepair A-B will be reassigned as A-EdgeC and B-EdgeC.
        Alters the network and network_lists properties to absorb all edges. Edge IDs are altered to not overlap preexisting node IDs. Alters the edges property so that labels correspond
        to new edge IDs. Alters (or sets, if none exists) the node_identities property to keep track of which new nodes are 'edges'. Alters node_centroids property to now contain edge_centroids.
        """

        print("Converting all edge objects to nodes...")

        if self._nodes is not None:
            max_node = np.max(self._nodes)
        else:
            max_node = None

        df, identity_dict, max_node = network_analysis.edge_to_node(self._network_lists, self._node_identities, maxnode = max_node)

        self._network_lists = network_analysis.read_excel_to_lists(df)
        self._network, net_weights = network_analysis.weighted_network(df)
        self._node_identities = identity_dict

        print("Reassigning edge centroids to node centroids (requires both edge_centroids and node_centroids attributes to be present)")

        try:

            new_centroids = {}
            for item in self._edge_centroids:
                new_centroids[item + max_node] = self._edge_centroids[item]
            self._edge_centroids = new_centroids
            self._node_centroids = self._edge_centroids | self._node_centroids

        except Exception as e:
            print("Could not update edge/node centroids. They were likely not precomputed as object attributes. This may cause errors when drawing elements from the merged edge/node array...")

        print("Relabelling self.edge array...")

        num_edge = np.max(self._edges)

        edge_bools = self._edges > 0

        self._edges = self._edges.astype(np.uint32)

        self._edges = self._edges + max_node

        self._edges = self._edges * edge_bools

        if num_edge < 256:
            self._edges = self._edges.astype(np.uint8)
        elif num_edge < 65536:
            self._edges = self._edges.astype(np.uint16)

        node_bools = self._nodes == 0

        self._nodes = self._nodes.astype(np.uint32)
        self._edges = self._edges * node_bools
        self._nodes = self._nodes + self._edges
        num_node = np.max(self._nodes)

        if num_node < 256:
            self._nodes = self._nodes.astype(np.uint8)
        elif num_node < 65536:
            self._nodes = self._nodes.astype(np.uint16)


    def trunk_to_node(self):
        """
        Converts the edge 'trunk' into a node. In this case, the trunk is the edge that creates the most node-node connections. There may be times when many nodes are connected by a single, expansive edge that obfuscates the rest of the edges. Converting the trunk to a node can better reveal these edges.
        Essentially a nodepair A-B that is connected via the trunk will be reassigned as A-Trunk and B-Trunk.
        Alters the network and network_lists properties to absorb the Trunk. Alters (or sets, if none exists) the node_identities property to keep track of which new nodes is a 'Trunk'.
        """

        nodesa = self._network_lists[0]
        nodesb = self._network_lists[1]
        edgesc = self._network_lists[2]
        nodea = []
        nodeb = []
        edgec = []

        trunk = stats.mode(edgesc)
        addtrunk = max(set(nodesa + nodesb)) + 1

        for i in range(len(nodesa)):
            if edgesc[i] == trunk:
                nodea.append(nodesa[i])
                nodeb.append(addtrunk)
                nodea.append(nodesb[i])
                nodeb.append(addtrunk)
                edgec.append(0)
                edgec.append(0)
            else:
                nodea.append(nodesa[i])
                nodeb.append(nodesb[i])
                edgec.append(edgesc[i])

        self.network_lists = [nodea, nodeb, edgec]

        self._node_centroids[addtrunk] = self._edge_centroids[trunk]

        if self._node_identities is None:
            self._node_identities = {}
            nodes = list(set(nodea + nodeb))
            for item in nodes:
                if item == addtrunk:
                    self._node_identities[item] = "Trunk"
                else:
                    self._node_identities[item] = "Node"
        else:
            self._node_identities[addtrunk] = "Trunk"

        if self._edges is not None and self._nodes is not None:

            node_bools = self._nodes == 0

            trunk = self._edges == trunk

            trunk = trunk * addtrunk

            trunk = trunk * node_bools

            self._nodes = self._nodes + trunk





    def prune_samenode_connections(self):
        """
        If working with a network that has multiple node identities (from merging nodes or otherwise manipulating this property),
        this method will remove from the network and network_lists properties any connections that exist between the same node identity,
        in case we want to investigate only connections between differing objects.
        """

        self._network_lists, self._node_identities = network_analysis.prune_samenode_connections(self._network_lists, self._node_identities)
        self._network, num_weights = network_analysis.weighted_network(self._network_lists)


    def isolate_internode_connections(self, ID1, ID2):
        """
        If working with a network that has at least three node identities (from merging nodes or otherwise manipulating this property),
        this method will isolate only connections between two types of nodes, as specified by the user,
        in case we want to investigate only connections between two specific node types.
        :param ID1: (Mandatory, string). The name of the first desired nodetype, as contained in the node_identities property.
        :param ID2: (Mandatory, string). The name of the second desired nodetype, as contained in the node_identities property.
        """

        self._network_lists, self._node_identities = network_analysis.isolate_internode_connections(self._network_lists, self._node_identities, ID1, ID2)
        self._network, num_weights = network_analysis.weighted_network(self._network_lists)

    def downsample(self, down_factor):
        """
        Downsamples the Network_3D object (and all its properties) by some specified factor, to make certain associated methods faster. Centroid IDs and voxel scalings are adjusted accordingly.
        :param down_factor: (Mandatory, int). The factor by which to downsample the Network_3D object.
        """
        try:
            original_shape = self._nodes.shape
        except:
            try:
                original_shape = self._edges.shape
            except:
                print("No node or edge attributes have been set.")

        try:
            self._nodes = downsample(self._nodes, down_factor)
            new_shape = self._nodes.shape
            print("Nodes downsampled...")
        except:
            print("Could not downsample nodes")
        try:
            self._edges = downsample(self._edges, down_factor)
            new_shape = self._edges.shape
            print("Edges downsampled...")
        except:
            print("Could not downsample edges")
        try:
            self._search_region = downsample(self._search_region, down_factor)
            print("Search region downsampled...")
        except:
            print("Could not downsample search region")
        try:
            centroids = self._node_centroids.copy()
            for item in self._node_centroids:
                centroids[item] = np.round((self._node_centroids[item])/down_factor)
            self._node_centroids = centroids
            print("Node centroids downsampled")
        except:
            print("Could not downsample node centroids")
        try:
            centroids = self._edge_centroids.copy()
            for item in self._edge_centroids:
                centroids[item] = np.round((self._edge_centroids[item])/down_factor)
            self._edge_centroids = centroids
            print("Edge centroids downsampled...")
        except:
            print("Could not downsample edge centroids")

        try:
            change = float(original_shape[1]/new_shape[1])
            self._xy_scale = self._xy_scale * change
            self._z_scale = self._z_scale * change
            print(f"Arrays of size {original_shape} resized to {new_shape}. Voxel scaling has been adjusted accordingly")
        except:
            print("Could not update voxel scaling")

    def upsample(self, up_factor, targ_shape):
        """
        Upsamples the Network_3D object (and all its properties) by some specified factor, usually to undo a downsample. Centroid IDs and voxel scalings are adjusted accordingly.
        Note that the upsample also asks for a target shape in the form of a tuple (Z, Y, X) (which can be obtained from numpy arrays as some_array.shape). 
        This is because simply upsampling by a factor that mirrors a downsample will not result in the exact same shape, so the target shape is also requested. Note that this method
        should only be called to undo downsamples by an equivalent factor, while inputting the original shape prior to downsampling in the targ_shape param. This method is not a general purpose rescale method
        and will give some unusual results if the up_factor does not result in an upsample whose shape is not already close to the targ_shape.
        :param up_factor: (Mandatory, int). The factor by which to upsample the Network_3D object.
        :targ_shape: (Mandatory, tuple). A (Z, Y, X) tuple of the target shape that should already be close to the shape of the upsampled array. 
        """

        try:
            original_shape = self._nodes.shape
        except:
            try:
                original_shape = self._edges.shape
            except:
                print("No node or edge attributes have been set.")

        try:
            self._nodes = upsample_with_padding(self._nodes, up_factor, targ_shape)
            print("Nodes upsampled...")
        except:
            print("Could not upsample nodes")
        try:
            self._edges = upsample_with_padding(self._edges, up_factor, targ_shape)
            print("Edges upsampled...")
        except:
            print("Could not upsample edges")
        try:
            centroids = self._node_centroids.copy()
            for item in self._node_centroids:
                centroids[item] = (self._node_centroids[item]) * up_factor
            self._node_centroids = centroids
            print("Node centroids upsampled")
        except:
            print("Could not upsample node centroids")
        try:
            centroids = self._edge_centroids.copy()
            for item in self._edge_centroids:
                centroids[item] = (self._edge_centroids[item]) * up_factor
            self._edge_centroids = centroids
            print("Edge centroids upsampled...")
        except:
            print("Could not upsample edge centroids")

        try:
            change = float(original_shape[1]/targ_shape[1])
            self._xy_scale = self._xy_scale * change
            self._z_scale = self._z_scale * change
            print(f"Arrays of size {original_shape} resized to {targ_shape}. Voxel scaling has been adjusted accordingly")
        except:
            print("Could not update voxel scaling")

    def remove_trunk_post(self):
        """
        Removes the 'edge' trunk from a network. In this case, the trunk is the edge that creates the most node-node connections. There may be times when many nodes are connected by a single, expansive edge that obfuscates the rest of the edges. Removing the trunk to a node can better reveal these edges.
        Alters the network and network_lists properties to remove the Trunk.
        """

        nodesa = self._network_lists[0]
        nodesb = self._network_lists[1]
        edgesc = self._network_lists[2]

        trunk = stats.mode(edgesc)

        for i in range(len(edgesc) - 1, -1, -1):
            if edgesc[i] == trunk:
                del edgesc[i]
                del nodesa[i]
                del nodesb[i]

        self._network_lists = [nodesa, nodesb, edgesc]
        self._network, weights = network_analysis.weighted_network(self._network_lists)



    #Methods related to visualizing the network using networkX and matplotlib

    def show_network(self, geometric = False, directory = None):
        """
        Shows the network property as a simplistic graph, and some basic stats. Does not support viewing edge weights.
        :param geoemtric: (Optional - Val = False; boolean). If False, node placement in the graph will be random. If True, nodes
        will be placed in their actual spatial location (from the original node segmentation) along the XY plane, using node_centroids.
        The node size will then represent the nodes Z location, with smaller nodes representing a larger Z value. If False, nodes will be placed randomly.
        :param directory: (Optional – Val = None; string). An optional string path to a directory to save the network plot image to. If not set, nothing will be saved.
        """

        if not geometric:

            simple_network.show_simple_network(self._network_lists, directory = directory)

        else:
            simple_network.show_simple_network(self._network_lists, geometric = True, geo_info = [self._node_centroids, self._nodes.shape], directory = directory)

    def show_communities_flex(self, geometric = False, directory = None, weighted = True, partition = False, style = 0):


        self._communities, self.normalized_weights = modularity.show_communities_flex(self._network, self._network_lists, self.normalized_weights, geo_info = [self._node_centroids, self._nodes.shape], geometric = geometric, directory = directory, weighted = weighted, partition = partition, style = style)


    def show_communities(self, geometric = False, directory = None):
        """
        Shows the network property, and some basic stats, as a graph where nodes are labelled by colors representing the community they belong to as determined by a label propogation algorithm. Does not support viewing edge weights.
        :param geoemtric: (Optional - Val = False; boolean). If False, node placement in the graph will be random. If True, nodes
        will be placed in their actual spatial location (from the original node segmentation) along the XY plane, using node_centroids.
        The node size will then represent the nodes Z location, with smaller nodes representing a larger Z value. If False, nodes will be placed randomly.
        :param directory: (Optional – Val = None; string). An optional string path to a directory to save the network plot image to. If not set, nothing will be saved.
        """

        if not geometric:

            simple_network.show_community_network(self._network_lists, directory = directory)

        else:
            simple_network.show_community_network(self._network_lists, geometric = True, geo_info = [self._node_centroids, self._nodes.shape], directory = directory)


    def show_communities_louvain(self, geometric = False, directory = None):
        """
        Shows the network property as a graph, and some basic stats, where nodes are labelled by colors representing the community they belong to as determined by a louvain algorithm. Supports viewing edge weights.
        :param geoemtric: (Optional - Val = False; boolean). If False, node placement in the graph will be random. If True, nodes
        will be placed in their actual spatial location (from the original node segmentation) along the XY plane, using node_centroids.
        The node size will then represent the nodes Z location, with smaller nodes representing a larger Z value. If False, nodes will be placed randomly.
        """

        if not geometric:

            modularity.louvain_mod(self._network_lists, directory = directory)
        else:
            modularity.louvain_mod(self._network_lists, geometric = True, geo_info = [self._node_centroids, self._nodes.shape], directory = directory)

    def louvain_modularity(self, solo_mod = False):
        """
        Shows some basic stats of the network, including modularity (essentially strength of community structure), using a louvain algorithm that accounts for edge weights.
        :param solo_mod: (Optional - Val = False; boolean). If True, will return a singular modularity for the network, taking into
        account all disconnected components as pieces of a network. If False, will return the modularity of each singular disconnected component of the network with the number of nodes in the component as a key
        and the modularity of the component as a value.
        :returns: A dictionary containing the modularity for each disconnected component in the network, key-indexed by that component's node count, or a single modularity value accounting for all disconnected components of the network if the solo_mod param is True.
        """

        if not solo_mod:
            mod = modularity._louvain_mod(self._network)
        else:
            mod = modularity._louvain_mod_solo(self._network)

        return mod

    def modularity(self, solo_mod = False):
        """
        Shows some basic stats of the network, including modularity (essentially strength of community structure), using a label propogation algorithm that does not consider edge weights.
        :param solo_mod: (Optional - Val = False; boolean). If True, will return a singular modularity for the network, taking into
        account all disconnected components as pieces of a network. If False, will return the modularity of each singular disconnected component of the network with the number of nodes in the component as a key
        and the modularity of the component as a value.
        :returns: A dictionary containing the modularity for each disconnected component in the network, key-indexed by that component's node count, or a single modularity value accounting for all disconnected components of the network if the solo_mod param is True.
        """

        modularity = simple_network.modularity(self._network, solo_mod = solo_mod)

        return modularity


    def show_identity_network(self, geometric = False, directory = None):
        """
        Shows the network property, and some basic stats, as a graph where nodes are labelled by colors representing the identity of the node as detailed in the node_identities property. Does not support viewing edge weights.
        :param geoemtric: (Optional - Val = False; boolean). If False, node placement in the graph will be random. If True, nodes
        will be placed in their actual spatial location (from the original node segmentation) along the XY plane, using node_centroids.
        The node size will then represent the nodes Z location, with smaller nodes representing a larger Z value. If False, nodes will be placed randomly.
        :param directory: (Optional – Val = None; string). An optional string path to a directory to save the network plot image to. If not set, nothing will be saved.
        """
        if not geometric:
            simple_network.show_identity_network(self._network_lists, self._node_identities, geometric = False, directory = directory)
        else:
            simple_network.show_identity_network(self._network_lists, self._node_identities, geometric = True, geo_info = [self._node_centroids, self._nodes.shape], directory = directory)



    #Methods relating to visualizing elements of the network in 3D

    def show_3D(self, other_arrays = None, down_factor = 1):
        """
        Allows the Network_3D object to be visualized in 3D using plotly. By default, this will show the nodes and edges properties. All arrays involved will be made binary. 
        Note that nettracer_3D is not primarily a 3D visualization tool, so the funcionality of this method is limited, and additionally it should really only be run on downsampled data.
        :param other_arrays: (Optional - Val = None; string). A filepath to additional .tif files (or a directory containing only .tif files) to show alongside the Network_3D object, for example a node_indicies or network_lattice overlay. 
        :param down_factor: (Optional - Val = 1; int). A downsampling factor to speed up showing the 3D display and improve processing. Note that ALL arrays being shown will be subject
        to this downsample factor. If you have files to be shown alongside the Network_3D object that were ALREADY downsampled, instead downsample the Network_3D object FIRST and pass nothing to this value.
        If arrays are sized to different shapes while show_3D() is being called, there may be unusual results.
        """
        if down_factor > 1:
            xy_scale = down_factor * self._xy_scale
            z_scale = down_factor * self._z_scale
            try:
                nodes = downsample(self._nodes, down_factor, order = 3)
                nodes = binarize(nodes)
            except:
                pass
            try:
                edges = downsample(self._edges, down_factor, order = 3)
                edges = binarize(edges)
            except:
                edges = None
            try:
                if not isinstance(other_arrays, np.ndarray):
                    other_arrays = tifffile.imread(other_arrays)
                if other_arrays.shape == self._nodes.shape:
                    other_arrays = downsample(other_arrays, down_factor, order = 3)
                    other_arrays = binarize(other_arrays)
                other_arrays = [edges, other_arrays]
            except:
                try:
                    arrays = directory_info(other_arrays)
                    directory = other_arrays
                    other_arrays = []
                    for array in arrays:
                        array = tifffile.imread(f'{directory}/{array}')
                        if array.shape == self._nodes.shape:
                            array = downsample(array, down_factor, order = 3)
                            array = binarize(array)
                        other_arrays.append(array)
                    other_arrays.insert(0, edges)
                except:
                    other_arrays = edges
            visualize_3D(nodes, other_arrays, xy_scale = xy_scale, z_scale = z_scale)
        else:
            try: 
                nodes = binarize(self._nodes)
            except:
                pass
            try:
                edges = binarize(self._edges)
            except:
                edges = None
            try:
                if not isinstance(other_arrays, np.ndarray):
                    other_arrays = tifffile.imread(other_arrays)
                other_arrays = binarize(other_arrays)
                other_arrays = [edges, other_arrays]
            except:
                try:
                    arrays = directory_info(other_arrays)
                    directory = other_arrays
                    other_arrays = []
                    for array in arrays:
                        array = tifffile.imread(f'{directory}/{array}')
                        array = binarize(array)
                        other_arrays.append(array)
                    other_arrays.insert(0, self._edges)
                except:
                    other_arrays = edges

            visualize_3D(nodes, other_arrays, xy_scale = self._xy_scale, z_scale = self._z_scale)

    def get_degrees(self, down_factor = 1, directory = None, called = False, no_img = 0):
        """
        Method to obtain information on the degrees of nodes in the network, also generating overlays that relate this information to the 3D structure.
        Overlays include a grayscale image where nodes are assigned a grayscale value corresponding to their degree, and a numerical index where numbers are drawn at nodes corresponding to their degree.
        These will be saved to the active directory if none is specified. Note calculations will be done with node_centroids unless a down_factor is passed. Note that a down_factor must be passed if there are no node_centroids.
        :param down_factor: (Optional - Val = 1; int). A factor to downsample nodes by while calculating centroids, assuming no node_centroids property was set.
        :param directory: (Optional - Val = None; string). A path to a directory to save outputs.
        :returns: A dictionary of degree values for each node.
        """

        if down_factor > 1:
            centroids = self._node_centroids.copy()
            for item in self._node_centroids:
                centroids[item] = np.round((self._node_centroids[item]) / down_factor)
            nodes = downsample(self._nodes, down_factor)
            degrees, nodes = network_analysis.get_degrees(nodes, self._network, directory = directory, centroids = centroids, called = called, no_img = no_img)

        else:
            degrees, nodes = network_analysis.get_degrees(self._nodes, self._network, directory = directory, centroids = self._node_centroids, called = called, no_img = no_img)

        return degrees, nodes

    def get_hubs(self, proportion = None, down_factor = 1, directory = None):
        """
        Method to isolate hub regions of a network (Removing all nodes below some proportion of highest degrees), also generating overlays that relate this information to the 3D structure.
        Overlays include a grayscale image where nodes are assigned a grayscale value corresponding to their degree, and a numerical index where numbers are drawn at nodes corresponding to their degree.
        These will be saved to the active directory if none is specified. Note calculations will be done with node_centroids unless a down_factor is passed. Note that a down_factor must be passed if there are no node_centroids.
        :param proportion: (Optional - Val = None; Float). A float of 0 to 1 that details what proportion of highest node degrees to include in the output. Note that this value will be set to 0.1 by default.
        :param down_factor: (Optional - Val = 1; int). A factor to downsample nodes by while calculating centroids, assuming no node_centroids property was set.
        :param directory: (Optional - Val = None; string). A path to a directory to save outputs.
        :returns: A dictionary of degree values for each node above the desired proportion of highest degree nodes.
        """
        if down_factor > 1:
            centroids = self._node_centroids.copy()
            for item in self._node_centroids:
                centroids[item] = np.round((self._node_centroids[item]) / down_factor)
            nodes = downsample(self._nodes, down_factor)
            hubs = hub_getter.get_hubs(nodes, self._network, proportion, directory = directory, centroids = centroids)

        else:
            hubs = hub_getter.get_hubs(self._nodes, self._network, proportion, directory = directory, centroids = self._node_centroids)

        return hubs 


    def isolate_connected_component(self, key = None, directory = None, full_edges = None, gen_images = True):
        """
        Method to isolate a connected component of a network. This can include isolating both nodes and edge images, primarily for visualization, but will also islate a .xlsx file
        to be used to analyze a connected component of a network in detail, as well as returning that networkx graph object. This method generates a number of images. By default,
        the isolated component will be presumed to be the largest one, however a key may be passed containing some node ID of any component needing to be isolated.
        :param key: (Optional - Val None; int). A node ID that is contained in the desired connected component to be isolated. If unset, the largest component will be isolated by default.
        :param directory: (Optional - Val = None; string). A path to a directory to save outputs.
        :param full_edges: (Optional - Val = False; string). If None, will not calculate 'full edges' of the connected component. Essentially, edges stored in the edges property will resemble
        how this file has been altered for connectivity calculations, but will not resemble true edges as they appeared in their original masked segmentation. To obtain edges, isolated over
        a connected component, as they appear in their segmentation, set this as a string file path to your original binary edges segmentation .tif file. Note that this requires the search_region property to be set.
        :param gen_images: (Optional - Val = True; boolean). If True, the various isolated images will be generated. However, as this costs time and memory, setting this value to False
        will cause this method to only generate the .xlsx file of the connected component and to only return the graph object, presuming the user is only interested in non-visual analytics here.
        :returns: IF NO EDGES ATTRIBUTE (will return isolated_nodes, isolated_network in that order. These components can be used to directly set a new Network_3D object
        without using load functions by setting multiple params at once, ie my_network.nodes, my_network.network = old_network.isolate_connected_component()). IF EDGES ATTRIBUTE (will
        return isolated nodes, isolated edges, and isolated network in that order). IF gen_images == False (Will return just the network).
        """

        if gen_images:

            if not hasattr(self, '_edges') or self._edges is None:

                connected_component, isonodes, _ = community_extractor.isolate_connected_component(self._nodes, self._network, key=key, directory = directory)

                nodea = []
                nodeb = []
                edgec = []
                nodesa = self._network_lists[0]
                nodesb = self._network_lists[1]
                edgesc = self._network_lists[2]
                for i in range(len(nodesa)):
                    if (nodesa[i], nodesb[i]) in connected_component:
                        nodea.append(nodesa[i])
                        nodeb.append(nodesb[i])
                        edgec.append(edgesc[i])
                network_lists = [nodea, nodeb, edgec]
                network, weights = network_analysis.weighted_network(network_lists)

                return isonodes, network

            else:
                if full_edges is not None:
                    connected_component, isonodes, isoedges, searchers = community_extractor.isolate_connected_component(self._nodes, self._network, key=key, edge_file = self._edges, search_region = self.search_region, netlists = self._network_lists, directory = directory)

                else:
                    connected_component, isonodes, isoedges, searchers = community_extractor.isolate_connected_component(self._nodes, self._network, key=key, edge_file = self._edges, netlists = self._network_lists, directory = directory)

                df = create_and_save_dataframe(connected_component)
                network_lists = network_analysis.read_excel_to_lists(df)
                network, net_weights = network_analysis.weighted_network(df)

                if full_edges is not None:
                    full_edges = tifffile.imread(full_edges)
                    community_extractor.isolate_full_edges(searchers, full_edges, directory = directory)

                return isonodes, isoedges, network

        else:
            G = community_extractor._isolate_connected(self._network, key = key)
            return G


    def isolate_mothers(self, directory = None, down_factor = 1, louvain = True, ret_nodes = False, called = False):

        """
        Method to isolate 'mother' nodes of a network (in this case, this means nodes that exist betwixt communities), also generating overlays that relate this information to the 3D structure.
        Overlays include a grayscale image where mother nodes are assigned a grayscale value corresponding to their degree, and a numerical index where numbers are drawn at mother nodes corresponding to their degree, and a general grayscale mask with mother nodes having grayscale IDs corresponding to those stored in the nodes property.
        These will be saved to the active directory if none is specified. Note calculations must be done with node_centroids.
        :param down_factor: (Optional - Val = 1; int). A factor to downsample nodes by while drawing overlays. Note this option REQUIRES node_centroids to already be set.
        :param directory: (Optional - Val = None; string). A path to a directory to save outputs.
        :param louvain: (Optional - Val = True; boolean). If True, louvain community detection will be used. Otherwise, label propogation will be used.
        :param ret_nodes: (Optional - Val = False; boolean). If True, will return the network graph object of the 'mothers'.
        :returns: A dictionary of mother nodes and their degree values.
        """

        if ret_nodes:
            mothers = community_extractor.extract_mothers(None, self._network, louvain = louvain, ret_nodes = True, called = called)
            return mothers
        else:

            if down_factor > 1:
                centroids = self._node_centroids.copy()
                for item in self._node_centroids:
                    centroids[item] = np.round((self._node_centroids[item]) / down_factor)
                nodes = downsample(self._nodes, down_factor)
                mothers, overlay = community_extractor.extract_mothers(nodes, self._network, directory = directory, centroid_dic = centroids, louvain = louvain, called = called)
            else:
                mothers, overlay = community_extractor.extract_mothers(self._nodes, self._network, centroid_dic = self._node_centroids, directory = directory, louvain = louvain, called = called)
            return mothers, overlay


    def isolate_hubs(self, proportion = 0.1, retimg = True):

        hubs = community_extractor.find_hub_nodes(self._network, proportion)

        if retimg:

            hub_img = np.isin(self._nodes, hubs) * self._nodes
        else:
            hub_iimg = None

        return hubs, hub_img


    def extract_communities(self, color_code = True, down_factor = None, identities = False):

        if down_factor is not None:
            original_shape = self._nodes.shape
            temp = downsample(self._nodes, down_factor)
            if color_code:
                if not identities:
                    image, output = community_extractor.assign_community_colors(self.communities, temp)
                else:
                    image, output = community_extractor.assign_community_colors(self.node_identities, temp)
            else:
                if not identities:
                    image, output = community_extractor.assign_community_grays(self.communities, temp)
                else:
                    image, output = community_extractor.assign_community_grays(self.node_identities, temp)
            image = upsample_with_padding(image, down_factor, original_shape)
        else:

            if color_code:
                if not identities:
                    image, output = community_extractor.assign_community_colors(self.communities, self._nodes)
                else:
                    image, output = community_extractor.assign_community_colors(self.node_identities, self._nodes)
            else:
                if not identities:
                    image, output = community_extractor.assign_community_grays(self.communities, self._nodes)
                else:
                    image, output = community_extractor.assign_community_grays(self.node_identities, self._nodes)


        return image, output
        




    def extract_communities_louvain(self, directory = None, down_factor = 1, color_code = True):
        """
        Method to generate overlays that relate community detection in a network to the 3D structure.
        Overlays include a grayscale image where nodes are assigned a grayscale value corresponding to their community, a numerical index where numbers are drawn at nodes corresponding to their community, and a
        color coded overlay where a nodes color corresponds to its community. Community detection will be done with louvain algorithm.
        These will be saved to the active directory if none is specified.
        :param directory: (Optional - Val = None; string). A path to a directory to save outputs.
        :param down_factor: (Optional - Val = 1; int). A factor to downsample nodes by while drawing overlays. Note this option REQUIRES node_centroids to already be set.
        :param color code: (Optional - Val = True; boolean). If set to False, the color-coded overlay will not be drawn.
        :returns: A dictionary where nodes are grouped by community.
        """

        if down_factor > 1:
            centroids = self._node_centroids.copy()
            for item in self._node_centroids:
                centroids[item] = np.round((self._node_centroids[item]) / down_factor)
            nodes = downsample(self._nodes, down_factor)
            partition = network_analysis.community_partition(nodes, self._network_lists, directory = directory, centroids = centroids, color_code = color_code)

        else:
            partition = network_analysis.community_partition(self._nodes, self._network_lists, directory = directory, centroids = self._node_centroids, color_code = color_code)

        return partition


    #Methods related to analysis:

    def radial_distribution(self, radial_distance, directory = None):
        """
        Method to calculate the radial distribution of all nodes in the network. Essentially, this is a distribution of the distances between
        all connected nodes in the network, grouped into histogram buckets, which can be used to evaluate the general distances of node-node connectivity. Also displays a histogram.
        This method will save a .xlsx file of this distribution (not bucketed but instead with all vals) to the active directory if none is specified.
        :param radial_distance: (Mandatory, int). The bucket size to group nodes into for the histogram. Note this value will correspond 1-1 with voxels in the nodes array if xy_scale/z_scale have not been set, otherwise they
        will correspond with whatever true value the voxels represent (ie microns).
        :param directory: (Optional - Val = None; string): A path to a directory to save outputs.
        :returns: A list of all the distances between connected nodes in the network.
        """

        radial_dist = network_analysis.radial_analysis(self._nodes, self._network_lists, radial_distance, self._xy_scale, self._z_scale, self._node_centroids, directory = directory)

        return radial_dist

    def assign_random(self, weighted = True):

        """
        Generates a random network of equivalent edge and node count to the current Network_3D object. This may be useful, for example, in comparing aspects of the Network_3D object
        to a similar random network, to demonstrate whether the Network_3D object is a result that itself can be considered random. For example, we can find the modularity of the
        random network and compare it to the Network_3D object's modularity. Note that the random result will itself not have a consistent modularity score between instances this
        method is called, due to randomness, in which case iterating over a large number, say 100, of these random networks will give a tighter comparison point. Please note that
        since Network_3D objects are weighted for multiple connections by default, the random network will consider each additional weight as an additional edge. So a network that has
        one edge of weight one and one of weight two will cause the random network to incorperate 3 edges (that may be crunched into one weighted edge themselves). Please call remove_edge_weights()
        on the Network_3D() object prior to generating the random network if this behavior is not desired.
        :param weighted: (Optional - Val = True; boolean). By default (when True), the random network will be able to take on edge weights by assigning additional edge
        connections between the same nodes. When False, all edges will be made to be discrete. Note that if you for some reason have a supremely weighted network and want to deweight
        the random network, there is a scenario where no new connections can be found and this method will become caught in a while loop.
        :returns: an equivalent random networkx graph object
        """

        G, df = network_analysis.generate_random(self._network, self._network_lists, weighted = weighted)

        return G, df

    def degree_distribution(self, directory = None):
        """
        Method to calculate the degree distribution of all nodes in the network. Essentially, this is recomputes the distribution of degrees to show an x axis of degrees in the network,
        and a y axis of the proportion of nodes in the network that have that degree. A .xlsx file containing the degree distribution will be saved to the active directory if none is specified. 
        This method also shows a scatterplot of this result and attempts to model a power-curve over it, however I found the excel power-curve modeler to be superior so that one may be more reliable than the one included here.
        :param directory: (Optional - Val = None; string): A path to a directory to save outputs.
        :returns: A dictionary with degrees as keys and the proportion of nodes with that degree as a value.
        """

        degrees = network_analysis.degree_distribution(self._network, directory = directory)

        return degrees

    def get_network_stats(self):
        """
        Calculate comprehensive network statistics from a NetworkX graph object.
        
        Parameters:
        G (networkx.Graph): Input graph
        
        Returns:
        dict: Dictionary containing various network statistics
        """
        G = self._network
        stats = {}
        
        # Basic graph properties
        stats['num_nodes'] = G.number_of_nodes()
        stats['num_edges'] = G.number_of_edges()
        stats['density'] = nx.density(G)
        stats['is_directed'] = G.is_directed()
        stats['is_connected'] = nx.is_connected(G) if not G.is_directed() else nx.is_strongly_connected(G)

        # Component analysis
        if not G.is_directed():
            stats['num_connected_components'] = nx.number_connected_components(G)
            largest_cc = max(nx.connected_components(G), key=len)
            stats['largest_component_size'] = len(largest_cc)
        else:
            stats['num_strongly_connected_components'] = nx.number_strongly_connected_components(G)
            largest_scc = max(nx.strongly_connected_components(G), key=len)
            stats['largest_strongly_connected_component_size'] = len(largest_scc)
        
        # Degree statistics
        degrees = [d for _, d in G.degree()]
        stats['avg_degree'] = sum(degrees) / len(degrees)
        stats['max_degree'] = max(degrees)
        stats['min_degree'] = min(degrees)
        
        # Centrality measures
        # Note: These can be computationally expensive for large graphs
        try:
            stats['avg_betweenness_centrality'] = np.mean(list(nx.betweenness_centrality(G).values()))
            stats['avg_closeness_centrality'] = np.mean(list(nx.closeness_centrality(G).values()))
            stats['avg_eigenvector_centrality'] = np.mean(list(nx.eigenvector_centrality(G, max_iter=1000).values()))
        except:
            stats['centrality_measures'] = "Failed to compute - graph might be too large or disconnected"
        
        # Clustering and transitivity
        stats['avg_clustering_coefficient'] = nx.average_clustering(G)
        stats['transitivity'] = nx.transitivity(G)
        
        # Path lengths
        if nx.is_connected(G):
            stats['diameter'] = nx.diameter(G)
            stats['avg_shortest_path_length'] = nx.average_shortest_path_length(G)
        else:
            stats['diameter'] = "Undefined - Graph is not connected"
            stats['avg_shortest_path_length'] = "Undefined - Graph is not connected"
        
        # Structural properties
        stats['is_tree'] = nx.is_tree(G)
        stats['num_triangles'] = sum(nx.triangles(G).values()) // 3
        
        # Assortativity
        try:
            stats['degree_assortativity'] = nx.degree_assortativity_coefficient(G)
        except:
            stats['degree_assortativity'] = "Failed to compute"

        try:
            nodes = np.unique(self._nodes)
            if nodes[0] == 0:
                nodes = np.delete(nodes, 0)
            stats['Unconnected nodes (left out from node image)'] = (len(nodes) - len(G.nodes()))
        except:
            stats['Unconnected nodes (left out from node image)'] = "Failed to compute"

        
        return stats


    def neighborhood_identities(self, root, directory = None, mode = 0, search = 0):



        targets = []
        total_dict = {}
        neighborhood_dict = {}
        proportion_dict = {}
        G = self._network
        node_identities = self._node_identities
        for val in set(node_identities.values()):
            total_dict[val] = 0
            neighborhood_dict[val] = 0

        for node in node_identities:
            nodeid = node_identities[node]
            total_dict[nodeid] += 1
            if nodeid == root:
                targets.append(node)


        if mode == 0: #search neighbor ids within the network


            for node in G.nodes():
                nodeid = node_identities[node]
                neighbors = list(G.neighbors(node))
                for subnode in neighbors:
                    subnodeid = node_identities[subnode]
                    if subnodeid == root:
                        neighborhood_dict[nodeid] += 1
                        break

            title1 = f'Neighborhood Distribution of Nodes in Network from Nodes: {root}'
            title2 = f'Neighborhood Distribution of Nodes in Network from Nodes {root} as a proportion of total nodes of that ID'


        elif mode == 1: #Search neighborhoods morphologically, obtain densities
            neighborhood_dict, total_dict, densities = morphology.search_neighbor_ids(self._nodes, targets, node_identities, neighborhood_dict, total_dict, search, self._xy_scale, self._z_scale, root)
            title1 = f'Volumetric Neighborhood Distribution of Nodes in image that are {search} from nodes: {root}'
            title2 = f'Density Distribution of Nodes in image that are {search} from Nodes {root} as a proportion of total node volume of that ID'


        for identity in neighborhood_dict:
            proportion_dict[identity] = neighborhood_dict[identity]/total_dict[identity]

        network_analysis.create_bar_graph(neighborhood_dict, title1, "Node Identity", "Amount", directory=directory)

        network_analysis.create_bar_graph(proportion_dict, title2, "Node Identity", "Proportion", directory=directory)

        try:
            network_analysis.create_bar_graph(densities, f'Clustering Factor of Node Identities with {search} from nodes {root}', "Node Identity", "Density Search/Density Total", directory=directory)
        except:
            densities = None


        return neighborhood_dict, proportion_dict, title1, title2, densities



#Morphological stats or network linking:

    def volumes(self, sort = 'nodes'):

        """Calculates the volumes of either the nodes or edges"""

        if sort == 'nodes':

            return morphology.calculate_voxel_volumes(self._nodes, self._xy_scale, self._z_scale)

        elif sort == 'edges':

            return morphology.calculate_voxel_volumes(self._edges, self._xy_scale, self._z_scale)

        elif sort == 'network_overlay':

            return morphology.calculate_voxel_volumes(self._network_overlay, self._xy_scale, self._z_scale)

        elif sort == 'id_overlay':

            return morphology.calculate_voxel_volumes(self._id_overlay, self._xy_scale, self._z_scale)




    def interactions(self, search = 0, cores = 0, resize = None, save = False, skele = False):

        return morphology.quantify_edge_node(self._nodes, self._edges, search = search, xy_scale = self._xy_scale, z_scale = self._z_scale, cores = cores, resize = resize, save = save, skele = skele)



    def morph_proximity(self, search = 0, targets = None):

        search_x, search_z = dilation_length_to_pixels(self._xy_scale, self._z_scale, search, search)

        num_nodes = np.max(self._nodes)

        my_dict = proximity.create_node_dictionary(self._nodes, num_nodes, search_x, search_z, targets = targets)

        my_dict = proximity.find_shared_value_pairs(my_dict)

        my_dict = create_and_save_dataframe(my_dict)

        self._network_lists = network_analysis.read_excel_to_lists(my_dict)

        self.remove_edge_weights()

    def centroid_array(self):
        """Use the centroids to populate a node array"""

        array = proximity.populate_array(self.node_centroids)

        return array


    def kd_network(self, distance = 100, targets = None):

        array = self.centroid_array()

        neighbors = proximity.find_neighbors_kdtree(array, distance, targets = targets)

        network = create_and_save_dataframe(neighbors)

        self._network_lists = network_analysis.read_excel_to_lists(network)

        self.remove_edge_weights()

        return array




if __name__ == "__main__":
    create_and_draw_network()