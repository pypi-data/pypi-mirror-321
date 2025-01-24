import numpy as np
from . import nettracer
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed
from scipy.spatial import KDTree
import concurrent.futures
import multiprocessing as mp
import pandas as pd
from typing import Dict, Union, Tuple, List, Optional


# Related to morphological border searching:

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



def _get_node_node_dict(label_array, label, dilate_xy, dilate_z):
    """Internal method used for the secondary algorithm to find which nodes interact 
    with which other nodes based on proximity."""
    
    # Create a boolean mask where elements with the specified label are True
    binary_array = label_array == label
    binary_array = nettracer.dilate_3D_recursive(binary_array, dilate_xy, dilate_xy, dilate_z) #Dilate the label to see where the dilated label overlaps
    label_array = label_array * binary_array  # Filter the labels by the node in question
    label_array = label_array.flatten()  # Convert 3d array to 1d array
    label_array = nettracer.remove_zeros(label_array)  # Remove zeros
    label_array = label_array[label_array != label]
    label_array = set(label_array)  # Remove duplicates
    label_array = list(label_array)  # Back to list
    return label_array

def process_label(args):
    """Internal method used for the secondary algorithm to process a particular node."""
    nodes, label, dilate_xy, dilate_z, array_shape = args
    print(f"Processing node {label}")
    indices = np.argwhere(nodes == label)
    z_vals, y_vals, x_vals = get_reslice_indices((indices, dilate_xy, dilate_z, array_shape))
    if z_vals is None: #If get_reslice_indices ran into a ValueError, nothing is returned.
        return None, None, None
    sub_nodes = reslice_3d_array((nodes, z_vals, y_vals, x_vals))
    return label, sub_nodes


def create_node_dictionary(nodes, num_nodes, dilate_xy, dilate_z, targets = None):
    """Internal method used for the secondary algorithm to process nodes in parallel."""
    # Initialize the dictionary to be returned
    node_dict = {}

    array_shape = nodes.shape


    # Use ThreadPoolExecutor for parallel execution
    with ThreadPoolExecutor(max_workers=mp.cpu_count()) as executor:
        # First parallel section to process labels
        # List of arguments for each parallel task
        args_list = [(nodes, i, dilate_xy, dilate_z, array_shape) for i in range(1, num_nodes + 1)]

        if targets is not None:
            args_list = [tup for tup in args_list if tup[1] in targets]

        results = executor.map(process_label, args_list)


        # Second parallel section to create dictionary entries
        for label, sub_nodes in results:
            executor.submit(create_dict_entry, node_dict, label, sub_nodes, dilate_xy, dilate_z)

    return node_dict

def create_dict_entry(node_dict, label, sub_nodes, dilate_xy, dilate_z):
    """Internal method used for the secondary algorithm to pass around args in parallel."""

    if label is None:
        pass
    else:
        node_dict[label] = _get_node_node_dict(sub_nodes, label, dilate_xy, dilate_z)

def find_shared_value_pairs(input_dict):
    """Internal method used for the secondary algorithm to look through discrete 
    node-node connections in the various node dictionaries"""
    # List comprehension approach
    return [[key, value, 0] for key, values in input_dict.items() for value in values]



#Related to kdtree centroid searching:

def populate_array(centroids):
    """
    Create a 3D array from centroid coordinates.
    
    Args:
        centroids: Dictionary where keys are object IDs and values are [z,y,x] coordinates
    
    Returns:
        3D numpy array where values are object IDs at their centroid locations
    """
    # Input validation
    if not centroids:
        raise ValueError("Centroids dictionary is empty")
    
    # Convert to numpy array and get bounds
    coords = np.array(list(centroids.values()))
    # Round coordinates to nearest integer
    coords = np.round(coords).astype(int)
    min_coords = coords.min(axis=0)
    max_coords = coords.max(axis=0)
    
    # Check for negative coordinates
    if np.any(min_coords < 0):
        raise ValueError("Negative coordinates found in centroids")
    
    # Create array
    array = np.zeros((max_coords[0] + 1, 
                     max_coords[1] + 1, 
                     max_coords[2] + 1), dtype=int)
    
    # Populate array with rounded coordinates
    for obj_id, coord in centroids.items():
        z, y, x = np.round([coord[0], coord[1], coord[2]]).astype(int)
        array[z, y, x] = obj_id
        
    return array

def find_neighbors_kdtree(array, radius, targets=None):
    # Get coordinates of nonzero points
    points = np.transpose(np.nonzero(array))
    
    # Create KD-tree from all nonzero points
    tree = KDTree(points)
    
    if targets is None:
        # Original behavior: find neighbors for all points
        query_points = points
        query_indices = range(len(points))  # Add this line
    else:
        # Find coordinates of target values
        target_points = []
        target_indices = []  # Add this line
        for idx, point in enumerate(points):
            if array[tuple(point)] in targets:
                target_points.append(point)
                target_indices.append(idx)  # Add this line
        
        # Convert to numpy array for querying
        query_points = np.array(target_points)
        query_indices = target_indices  # Add this line
        
        # Handle case where no target values were found
        if len(query_points) == 0:
            return []
    
    # Query for all points within radius of each query point
    neighbor_indices = tree.query_ball_point(query_points, radius)
    
    # Initialize output list
    output = []
    
    # Generate pairs
    for i, neighbors in enumerate(neighbor_indices):
        query_idx = query_indices[i]  # Modified this line
        for neighbor_idx in neighbors:
            # Skip self-pairing
            if neighbor_idx != query_idx:
                query_value = array[tuple(points[query_idx])]
                neighbor_value = array[tuple(points[neighbor_idx])]
                output.append([query_value, neighbor_value, 0])
    
    return output


def extract_pairwise_connections(connections):
    output = []

    for i, sublist in enumerate(connections):
        list_index_value = i + 1  # Element corresponding to the sublist's index
        for number in sublist:
            if number != list_index_value:  # Exclude self-pairing
                output.append([list_index_value, number, 0])
                print(f'sublist: {sublist}, adding: {[list_index_value, number, 0]}')

    return output



#voronois:
def create_voronoi_3d_kdtree(centroids: Dict[Union[int, str], Union[Tuple[int, int, int], List[int]]], 
                            shape: Optional[Tuple[int, int, int]] = None) -> np.ndarray:
    """
    Create a 3D Voronoi diagram using scipy's KDTree for faster computation.
    
    Args:
        centroids: Dictionary with labels as keys and (z,y,x) coordinates as values
        shape: Optional tuple of (Z,Y,X) dimensions. If None, calculated from centroids
    
    Returns:
        3D numpy array where each cell contains the label of the closest centroid as uint32
    """
    from scipy.spatial import cKDTree
    
    # Convert string labels to integers if necessary
    if any(isinstance(k, str) for k in centroids.keys()):
        label_map = {label: idx for idx, label in enumerate(centroids.keys())}
        centroids = {label_map[k]: v for k, v in centroids.items()}
    
    # Convert centroids to array and keep track of labels
    labels = np.array(list(centroids.keys()), dtype=np.uint32)
    centroid_points = np.array([centroids[label] for label in labels])
    
    # Calculate shape if not provided
    if shape is None:
        max_coords = centroid_points.max(axis=0)
        shape = tuple(max_coord + 1 for max_coord in max_coords)
    
    # Create KD-tree
    tree = cKDTree(centroid_points)
    
    # Create coordinate arrays
    coords = np.array(np.meshgrid(
        np.arange(shape[0]),
        np.arange(shape[1]),
        np.arange(shape[2]),
        indexing='ij'
    )).reshape(3, -1).T
    
    # Find nearest centroid for each point
    _, indices = tree.query(coords)
    
    # Convert indices to labels and ensure uint32 dtype
    label_array = labels[indices].astype(np.uint32)
    
    # Reshape to final shape
    return label_array.reshape(shape)