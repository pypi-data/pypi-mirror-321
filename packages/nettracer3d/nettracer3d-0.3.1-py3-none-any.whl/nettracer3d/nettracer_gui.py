import sys
import networkx as nx
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QSlider, QMenuBar, QMenu, QDialog, 
                            QFormLayout, QLineEdit, QPushButton, QFileDialog,
                            QLabel, QComboBox, QMessageBox, QTableView, QInputDialog,
                            QMenu, QTabWidget)
from PyQt6.QtCore import (QPoint, Qt, QAbstractTableModel, QTimer)
import numpy as np
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from qtrangeslider import QRangeSlider
from nettracer3d import nettracer as n3d
from nettracer3d import smart_dilate as sdl
from nettracer3d import proximity as pxt
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
from PyQt6.QtGui import (QFont, QCursor, QColor)
import tifffile
import copy
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
from functools import partial


class ImageViewerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NetTracer3D")
        self.setGeometry(100, 100, 1400, 800)
        
        # Initialize channel data and states
        self.channel_data = [None] * 4
        self.channel_visible = [False] * 4
        self.current_slice = 0
        self.active_channel = 0  # Initialize active channel

        self.color_dictionary = {
        # Reds
        "RED": (1, 0, 0),
        "LIGHT_RED": (1, 0.3, 0.3),
        "DARK_RED": (0.6, 0, 0),
        "CORAL": (1, 0.5, 0.3),
        
        # Oranges
        "ORANGE": (1, 0.5, 0),
        "LIGHT_ORANGE": (1, 0.7, 0.3),
        "DARK_ORANGE": (0.8, 0.3, 0),
        
        # Yellows
        "YELLOW": (1, 1, 0),
        "LIGHT_YELLOW": (1, 1, 0.5),
        "GOLD": (1, 0.84, 0),
        
        # Greens
        "GREEN": (0, 1, 0),
        "LIGHT_GREEN": (0.3, 1, 0.3),
        "DARK_GREEN": (0, 0.6, 0),
        "LIME": (0.6, 1, 0),
        "FOREST_GREEN": (0.13, 0.55, 0.13),
        
        # Blues
        "BLUE": (0, 0, 1),
        "LIGHT_BLUE": (0.3, 0.3, 1),
        "DARK_BLUE": (0, 0, 0.6),
        "ROYAL_BLUE": (0.25, 0.41, 0.88),
        "NAVY": (0, 0, 0.5),
        
        # Cyans
        "CYAN": (0, 1, 1),
        "LIGHT_CYAN": (0.5, 1, 1),
        "DARK_CYAN": (0, 0.6, 0.6),
        
        # Purples
        "PURPLE": (0.5, 0, 0.5),
        "LIGHT_PURPLE": (0.8, 0.6, 0.8),
        "VIOLET": (0.93, 0.51, 0.93),
        "MAGENTA": (1, 0, 1),
        
        # Neutrals
        "WHITE": (1, 1, 1),
        "GRAY": (0.5, 0.5, 0.5),
        "LIGHT_GRAY": (0.8, 0.8, 0.8),
        "DARK_GRAY": (0.2, 0.2, 0.2)
        }

        self.base_colors = [ #Channel colors
            self.color_dictionary['LIGHT_RED'],    # Lighter red
            self.color_dictionary['LIGHT_GREEN'],    # Lighter green
            self.color_dictionary['WHITE'],        # White
            self.color_dictionary['WHITE']         # White
        ]
        
        
        # Initialize selection state
        self.selecting = False
        self.selection_start = None
        self.selection_rect = None
        self.click_start_time = None  # Add this to track when click started
        self.selection_threshold = 1.0  # Time in seconds before starting rectangle selection
        
        # Initialize zoom mode state
        self.zoom_mode = False
        self.original_xlim = None
        self.original_ylim = None

        # Pan mode state
        self.pan_mode = False
        self.panning = False
        self.pan_start = None
        
        # Store brightness/contrast values for each channel
        self.channel_brightness = [{
            'min': 0,
            'max': 1
        } for _ in range(4)]
        
        # Create the brightness dialog but don't show it yet
        self.brightness_dialog = BrightnessContrastDialog(self)
        
        self.min_max = {
            0: [0,0],
            1: [0,0],
            2: [0,0],
            3: [0,0]
        }

        self.volume_dict = {
            0: None,
            1: None,
            2: None,
            3: None
        } #For storing thresholding information

        self.original_shape = None #For undoing resamples
        
        # Create control panel
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        
        # Create active channel selector
        active_channel_widget = QWidget()
        active_channel_layout = QHBoxLayout(active_channel_widget)
        
        active_label = QLabel("Active Image:")
        active_channel_layout.addWidget(active_label)
        
        self.active_channel_combo = QComboBox()
        self.active_channel_combo.addItems(["Nodes", "Edges", "Overlay 1", "Overlay 2"])
        self.active_channel_combo.setCurrentIndex(0)
        self.active_channel_combo.currentIndexChanged.connect(self.set_active_channel)
        # Initially disable the combo box
        self.active_channel_combo.setEnabled(False)
        active_channel_layout.addWidget(self.active_channel_combo)
        
        control_layout.addWidget(active_channel_widget)

        # Create zoom button and pan button
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)

        # Create zoom button
        self.zoom_button = QPushButton("🔍")
        self.zoom_button.setCheckable(True)
        self.zoom_button.setFixedSize(40, 40)
        self.zoom_button.clicked.connect(self.toggle_zoom_mode)
        control_layout.addWidget(self.zoom_button)

        self.pan_button = QPushButton("✋")
        self.pan_button.setCheckable(True)
        self.pan_button.setFixedSize(40, 40)
        self.pan_button.clicked.connect(self.toggle_pan_mode)
        buttons_layout.addWidget(self.pan_button)

        control_layout.addWidget(buttons_widget)
                
        # Create channel buttons
        self.channel_buttons = []
        self.delete_buttons = []  # New list to store delete buttons
        self.channel_names = ["Nodes", "Edges", "Overlay 1", "Overlay 2"]

        # Create channel toggles with delete buttons
        for i in range(4):
            # Create container for each channel's controls
            channel_container = QWidget()
            channel_layout = QHBoxLayout(channel_container)
            channel_layout.setSpacing(2)  # Reduce spacing between buttons
            
            # Create toggle button
            btn = QPushButton(f"{self.channel_names[i]}")
            btn.setCheckable(True)
            btn.setEnabled(False)
            btn.clicked.connect(lambda checked, ch=i: self.toggle_channel(ch))
            self.channel_buttons.append(btn)
            channel_layout.addWidget(btn)
            
            # Create delete button
            delete_btn = QPushButton("×")  # Using × character for delete
            delete_btn.setFixedSize(20, 20)  # Make it small and square
            delete_btn.setStyleSheet("""
                QPushButton {
                    background-color: transparent;
                    border: none;
                    color: gray;
                    font-weight: bold;
                }
                QPushButton:hover {
                    color: red;
                }
                QPushButton:disabled {
                    color: lightgray;
                }
            """)
            delete_btn.setEnabled(False)
            delete_btn.clicked.connect(lambda checked, ch=i: self.delete_channel(ch))
            self.delete_buttons.append(delete_btn)
            channel_layout.addWidget(delete_btn)
            
            control_layout.addWidget(channel_container)

        # Create the main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Create left panel for image and controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Create matplotlib canvas for image display
        self.figure = Figure(figsize=(8, 8))
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        left_layout.addWidget(self.canvas)

        
        left_layout.addWidget(control_panel)

        # Add timer for debouncing slice updates
        self._slice_update_timer = QTimer()
        self._slice_update_timer.setSingleShot(True)  # Only fire once after last trigger
        self._slice_update_timer.timeout.connect(self._do_slice_update)
        self.pending_slice = None  # Store the latest requested slice
        
        # Create container for slider and arrow buttons
        slider_container = QWidget()
        slider_layout = QHBoxLayout(slider_container)
        slider_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add left arrow button
        self.left_arrow = QPushButton("←")
        self.left_arrow.setFixedSize(30, 30)
        self.left_arrow.pressed.connect(self.start_left_scroll)
        self.left_arrow.released.connect(self.stop_continuous_scroll)
        slider_layout.addWidget(self.left_arrow)
        
        # Add slider for depth navigation
        self.slice_slider = QSlider(Qt.Orientation.Horizontal)
        self.slice_slider.setEnabled(False)
        self.slice_slider.valueChanged.connect(self.update_slice)
        slider_layout.addWidget(self.slice_slider)
        
        # Add right arrow button
        self.right_arrow = QPushButton("→")
        self.right_arrow.setFixedSize(30, 30)
        self.right_arrow.pressed.connect(self.start_right_scroll)
        self.right_arrow.released.connect(self.stop_continuous_scroll)
        slider_layout.addWidget(self.right_arrow)
        
        # Initialize continuous scroll timer
        self.continuous_scroll_timer = QTimer()
        self.continuous_scroll_timer.timeout.connect(self.continuous_scroll)
        self.scroll_direction = 0  # 0: none, -1: left, 1: right
        
        left_layout.addWidget(slider_container)

        
        main_layout.addWidget(left_panel)
        
        # Create right panel
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        # Create tabbed data widget for top right
        self.tabbed_data = TabbedDataWidget(self)
        right_layout.addWidget(self.tabbed_data)
        # Initialize data_table property to None - it will be set when tabs are added
        self.data_table = None
        
        # Create table control panel
        table_control = QWidget()
        table_control_layout = QHBoxLayout(table_control)
        
        # Create toggle buttons for tables
        self.network_button = QPushButton("Network")
        self.network_button.setCheckable(True)
        self.network_button.setChecked(True)
        self.network_button.clicked.connect(self.show_network_table)
        
        self.selection_button = QPushButton("Selection")
        self.selection_button.setCheckable(True)
        self.selection_button.clicked.connect(self.show_selection_table)
        
        # Add buttons to control layout
        table_control_layout.addWidget(self.network_button)
        table_control_layout.addWidget(self.selection_button)
        
        # Add control panel to right layout
        right_layout.addWidget(table_control)
        
        # Create both table views
        self.network_table = CustomTableView(self)
        self.selection_table = CustomTableView(self)
        empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
        self.selection_table.setModel(PandasModel(empty_df))
        self.network_table.setAlternatingRowColors(True)
        self.selection_table.setAlternatingRowColors(True)
        self.network_table.setSortingEnabled(True)
        self.selection_table.setSortingEnabled(True)
        
        # Initially show network table and hide selection table
        right_layout.addWidget(self.network_table)
        right_layout.addWidget(self.selection_table)
        self.selection_table.hide()
        
        # Store reference to currently active table
        self.active_table = self.network_table
        
        main_layout.addWidget(right_panel)
        
        # Create menu bar
        self.create_menu_bar()

        # Initialize clicked values dictionary
        self.clicked_values = {
            'nodes': [],
            'edges': []
        }
        
        # Connect mouse events
        self.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        self.canvas.mpl_connect('button_release_event', self.on_mouse_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        #self.canvas.mpl_connect('button_press_event', self.on_mouse_click)

        # Initialize measurement points tracking
        self.measurement_points = []  # List to store point pairs
        self.current_point = None  # Store first point of current pair
        self.current_pair_index = 0  # Track pair numbering
        

        # Add these new methods for handling neighbors and components (FOR RIGHT CLICKIGN)
        self.show_neighbors_clicked = None
        self.show_component_clicked = None

        # Initialize highlight overlay
        self.highlight_overlay = None
        self.highlight_bounds = None  # Store bounds for positioning

    def start_left_scroll(self):
        """Start scrolling left when left arrow is pressed."""
        # Single increment first
        current_value = self.slice_slider.value()
        if current_value > self.slice_slider.minimum():
            self.slice_slider.setValue(current_value - 1)
        # Then start continuous scroll
        self.scroll_direction = -1
        self.continuous_scroll_timer.start(200)  # 200ms interval for steady pace
        
    def start_right_scroll(self):
        """Start scrolling right when right arrow is pressed."""
        # Single increment first
        current_value = self.slice_slider.value()
        if current_value < self.slice_slider.maximum():
            self.slice_slider.setValue(current_value + 1)
        # Then start continuous scroll
        self.scroll_direction = 1
        self.continuous_scroll_timer.start(200)  # 200ms interval for steady pace
        
    def stop_continuous_scroll(self):
        """Stop continuous scrolling when arrow is released."""
        self.continuous_scroll_timer.stop()
        self.scroll_direction = 0
        
    def continuous_scroll(self):
        """Handle continuous scrolling while arrow is held."""
        current_value = self.slice_slider.value()
        new_value = current_value + self.scroll_direction
        
        if self.scroll_direction < 0 and new_value >= self.slice_slider.minimum():
            self.slice_slider.setValue(new_value)
        elif self.scroll_direction > 0 and new_value <= self.slice_slider.maximum():
            self.slice_slider.setValue(new_value)
        

    def create_highlight_overlay(self, node_indices=None, edge_indices=None, overlay1_indices = None, overlay2_indices = None):
        """
        Create a binary overlay highlighting specific nodes and/or edges using parallel processing.
        
        Args:
            node_indices (list): List of node indices to highlight
            edge_indices (list): List of edge indices to highlight
        """

        def process_chunk(chunk_data, indices_to_check):
            """Process a single chunk of the array to create highlight mask"""
            mask = np.isin(chunk_data, indices_to_check)
            return mask * 255

        if node_indices is not None:
            if 0 in node_indices:
                node_indices.remove(0)
        if edge_indices is not None:
            if 0 in edge_indices:
                edge_indices.remove(0)
        if overlay1_indices is not None:
            if 0 in overlay1_indices:
                overlay1_indices.remove(0)

        if node_indices is None:
            node_indices = []
        if edge_indices is None:
            edge_indices = []
        if overlay1_indices is None:
            overlay1_indices = []
        if overlay2_indices is None:
            overlay2_indices = []
            
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        
        if not node_indices and not edge_indices and not overlay1_indices and not overlay2_indices:
            self.highlight_overlay = None
            self.highlight_bounds = None
            self.update_display(preserve_zoom=(current_xlim, current_ylim))
            return
            
        # Get the shape of the full array from any existing channel
        for channel in self.channel_data:
            if channel is not None:
                full_shape = channel.shape
                break
        else:
            return  # No valid channels to get shape from
            
        # Initialize full-size overlay
        self.highlight_overlay = np.zeros(full_shape, dtype=np.uint8)
        
        # Get number of CPU cores
        num_cores = mp.cpu_count()
        
        # Calculate chunk size along y-axis
        chunk_size = full_shape[0] // num_cores
        if chunk_size < 1:
            chunk_size = 1
        
        def process_channel(channel_data, indices, array_shape):
            if channel_data is None or not indices:
                return None
                
            # Create chunks
            chunks = []
            for i in range(0, array_shape[0], chunk_size):
                end = min(i + chunk_size, array_shape[0])
                chunks.append(channel_data[i:end])
                
            # Process chunks in parallel using ThreadPoolExecutor
            process_func = partial(process_chunk, indices_to_check=indices)
            
            with ThreadPoolExecutor(max_workers=num_cores) as executor:
                chunk_results = list(executor.map(process_func, chunks))
                
            # Reassemble the chunks
            return np.vstack(chunk_results)
        
        # Process nodes and edges in parallel using multiprocessing
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_nodes = executor.submit(process_channel, self.channel_data[0], node_indices, full_shape)
            future_edges = executor.submit(process_channel, self.channel_data[1], edge_indices, full_shape)
            future_overlay1 = executor.submit(process_channel, self.channel_data[2], overlay1_indices, full_shape)
            future_overlay2 = executor.submit(process_channel, self.channel_data[3], overlay2_indices, full_shape)
            
            # Get results
            node_overlay = future_nodes.result()
            edge_overlay = future_edges.result()
            overlay1_overlay = future_overlay1.result()
            overlay2_overlay = future_overlay2.result()
            
        # Combine results
        if node_overlay is not None:
            self.highlight_overlay = np.maximum(self.highlight_overlay, node_overlay)
        if edge_overlay is not None:
            self.highlight_overlay = np.maximum(self.highlight_overlay, edge_overlay)
        if overlay1_overlay is not None:
            self.highlight_overlay = np.maximum(self.highlight_overlay, overlay1_overlay)
        if overlay2_overlay is not None:
            self.highlight_overlay = np.maximum(self.highlight_overlay, overlay2_overlay)
                
        # Update display
        self.update_display(preserve_zoom=(current_xlim, current_ylim))




#METHODS RELATED TO RIGHT CLICK:
    
    def create_context_menu(self, event):
        """Create and show context menu at mouse position."""
        if self.channel_data[self.active_channel] is not None:
            x_idx = int(round(event.xdata))
            y_idx = int(round(event.ydata))
            
            try:
                # Create context menu
                context_menu = QMenu(self)
                
                # Create "Show Neighbors" submenu
                neighbors_menu = QMenu("Show Neighbors", self)
                
                # Add submenu options
                show_neighbor_nodes = neighbors_menu.addAction("Show Neighboring Nodes")
                show_neighbor_all = neighbors_menu.addAction("Show Neighboring Nodes and Edges")
                show_neighbor_edge = neighbors_menu.addAction("Show Neighboring Edges")
                
                context_menu.addMenu(neighbors_menu)

                component_menu = QMenu("Show Connected Component(s)", self)
                show_component_nodes = component_menu.addAction("Just nodes")
                show_component_edges = component_menu.addAction("Nodes + Edges")
                show_component_only_edges = component_menu.addAction("Just edges")
                context_menu.addMenu(component_menu)

                community_menu = QMenu("Show Community(s)", self)
                show_community_nodes = community_menu.addAction("Just nodes")
                show_community_edges = community_menu.addAction("Nodes + Edges")
                context_menu.addMenu(community_menu)

                if my_network.node_identities is not None:
                    identity_menu = QMenu("Show Identity", self)
                    for item in set(my_network.node_identities.values()):
                        show_identity = identity_menu.addAction(f"ID: {item}")
                        show_identity.triggered.connect(lambda checked, item=item: self.handle_show_identities(sort=item))
                    context_menu.addMenu(identity_menu)

                select_all_menu = QMenu("Select All", self)
                select_nodes = select_all_menu.addAction("Nodes")
                select_both = select_all_menu.addAction("Nodes + Edges")
                select_edges = select_all_menu.addAction("Edges")
                context_menu.addMenu(select_all_menu)

                if len(self.clicked_values['nodes']) > 0 or len(self.clicked_values['edges']) > 0:
                    highlight_menu = QMenu("Selection", self)
                    if len(self.clicked_values['nodes']) > 1 or len(self.clicked_values['edges']) > 1:
                        combine_obj = highlight_menu.addAction("Combine Object Labels")
                        combine_obj.triggered.connect(self.handle_combine)
                    split_obj = highlight_menu.addAction("Split Non-Touching Labels")
                    split_obj.triggered.connect(self.handle_seperate)
                    delete_obj = highlight_menu.addAction("Delete Selection")
                    delete_obj.triggered.connect(self.handle_delete)
                    if len(self.clicked_values['nodes']) > 1:
                        link_nodes = highlight_menu.addAction("Link Nodes")
                        link_nodes.triggered.connect(self.handle_link)
                        delink_nodes = highlight_menu.addAction("Split Nodes")
                        delink_nodes.triggered.connect(self.handle_split)
                context_menu.addMenu(highlight_menu)

                # Create measure menu
                measure_menu = QMenu("Measure", self)

                if self.current_point is None:
                    # If no point is placed, show option to place first point
                    show_point_menu = measure_menu.addAction("Place Measurement Point")
                    show_point_menu.triggered.connect(
                        lambda: self.place_point(x_idx, y_idx, self.current_slice))
                else:
                    # If first point is placed, show option to place second point
                    show_point_menu = measure_menu.addAction("Place Second Point")
                    show_point_menu.triggered.connect(
                        lambda: self.place_point(x_idx, y_idx, self.current_slice))

                show_remove_menu = measure_menu.addAction("Remove Measurement Points")
                context_menu.addMenu(measure_menu)
                
                # Connect actions to callbacks
                show_neighbor_nodes.triggered.connect(self.handle_show_neighbors)
                show_neighbor_all.triggered.connect(lambda: self.handle_show_neighbors(edges=True))
                show_neighbor_edge.triggered.connect(lambda: self.handle_show_neighbors(edges = True, nodes = False))
                show_component_nodes.triggered.connect(self.handle_show_component)
                show_component_edges.triggered.connect(lambda: self.handle_show_component(edges = True))
                show_component_only_edges.triggered.connect(lambda: self.handle_show_component(edges = True, nodes = False))
                show_community_nodes.triggered.connect(self.handle_show_communities)
                show_community_edges.triggered.connect(lambda: self.handle_show_communities(edges = True))
                select_nodes.triggered.connect(lambda: self.handle_select_all(edges = False, nodes = True))
                select_both.triggered.connect(lambda: self.handle_select_all(edges = True))
                select_edges.triggered.connect(lambda: self.handle_select_all(edges = True, nodes = False))
                if self.highlight_overlay is not None:
                    highlight_select = context_menu.addAction("Add highlight in network selection")
                    highlight_select.triggered.connect(self.handle_highlight_select)
                show_remove_menu.triggered.connect(self.handle_remove_points)
                
                cursor_pos = QCursor.pos()
                context_menu.exec(cursor_pos)
                
            except IndexError:
                pass


    def place_point(self, x, y, z):
        """Place a measurement point at the specified coordinates."""
        if self.current_point is None:
            # This is the first point
            self.current_point = (x, y, z)
            self.ax.plot(x, y, 'yo', markersize=8)
            # Add pair index label above the point
            self.ax.text(x, y+5, str(self.current_pair_index), 
                        color='white', ha='center', va='bottom')
            self.canvas.draw()

        else:
            # This is the second point
            x1, y1, z1 = self.current_point
            x2, y2, z2 = x, y, z
            
            # Calculate distance
            distance = np.sqrt(((x2-x1)*my_network.xy_scale)**2 + ((y2-y1)*my_network.xy_scale)**2 + ((z2-z1)*my_network.z_scale)**2)
            distance2 = np.sqrt(((x2-x1))**2 + ((y2-y1))**2 + ((z2-z1))**2)
            
            # Store the point pair
            self.measurement_points.append({
                'pair_index': self.current_pair_index,
                'point1': self.current_point,
                'point2': (x2, y2, z2),
                'distance': distance,
                'distance2': distance2
            })
            
            # Draw second point and line
            self.ax.plot(x2, y2, 'yo', markersize=8)
            # Add pair index label above the second point
            self.ax.text(x2, y2+5, str(self.current_pair_index), 
                        color='white', ha='center', va='bottom')
            if z1 == z2:  # Only draw line if points are on same slice
                self.ax.plot([x1, x2], [y1, y2], 'r--', alpha=0.5)
            self.canvas.draw()
            
            # Update measurement display
            self.update_measurement_display()
            
            # Reset for next pair
            self.current_point = None
            self.current_pair_index += 1

    def handle_remove_points(self):
        """Remove all measurement points."""
        self.measurement_points = []
        self.current_point = None
        self.current_pair_index = 0
        self.update_display()
        self.update_measurement_display()

    # Modify the update_measurement_display method:
    def update_measurement_display(self):
        """Update the measurement information display in the top right widget."""
        if not self.measurement_points:
            # Create empty DataFrame with no specific headers
            df = pd.DataFrame()
        else:
            # Create data for DataFrame with measurement-specific headers
            data = []
            for point in self.measurement_points:
                x1, y1, z1 = point['point1']
                x2, y2, z2 = point['point2']
                data.append({
                    'Pair ID': point['pair_index'],
                    'Point 1 (X,Y,Z)': f"({x1:.1f}, {y1:.1f}, {z1})",
                    'Point 2 (X,Y,Z)': f"({x2:.1f}, {y2:.1f}, {z2})",
                    'Scaled Distance': f"{point['distance']:.2f}",
                    'Voxel Distance': f"{point['distance2']:.2f}"
                })
            df = pd.DataFrame(data)
        
        # Create new table for measurements
        table = CustomTableView(self)
        table.setModel(PandasModel(df))
        
        # Add to tabbed widget
        self.tabbed_data.add_table("Measurements", table)
        
        # Adjust column widths to content
        for column in range(table.model().columnCount(None)):
            table.resizeColumnToContents(column)


    def show_network_table(self):
        """Switch to display the main network table."""
        if not self.network_button.isChecked():
            self.network_button.setChecked(True)
            return
        self.selection_button.setChecked(False)
        self.network_table.show()
        self.selection_table.hide()
        self.active_table = self.network_table

    def show_selection_table(self):
        """Switch to display the selection table."""
        if not self.selection_button.isChecked():
            self.selection_button.setChecked(True)
            return
        self.network_button.setChecked(False)
        self.network_table.hide()
        self.selection_table.show()
        self.active_table = self.selection_table

    def handle_show_neighbors(self, edges=False, nodes = True):
        """Handle the Show Neighbors action."""

        try:
            if len(self.clicked_values['nodes']) > 0 or len(self.clicked_values['edges']) > 0:  # Check if we have any nodes selected

                old_nodes = copy.deepcopy(self.clicked_values['nodes']) 

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data
                
                # Create mask for rows where one column is any original node AND the other column is any neighbor
                mask = (
                    (original_df.iloc[:, 0].isin(self.clicked_values['nodes'])) |
                    (original_df.iloc[:, 1].isin(self.clicked_values['nodes'])) |
                    (original_df.iloc[:, 2].isin(self.clicked_values['edges']))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()
                
                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

                print(f"Found {len(filtered_df)} direct connections between nodes {old_nodes} and their neighbors")
                self.clicked_values['nodes'] = list(set(filtered_df.iloc[:, 0].to_list() + filtered_df.iloc[:, 1].to_list()))

                if not nodes:
                    self.clicked_values['nodes'] = old_nodes

                do_highlight = True

            else:

                do_highlight = False

            if do_highlight:
              
                # Create highlight overlay for visualization
                if edges:
                    edge_indices = filtered_df.iloc[:, 2].unique().tolist()
                    self.clicked_values['edges'] = edge_indices

                    self.create_highlight_overlay(
                        node_indices=self.clicked_values['nodes'], 
                        edge_indices=self.clicked_values['edges']
                    )
                else:
                    self.create_highlight_overlay(
                        node_indices=self.clicked_values['nodes']
                )
            
                
        except Exception as e:
            print(f"Error processing neighbors: {e}")

    
    def handle_show_component(self, edges = False, nodes = True):
        """Handle the Show Component action."""

        try:

            old_nodes = copy.deepcopy(self.clicked_values['nodes'])

            if len(self.clicked_values['nodes']) == 0: #If we haven't clicked anything, this will return the largest connected component

                G = my_network.isolate_connected_component(gen_images = False)

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data

                # Create mask for rows where one column is any original node AND the other column is any neighbor
                mask = (
                    (original_df.iloc[:, 0].isin(G.nodes()) & original_df.iloc[:, 1].isin(G.nodes()))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()

                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()


            else: #If we have clicked any nodes, we get the components of the clicked objects instead

                G = nx.Graph()

                for node in self.clicked_values['nodes']:

                    if node in G: #Meaning we've already done this component
                        continue
                    else: #Otherwise, get the graph and add it to the subgraph(s)
                        G1 = my_network.isolate_connected_component(gen_images = False, key = node)
                        G = nx.compose(G1, G)

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data

                # Create mask for rows of this component
                mask = (
                    (original_df.iloc[:, 0].isin(G.nodes()) & original_df.iloc[:, 1].isin(G.nodes()))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()
                
                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

            if not nodes:
                self.clicked_values['nodes'] = old_nodes
            else:
                self.clicked_values['nodes'] = G.nodes()

            if edges:
                edge_indices = filtered_df.iloc[:, 2].unique().tolist()
                self.clicked_values['edges'] = edge_indices
                self.create_highlight_overlay(
                    node_indices=self.clicked_values['nodes'],
                    edge_indices=edge_indices
                )
            else:
                self.create_highlight_overlay(
                    node_indices = self.clicked_values['nodes']
            )

        except Exception as e:

            print(f"Error finding component: {e}")

    def handle_show_communities(self, edges = False):

        def invert_dict(d):
            """For inverting the community dictionary"""
            inverted = {}
            for key, value in d.items():
                inverted.setdefault(value, []).append(key)
            return inverted

        try:

            if len(self.clicked_values['nodes']) > 0:

                if my_network.communities is None:
                    self.show_partition_dialog()

                communities = invert_dict(my_network.communities)

                targets = []

                for node in self.clicked_values['nodes']: #Get the communities we need

                    if node in targets:
                        continue
                    else:
                        targets.append(my_network.communities[node])

                nodes = []

                for com in targets: #Get the nodes for each community in question

                    for node in communities[com]:

                        nodes.append(node)

                nodes = list(set(nodes))

                # Get the existing DataFrame from the model
                original_df = self.network_table.model()._data

                # Create mask for rows for nodes in question
                mask = (
                    (original_df.iloc[:, 0].isin(nodes) & original_df.iloc[:, 1].isin(nodes))
                    )
                
                # Filter the DataFrame to only include direct connections
                filtered_df = original_df[mask].copy()
                
                # Create new model with filtered DataFrame and update selection table
                new_model = PandasModel(filtered_df)
                self.selection_table.setModel(new_model)
                
                # Switch to selection table
                self.selection_button.click()

                if edges:
                    edge_indices = filtered_df.iloc[:, 2].unique().tolist()
                    self.clicked_values['edges'] = edge_indices
                    self.create_highlight_overlay(
                        node_indices=nodes,
                        edge_indices=edge_indices
                    )
                    self.clicked_values['nodes'] = nodes
                else:
                    self.create_highlight_overlay(
                        node_indices = nodes
                )
                    self.clicked_values['nodes'] = nodes

        except Exception as e:
            print(f"Error showing communities: {e}")

    def handle_show_identities(self, sort):

        try:

            nodes = []

            for node in my_network.node_identities:
                if sort == my_network.node_identities[node]:
                    nodes.append(node)

            neighbors = set()  # Use a set from the start to avoid duplicates
            nodes += self.clicked_values['nodes']
            
            # Get the existing DataFrame from the model
            original_df = self.network_table.model()._data
            
            # Create mask for pairs that have nodes of the ID in question
            mask = (
                (original_df.iloc[:, 0].isin(nodes)) | (original_df.iloc[:, 1].isin(nodes))
            )
            
            # Filter the DataFrame to only include direct connections
            filtered_df = original_df[mask].copy()
            
            # Create new model with filtered DataFrame and update selection table
            new_model = PandasModel(filtered_df)
            self.selection_table.setModel(new_model)
            
            # Switch to selection table
            self.selection_button.click()

            print(f"Found {len(filtered_df)} direct connections between nodes of ID {sort} and their neighbors (of any ID)")

            self.create_highlight_overlay(
                node_indices= nodes
                )

        except Exception as e:
            print(f"Error showing identities: {e}")


    def handle_select_all(self, nodes = True, edges = False):

        try:

            if nodes:
                nodes = list(np.unique(my_network.nodes))
                if nodes[0] == 0:
                    del nodes[0]
            else:
                nodes = []
            if edges:
                edges = list(np.unique(my_network.edges))
                if edges[0] == 0:
                    del edges[0]
            else:
                edges = []

            self.clicked_values['nodes'] += nodes
            self.clicked_values['edges'] += edges

            self.create_highlight_overlay(edge_indices = self.clicked_values['edges'], node_indices = self.clicked_values['nodes'])

        except Exception as e:
            print(f"Error: {e}")

    def handle_info(self, sort = 'node'):

        try:

            info_dict = {}

            if sort == 'node':

                label = self.clicked_values['nodes'][-1]

                info_dict['Label'] = label

                info_dict['Object Class'] = 'Node'

                if my_network.node_identities is not None:
                    info_dict['ID'] = my_network.node_identities[label]

                if my_network.network is not None:
                    info_dict['Degree'] = my_network.network.degree(label)

                if my_network.communities is not None:
                    info_dict['Community'] = my_network.communities[label]

                if my_network.node_centroids is not None:
                    info_dict['Centroid'] = my_network.node_centroids[label]

                if self.volume_dict[0] is not None:
                    info_dict['Volume'] = self.volume_dict[0][label]


            elif sort == 'edge':

                label = self.clicked_values['edges'][-1]

                info_dict['Label'] = label

                info_dict['Object Class'] = 'Edge'

                if my_network.edge_centroids is not None:
                    info_dict['Centroid'] = my_network.edge_centroids[label]

                if self.volume_dict[1] is not None:
                    info_dict['Volume'] = self.volume_dict[1][label]

            self.format_for_upperright_table(info_dict, title = f'Info on Object')

        except:
            pass




    def handle_combine(self):

        try:

            self.clicked_values['nodes'].sort()
            nodes = copy.deepcopy(self.clicked_values['nodes'])
            self.clicked_values['edges'].sort()
            edges = copy.deepcopy(self.clicked_values['edges'])

            if len(nodes) > 1:
                new_nodes = nodes[0]

                mask = np.isin(self.channel_data[0], nodes)
                my_network.nodes[mask] = new_nodes
                self.load_channel(0, my_network.nodes, True)
                self.clicked_values['nodes'] = new_nodes

            if len(edges) > 1:
                new_edges = edges[0]

                mask = np.isin(self.channel_data[1], edges)
                my_network.edges[mask] = new_edges
                self.load_channel(1, my_network.edges, True)
                self.clicked_values['edges'] = new_edges

            try:

                for i in range(len(my_network.network_lists[0])):
                    if my_network.network_lists[0][i] in nodes and len(nodes) > 1:
                        my_network.network_lists[0][i] = new_nodes
                    if my_network.network_lists[1][i] in nodes and len(nodes) > 1:
                        my_network.network_lists[1][i] = new_nodes    
                    if my_network.network_lists[2][i] in edges and len(edges) > 1:
                        my_network.network_lists[2][i] = new_edges


                my_network.network_lists = my_network.network_lists

                if not hasattr(my_network, 'network_lists') or my_network.network_lists is None:
                    empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
                    model = PandasModel(empty_df)
                    self.network_table.setModel(model)
                else:
                    model = PandasModel(my_network.network_lists)
                    self.network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.network_table.resizeColumnToContents(column)

                self.highlight_overlay = None
                self.update_display()

                self.show_centroid_dialog()

            except Exception as e:
                print(f"Error, could not update network: {e}")


        except Exception as e:
            print(f"An error has occured: {e}")

    def handle_seperate(self):

        try:

            if len(self.clicked_values['nodes']) > 0:
                self.create_highlight_overlay(node_indices = self.clicked_values['nodes'])
                max_val = np.max(my_network.nodes)
                self.highlight_overlay, num = n3d.label_objects(self.highlight_overlay)

                node_bools = self.highlight_overlay != 0
                new_max = num + max_val
                self.highlight_overlay = self.highlight_overlay + max_val
                self.highlight_overlay = self.highlight_overlay * node_bools
                if new_max < 256:
                    dtype = np.uint8
                elif new_max < 65536:
                    dtype = np.uint16
                else:
                    dtype = np.uint32

                self.highlight_overlay = self.highlight_overlay.astype(dtype)
                my_network.nodes = my_network.nodes + self.highlight_overlay
                self.load_channel(0, my_network.nodes, True)

            if len(self.clicked_values['edges']) > 0:
                self.create_highlight_overlay(edge_indices = self.clicked_values['edges'])
                max_val = np.max(my_network.edges)
                self.highlight_overlay, num = n3d.label_objects(self.highlight_overlay)
                node_bools = self.highlight_overlay != 0
                new_max = num + max_val

                self.highlight_overlay = self.highlight_overlay + max_val
                self.highlight_overlay = self.highlight_overlay * node_bools
                if new_max < 256:
                    dtype = np.uint8
                elif new_max < 65536:
                    dtype = np.uint16
                else:
                    dtype = np.uint32

                self.highlight_overlay = self.highlight_overlay.astype(dtype)
                my_network.edges = my_network.edges + self.highlight_overlay
                self.load_channel(1, my_network.edges, True)
            self.highlight_overlay = None
            self.update_display()
            print("Network is not updated automatically, please recompute if necesarry. Identities are not automatically updated.")
            self.show_centroid_dialog()

        except Exception as e:
            print(f"Error seperating: {e}")





    def handle_delete(self):

        try:
            if len(self.clicked_values['nodes']) > 0:
                self.create_highlight_overlay(node_indices = self.clicked_values['nodes'])
                mask = self.highlight_overlay == 0
                my_network.nodes = my_network.nodes * mask
                self.load_channel(0, my_network.nodes, True)

                for i in range(len(my_network.network_lists[0]) - 1, -1, -1):
                    if my_network.network_lists[0][i] in self.clicked_values['nodes'] or my_network.network_lists[0][i] in self.clicked_values['nodes']:
                        del my_network.network_lists[0][i]
                        del my_network.network_lists[1][i]
                        del my_network.network_lists[2][i]



            if len(self.clicked_values['edges']) > 0:
                self.create_highlight_overlay(node_indices = self.clicked_values['edges'])
                mask = self.highlight_overlay == 0
                my_network.edges = my_network.edges * mask
                self.load_channel(1, my_network.edges, True)

                for i in range(len(my_network.network_lists[1]) - 1, -1, -1):
                    if my_network.network_lists[2][i] in self.clicked_values['edges']:
                        del my_network.network_lists[0][i]
                        del my_network.network_lists[1][i]
                        del my_network.network_lists[2][i]

            my_network.network_lists = my_network.network_lists


            if not hasattr(my_network, 'network_lists') or my_network.network_lists is None:
                empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
                model = PandasModel(empty_df)
                self.network_table.setModel(model)
            else:
                model = PandasModel(my_network.network_lists)
                self.network_table.setModel(model)
                # Adjust column widths to content
                for column in range(model.columnCount(None)):
                    self.network_table.resizeColumnToContents(column)

            self.show_centroid_dialog()
        except Exception as e:
            print(f"Error: {e}")

    def handle_link(self):

        try:
            nodes = self.clicked_values['nodes']
            from itertools import combinations
            pairs = list(combinations(nodes, 2))
            
            # Convert existing connections to a set of tuples for efficient lookup
            existing_connections = set()
            for n1, n2 in zip(my_network.network_lists[0], my_network.network_lists[1]):
                existing_connections.add((n1, n2))
                existing_connections.add((n2, n1))  # Add reverse pair too
            
            # Filter out existing connections
            new_pairs = []
            for pair in pairs:
                if pair not in existing_connections:
                    new_pairs.append(pair)
            
            # Add new connections
            for pair in new_pairs:
                my_network.network_lists[0].append(pair[0])
                my_network.network_lists[1].append(pair[1])
                my_network.network_lists[2].append(0)
            
            # Update the table
            if not hasattr(my_network, 'network_lists') or my_network.network_lists is None:
                empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
                model = PandasModel(empty_df)
                self.network_table.setModel(model)
            else:
                model = PandasModel(my_network.network_lists)
                self.network_table.setModel(model)
                # Adjust column widths to content
                for column in range(model.columnCount(None)):
                    self.network_table.resizeColumnToContents(column)
        except Exception as e:
            print(f"An error has occurred: {e}")


    def handle_split(self):
        try:
            nodes = self.clicked_values['nodes']

            from itertools import combinations

            pairs = list(combinations(nodes, 2))

            print(pairs)


            for i in range(len(my_network.network_lists[0]) - 1, -1, -1):
                print((my_network.network_lists[0][i], my_network.network_lists[1][i]))
                if (my_network.network_lists[0][i], my_network.network_lists[1][i]) in pairs or (my_network.network_lists[1][i], my_network.network_lists[0][i]) in pairs:
                    del my_network.network_lists[0][i]
                    del my_network.network_lists[1][i]
                    del my_network.network_lists[2][i]

            my_network.network_lists = my_network.network_lists

            if not hasattr(my_network, 'network_lists') or my_network.network_lists is None:
                empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
                model = PandasModel(empty_df)
                self.network_table.setModel(model)
            else:
                model = PandasModel(my_network.network_lists)
                self.network_table.setModel(model)
                # Adjust column widths to content
                for column in range(model.columnCount(None)):
                    self.network_table.resizeColumnToContents(column)
        except Exception as e:
            print(f"An error has occurred: {e}")







    def handle_highlight_select(self):

        try:

            # Get the existing DataFrame from the model
            original_df = self.network_table.model()._data
            
            # Create mask for rows where one column is any original node AND the other column is any neighbor
            mask = (
                (original_df.iloc[:, 0].isin(self.clicked_values['nodes'])) |
                (original_df.iloc[:, 1].isin(self.clicked_values['nodes'])) |
                (original_df.iloc[:, 2].isin(self.clicked_values['edges']))

            )
            
            # Filter the DataFrame to only include direct connections
            filtered_df = original_df[mask].copy()
            
            # Create new model with filtered DataFrame and update selection table
            new_model = PandasModel(filtered_df)
            self.selection_table.setModel(new_model)
            
            # Switch to selection table
            self.selection_button.click()

            print("Selected nodes + edges have been isolated in the selection table, alongside their neighbors")

        except Exception as e:
            print(f"Error: {e}")




        
    def toggle_zoom_mode(self):
        """Toggle zoom mode on/off."""
        self.zoom_mode = self.zoom_button.isChecked()
        if self.zoom_mode:
            self.pan_button.setChecked(False)
            self.pan_mode = False
            self.canvas.setCursor(Qt.CursorShape.CrossCursor)
        else:
            self.canvas.setCursor(Qt.CursorShape.ArrowCursor)

    def toggle_pan_mode(self):
        """Toggle pan mode on/off."""
        self.pan_mode = self.pan_button.isChecked()
        if self.pan_mode:
            self.zoom_button.setChecked(False)
            self.zoom_mode = False
            self.canvas.setCursor(Qt.CursorShape.OpenHandCursor)
        else:
            self.canvas.setCursor(Qt.CursorShape.ArrowCursor)

    def on_mouse_press(self, event):
        """Handle mouse press events."""
        if event.inaxes != self.ax:
            return
                
        if self.zoom_mode:
            # Handle zoom mode press
            if self.original_xlim is None:
                self.original_xlim = self.ax.get_xlim()
                self.original_ylim = self.ax.get_ylim()
            
            current_xlim = self.ax.get_xlim()
            current_ylim = self.ax.get_ylim()
            xdata = event.xdata
            ydata = event.ydata
            
            if event.button == 1:  # Left click - zoom in
                x_range = (current_xlim[1] - current_xlim[0]) / 4
                y_range = (current_ylim[1] - current_ylim[0]) / 4
                
                self.ax.set_xlim([xdata - x_range, xdata + x_range])
                self.ax.set_ylim([ydata - y_range, ydata + y_range])
                
            elif event.button == 3:  # Right click - zoom out
                x_range = (current_xlim[1] - current_xlim[0])
                y_range = (current_ylim[1] - current_ylim[0])
                
                new_xlim = [xdata - x_range, xdata + x_range]
                new_ylim = [ydata - y_range, ydata + y_range]
                
                if (new_xlim[0] <= self.original_xlim[0] or 
                    new_xlim[1] >= self.original_xlim[1] or
                    new_ylim[0] <= self.original_ylim[0] or
                    new_ylim[1] >= self.original_ylim[1]):
                    self.ax.set_xlim(self.original_xlim)
                    self.ax.set_ylim(self.original_ylim)
                else:
                    self.ax.set_xlim(new_xlim)
                    self.ax.set_ylim(new_ylim)
            
            self.canvas.draw()
                
        elif self.pan_mode:
            self.panning = True
            self.pan_start = (event.xdata, event.ydata)
            self.canvas.setCursor(Qt.CursorShape.ClosedHandCursor)
        
        elif event.button == 3:  # Right click (for context menu)
            self.create_context_menu(event)
        
        elif event.button == 1:  # Left click
            # Store initial click position but don't start selection yet
            self.selection_start = (event.xdata, event.ydata)
            self.selecting = False  # Will be set to True if the mouse moves while button is held

    def on_mouse_move(self, event):
        """Handle mouse movement events."""
        if event.inaxes != self.ax:
            return
                
        if self.selection_start and not self.selecting and not self.pan_mode and not self.zoom_mode:
            # If mouse has moved more than a tiny amount while button is held, start selection
            if (abs(event.xdata - self.selection_start[0]) > 1 or 
                abs(event.ydata - self.selection_start[1]) > 1):
                self.selecting = True
                self.selection_rect = plt.Rectangle(
                    (self.selection_start[0], self.selection_start[1]), 0, 0,
                    fill=False, color='white', linestyle='--'
                )
                self.ax.add_patch(self.selection_rect)
                
        if self.selecting and self.selection_rect is not None:
            # Update selection rectangle
            x0 = min(self.selection_start[0], event.xdata)
            y0 = min(self.selection_start[1], event.ydata)
            width = abs(event.xdata - self.selection_start[0])
            height = abs(event.ydata - self.selection_start[1])
            
            self.selection_rect.set_bounds(x0, y0, width, height)
            self.canvas.draw()

        elif self.panning and self.pan_start is not None:
            # Calculate the movement
            dx = event.xdata - self.pan_start[0]
            dy = event.ydata - self.pan_start[1]
            
            # Get current view limits
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            
            # Calculate new limits
            new_xlim = [xlim[0] - dx, xlim[1] - dx]
            new_ylim = [ylim[0] - dy, ylim[1] - dy]
            
            # Get image bounds
            if self.channel_data[0] is not None:  # Use first channel as reference
                img_height, img_width = self.channel_data[0][self.current_slice].shape
                
                # Ensure new limits don't go beyond image bounds
                if new_xlim[0] < 0:
                    new_xlim = [0, xlim[1] - xlim[0]]
                elif new_xlim[1] > img_width:
                    new_xlim = [img_width - (xlim[1] - xlim[0]), img_width]
                    
                if new_ylim[0] < 0:
                    new_ylim = [0, ylim[1] - ylim[0]]
                elif new_ylim[1] > img_height:
                    new_ylim = [img_height - (ylim[1] - ylim[0]), img_height]
            
            # Apply new limits
            self.ax.set_xlim(new_xlim)
            self.ax.set_ylim(new_ylim)
            self.canvas.draw()
            
            # Update pan start position
            self.pan_start = (event.xdata, event.ydata)

    def on_mouse_release(self, event):
        """Handle mouse release events."""
        if self.pan_mode:
            self.panning = False
            self.pan_start = None
            self.canvas.setCursor(Qt.CursorShape.OpenHandCursor)
        elif event.button == 1:  # Left button release
            if self.selecting and self.selection_rect is not None:
                # Get the rectangle bounds
                x0 = min(self.selection_start[0], event.xdata)
                y0 = min(self.selection_start[1], event.ydata)
                width = abs(event.xdata - self.selection_start[0])
                height = abs(event.ydata - self.selection_start[1])
                
                # Get current slice data for active channel
                if self.channel_data[self.active_channel] is not None:
                    data = self.channel_data[self.active_channel][self.current_slice]
                    
                    # Convert coordinates to array indices
                    x_min = max(0, int(x0))
                    y_min = max(0, int(y0))
                    x_max = min(data.shape[1], int(x0 + width))
                    y_max = min(data.shape[0], int(y0 + height))
                    
                    # Extract unique non-zero values in selection rectangle
                    selected_region = data[y_min:y_max, x_min:x_max]
                    selected_values = np.unique(selected_region)
                    selected_values = selected_values[selected_values != 0]  # Remove background
                    
                    # Check if ctrl is pressed
                    ctrl_pressed = 'ctrl' in event.modifiers
                    
                    # Update clicked_values based on active channel
                    if self.active_channel == 0:  # Nodes
                        if not ctrl_pressed:
                            self.clicked_values['nodes'] = []  # Clear existing selection if ctrl not pressed
                        self.clicked_values['nodes'].extend(selected_values)
                        # Remove duplicates while preserving order
                        self.clicked_values['nodes'] = list(dict.fromkeys(self.clicked_values['nodes']))
                        self.create_highlight_overlay(node_indices=self.clicked_values['nodes'])
                        
                        # Try to highlight the last selected value in tables
                        if self.clicked_values['nodes']:
                            self.highlight_value_in_tables(self.clicked_values['nodes'][-1])
                            
                    elif self.active_channel == 1:  # Edges
                        if not ctrl_pressed:
                            self.clicked_values['edges'] = []  # Clear existing selection if ctrl not pressed
                        self.clicked_values['edges'].extend(selected_values)
                        # Remove duplicates while preserving order
                        self.clicked_values['edges'] = list(dict.fromkeys(self.clicked_values['edges']))
                        self.create_highlight_overlay(edge_indices=self.clicked_values['edges'])
                        
                        # Try to highlight the last selected value in tables
                        if self.clicked_values['edges']:
                            self.highlight_value_in_tables(self.clicked_values['edges'][-1])

            
            elif not self.selecting and self.selection_start:  # If we had a click but never started selection
                # Handle as a normal click
                self.on_mouse_click(event)
            
            # Clean up
            self.selection_start = None
            self.selecting = False
            if self.selection_rect is not None:
                self.selection_rect.remove()
                self.selection_rect = None
                self.canvas.draw()

    def highlight_value_in_tables(self, clicked_value):
        """Helper method to find and highlight a value in both tables."""
        
        if not self.network_table.model() and not self.selection_table.model():
            return False

        found = False
        tables_to_check = [self.network_table, self.selection_table]
        active_table_index = tables_to_check.index(self.active_table)
        
        # Reorder tables to check active table first
        tables_to_check = tables_to_check[active_table_index:] + tables_to_check[:active_table_index]
        
        for table in tables_to_check:
            if table.model() is None:
                continue
                
            df = table.model()._data

            # Create appropriate masks based on active channel
            if self.active_channel == 0:  # Nodes channel
                col1_matches = df[df.columns[0]] == clicked_value
                col2_matches = df[df.columns[1]] == clicked_value
                all_matches = col1_matches | col2_matches

            elif self.active_channel == 1:  # Edges channel
                all_matches = df[df.columns[2]] == clicked_value

            else:
                continue

            if all_matches.any():
                # Get indices from the current dataframe's index
                match_indices = df[all_matches].index.tolist()
                
                # If this is the active table, handle selection and scrolling
                if table == self.active_table:
                    current_row = table.currentIndex().row()
                    
                    # Convert match_indices to row numbers (position in the visible table)
                    row_positions = [df.index.get_loc(idx) for idx in match_indices]
                    
                    # Find next match after current position
                    if current_row >= 0:
                        next_positions = [pos for pos in row_positions if pos > current_row]
                        row_pos = next_positions[0] if next_positions else row_positions[0]
                    else:
                        row_pos = row_positions[0]
                    
                    # Update selection and scroll
                    model_index = table.model().index(row_pos, 0)
                    table.scrollTo(model_index)
                    table.clearSelection()
                    table.selectRow(row_pos)
                    table.setCurrentIndex(model_index)

                    # Add highlighting for specific cells based on active channel
                    if self.active_channel == 0:  # Nodes channel
                        # Only highlight cells in columns 0 and 1 where the value matches
                        if df.iloc[row_pos, 0] == clicked_value:
                            table.model().highlight_cell(row_pos, 0)
                        if df.iloc[row_pos, 1] == clicked_value:
                            table.model().highlight_cell(row_pos, 1)
                    else:  # Edges channel
                        # Highlight the edge column
                        table.model().highlight_cell(row_pos, 2)
                
                found = True

        return found

    def on_mouse_click(self, event):
        """Handle mouse clicks for zooming and data inspection."""
        if event.inaxes != self.ax:
            return
            
        if self.zoom_mode:
            # Existing zoom functionality
            if self.original_xlim is None:
                self.original_xlim = self.ax.get_xlim()
                self.original_ylim = self.ax.get_ylim()
            
            current_xlim = self.ax.get_xlim()
            current_ylim = self.ax.get_ylim()
            xdata = event.xdata
            ydata = event.ydata
            
            if event.button == 1:  # Left click - zoom in
                x_range = (current_xlim[1] - current_xlim[0]) / 4
                y_range = (current_ylim[1] - current_ylim[0]) / 4
                
                self.ax.set_xlim([xdata - x_range, xdata + x_range])
                self.ax.set_ylim([ydata - y_range, ydata + y_range])
                
            elif event.button == 3:  # Right click - zoom out
                x_range = (current_xlim[1] - current_xlim[0])
                y_range = (current_ylim[1] - current_ylim[0])
                
                new_xlim = [xdata - x_range, xdata + x_range]
                new_ylim = [ydata - y_range, ydata + y_range]
                
                if (new_xlim[0] <= self.original_xlim[0] or 
                    new_xlim[1] >= self.original_xlim[1] or
                    new_ylim[0] <= self.original_ylim[0] or
                    new_ylim[1] >= self.original_ylim[1]):
                    self.ax.set_xlim(self.original_xlim)
                    self.ax.set_ylim(self.original_ylim)
                else:
                    self.ax.set_xlim(new_xlim)
                    self.ax.set_ylim(new_ylim)
            
            self.canvas.draw()
        
        elif event.button == 3:  # Right click
            self.create_context_menu(event)

        else:  # Not in zoom mode - handle value inspection
            if self.channel_data[self.active_channel] is not None:
                try:
                    # Get clicked value
                    x_idx = int(round(event.xdata))
                    y_idx = int(round(event.ydata))
                    # Check if Ctrl key is pressed (using matplotlib's key_press system)
                    ctrl_pressed = 'ctrl' in event.modifiers  # Note: changed from 'control' to 'ctrl'
                    if self.channel_data[self.active_channel][self.current_slice, y_idx, x_idx] != 0:
                        clicked_value = self.channel_data[self.active_channel][self.current_slice, y_idx, x_idx]
                    else:
                        if not ctrl_pressed:
                            self.clicked_values = {
                                'nodes': [],
                                'edges': []
                            }
                            self.create_highlight_overlay()
                        return
                    

                    starting_vals = copy.deepcopy(self.clicked_values)
                    
                    # Store or remove the clicked value in the appropriate list
                    if self.active_channel == 0:
                        if ctrl_pressed:
                            if clicked_value in self.clicked_values['nodes']:
                                # Remove value if it's already selected
                                self.clicked_values['nodes'].remove(clicked_value)
                            else:
                                # Add value if it's not already selected
                                self.clicked_values['nodes'].append(clicked_value)
                        else:
                            # Reset both lists and start new selection
                            self.clicked_values = {'nodes': [clicked_value], 'edges': []}
                        # Get latest value (or the last remaining one if we just removed an item)
                        latest_value = self.clicked_values['nodes'][-1] if self.clicked_values['nodes'] else None
                        self.handle_info('node')
                    elif self.active_channel == 1:
                        if ctrl_pressed:
                            if clicked_value in self.clicked_values['edges']:
                                # Remove value if it's already selected
                                self.clicked_values['edges'].remove(clicked_value)
                            else:
                                # Add value if it's not already selected
                                self.clicked_values['edges'].append(clicked_value)
                        else:
                            # Reset both lists and start new selection
                            self.clicked_values = {'nodes': [], 'edges': [clicked_value]}
                        # Get latest value (or the last remaining one if we just removed an item)
                        latest_value = self.clicked_values['edges'][-1] if self.clicked_values['edges'] else None
                        self.handle_info('edge')

                    
                    # Try to find and highlight the latest value in the current table
                    try:
                        found = self.highlight_value_in_tables(latest_value)
                    except:
                        return
                    
                    # If not found in current table but it exists in the other table, offer to switch
                    if not found:
                        other_table = self.selection_table if self.active_table == self.network_table else self.network_table
                        if other_table.model() is not None:
                            df = other_table.model()._data
                            if self.active_channel == 0:
                                exists_in_other = (df[df.columns[0]] == latest_value).any() or (df[df.columns[1]] == latest_value).any()
                            else:
                                exists_in_other = (df[df.columns[2]] == latest_value).any()
                                
                            if exists_in_other:
                                # Switch to the other table
                                if other_table == self.network_table:
                                    self.network_button.click()
                                else:
                                    self.selection_button.click()
                                # Now highlight in the newly active table
                                self.highlight_value_in_tables(latest_value)

                    # Highlight the clicked element in the image using the stored lists                
                    if self.active_channel == 0 and (starting_vals['nodes']) != (self.clicked_values['nodes']):
                        self.create_highlight_overlay(node_indices=self.clicked_values['nodes'], edge_indices=self.clicked_values['edges'])
                    elif self.active_channel == 1 and starting_vals['edges'] != self.clicked_values['edges']:
                        self.create_highlight_overlay(node_indices=self.clicked_values['nodes'], edge_indices=self.clicked_values['edges'])

                                
                except IndexError:
                    pass  # Clicked outside image boundaries
                
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")

        # Create Save submenu
        save_menu = file_menu.addMenu("Save")
        network_save = save_menu.addAction("Save Network3D Object")
        network_save.triggered.connect(lambda: self.save_network_3d(False))
        for i in range(4):
            save_action = save_menu.addAction(f"Save {self.channel_names[i]}")
            save_action.triggered.connect(lambda checked, ch=i: self.save(ch, False))
        highlight_save = save_menu.addAction("Save Highlight Overlay")
        highlight_save.triggered.connect(lambda checked, ch=4: self.save(ch, False))

        # Create Save As submenu
        save_as_menu = file_menu.addMenu("Save As")
        network_saveas = save_as_menu.addAction("Save Network3D Object As")
        network_saveas.triggered.connect(lambda: self.save_network_3d(True))
        for i in range(4):
            save_action = save_as_menu.addAction(f"Save {self.channel_names[i]} As")
            save_action.triggered.connect(lambda checked, ch=i: self.save(ch))
        highlight_save = save_as_menu.addAction("Save Highlight Overlay As")
        highlight_save.triggered.connect(lambda checked, ch=4: self.save(ch))
        
        # Create Load submenu
        load_menu = file_menu.addMenu("Load")
        network_load = load_menu.addAction("Load Network3D Object")
        network_load.triggered.connect(self.load_from_network_obj)
        for i in range(4):
            load_action = load_menu.addAction(f"Load {self.channel_names[i]}")
            load_action.triggered.connect(lambda checked, ch=i: self.load_channel(ch))
        load_action = load_menu.addAction("Load Network")
        load_action.triggered.connect(self.load_network)
        misc_menu = load_menu.addMenu("Load Misc Properties")
        load_action = misc_menu.addAction("Load Node IDs")
        load_action.triggered.connect(lambda: self.load_misc('Node Identities'))
        load_action = misc_menu.addAction("Load Node Centroids")
        load_action.triggered.connect(lambda: self.load_misc('Node Centroids'))
        load_action = misc_menu.addAction("Load Edge Centroids")
        load_action.triggered.connect(lambda: self.load_misc('Edge Centroids'))
        load_action = misc_menu.addAction("Merge Nodes")
        load_action.triggered.connect(lambda: self.load_misc('Merge Nodes'))

        
        # Analysis menu
        analysis_menu = menubar.addMenu("Analyze")
        network_menu = analysis_menu.addMenu("Network")
        netshow_action = network_menu.addAction("Show Network")
        netshow_action.triggered.connect(self.show_netshow_dialog)
        partition_action = network_menu.addAction("Community Partition + Community Stats")
        partition_action.triggered.connect(self.show_partition_dialog)
        stats_menu = analysis_menu.addMenu("Stats")
        allstats_action = stats_menu.addAction("Calculate Generic Network Stats")
        allstats_action.triggered.connect(self.stats)
        radial_action = stats_menu.addAction("Radial Distribution Analysis")
        radial_action.triggered.connect(self.show_radial_dialog)
        degree_dist_action = stats_menu.addAction("Degree Distribution Analysis")
        degree_dist_action.triggered.connect(self.show_degree_dist_dialog)
        neighbor_id_action = stats_menu.addAction("Identity Distribution of Neighbors")
        neighbor_id_action.triggered.connect(self.show_neighbor_id_dialog)
        random_action = stats_menu.addAction("Generate Equivalent Random Network")
        random_action.triggered.connect(self.show_random_dialog)
        vol_action = stats_menu.addAction("Calculate Volumes")
        vol_action.triggered.connect(self.volumes)
        inter_action = stats_menu.addAction("Calculate Node < > Edge Interaction")
        inter_action.triggered.connect(self.show_interaction_dialog)
        overlay_menu = analysis_menu.addMenu("Data/Overlays")
        degree_action = overlay_menu.addAction("Get Degree Information")
        degree_action.triggered.connect(self.show_degree_dialog)
        hub_action = overlay_menu.addAction("Get Hub Information")
        hub_action.triggered.connect(self.show_hub_dialog)
        mother_action = overlay_menu.addAction("Get Mother Nodes")
        mother_action.triggered.connect(self.show_mother_dialog)
        community_code_action = overlay_menu.addAction("Code Communities")
        community_code_action.triggered.connect(lambda: self.show_code_dialog(sort = 'Community'))
        id_code_action = overlay_menu.addAction("Code Identities")
        id_code_action.triggered.connect(lambda: self.show_code_dialog(sort = 'Identity'))


        # Process menu
        process_menu = menubar.addMenu("Process")
        calculate_menu = process_menu.addMenu("Calculate")
        calc_all_action = calculate_menu.addAction("Calculate All (Find Node-Edge-Node Network)")
        calc_all_action.triggered.connect(self.show_calc_all_dialog)
        calc_prox_action = calculate_menu.addAction("Calculate Proximity Network (connect nodes by distance)")
        calc_prox_action.triggered.connect(self.show_calc_prox_dialog)
        centroid_action = calculate_menu.addAction("Calculate Centroids (Active Image)")
        centroid_action.triggered.connect(self.show_centroid_dialog)

        image_menu = process_menu.addMenu("Image")
        resize_action = image_menu.addAction("Resize (Up/Downsample)")
        resize_action.triggered.connect(self.show_resize_dialog)
        dilate_action = image_menu.addAction("Dilate")
        dilate_action.triggered.connect(self.show_dilate_dialog)
        erode_action = image_menu.addAction("Erode")
        erode_action.triggered.connect(self.show_erode_dialog)
        hole_action = image_menu.addAction("Fill Holes")
        hole_action.triggered.connect(self.show_hole_dialog)
        binarize_action = image_menu.addAction("Binarize")
        binarize_action.triggered.connect(self.show_binarize_dialog)
        label_action = image_menu.addAction("Label Objects")
        label_action.triggered.connect(self.show_label_dialog)
        thresh_action = image_menu.addAction("Threshold/Segment")
        thresh_action.triggered.connect(self.show_thresh_dialog)
        mask_action = image_menu.addAction("Mask Channel")
        mask_action.triggered.connect(self.show_mask_dialog)
        skeletonize_action = image_menu.addAction("Skeletonize")
        skeletonize_action.triggered.connect(self.show_skeletonize_dialog)
        watershed_action = image_menu.addAction("Watershed")
        watershed_action.triggered.connect(self.show_watershed_dialog)
        z_proj_action = image_menu.addAction("Z Project")
        z_proj_action.triggered.connect(self.show_z_dialog)

        generate_menu = process_menu.addMenu("Generate")
        centroid_node_action = generate_menu.addAction("Generate Nodes (From Node Centroids)")
        centroid_node_action.triggered.connect(self.show_centroid_node_dialog)
        gennodes_action = generate_menu.addAction("Generate Nodes (From 'Edge' Vertices)")
        gennodes_action.triggered.connect(self.show_gennodes_dialog)
        branch_action = generate_menu.addAction("Label Branches")
        branch_action.triggered.connect(self.show_branch_dialog)
        genvor_action = generate_menu.addAction("Generate Voronoi Diagram (From Node Centroids) - goes in Overlay2")
        genvor_action.triggered.connect(self.voronoi)

        modify_action = process_menu.addAction("Modify Network")
        modify_action.triggered.connect(self.show_modify_dialog)

        
        # Image menu
        image_menu = menubar.addMenu("Image")
        properties_action = image_menu.addAction("Properties")
        properties_action.triggered.connect(self.show_properties_dialog)
        brightness_action = image_menu.addAction("Adjust Brightness/Contrast")
        brightness_action.triggered.connect(self.show_brightness_dialog)
        color_action = image_menu.addAction("Channel Colors")
        color_action.triggered.connect(self.show_color_dialog)
        overlay_menu = image_menu.addMenu("Overlays")
        netoverlay_action = overlay_menu.addAction("Create Network Overlay")
        netoverlay_action.triggered.connect(self.show_netoverlay_dialog)
        idoverlay_action = overlay_menu.addAction("Create ID Overlay")
        idoverlay_action.triggered.connect(self.show_idoverlay_dialog)
        searchoverlay_action = overlay_menu.addAction("Show Search Regions")
        white_action = overlay_menu.addAction("White Background Overlay")
        white_action.triggered.connect(self.show_white_dialog)
        searchoverlay_action.triggered.connect(self.show_search_dialog)
        shuffle_action = overlay_menu.addAction("Shuffle")
        shuffle_action.triggered.connect(self.show_shuffle_dialog)
        show3d_action = image_menu.addAction("Show 3D (beta)")
        show3d_action.triggered.connect(self.show3d_dialog)


    def stats(self):
        """Method to get and display the network stats"""
        # Get the stats dictionary
        try:
            stats = my_network.get_network_stats()

            self.format_for_upperright_table(stats, title = 'Network Stats')
        except Exception as e:
            print(f"Error finding stats: {e}")

    def volumes(self):


        if self.active_channel == 1:
            output = my_network.volumes('edges')
            self.format_for_upperright_table(output, metric='Edge ID', value = 'Voxel Volume (Scaled)', title = 'Edge Volumes')
            self.volume_dict[1] = output

        elif self.active_channel == 0:
            output = my_network.volumes('nodes')
            self.format_for_upperright_table(output, metric='Node ID', value = 'Voxel Volume (Scaled)', title = 'Node Volumes')
            self.volume_dict[0] = output

        elif self.active_channel == 2:
            output = my_network.volumes('network_overlay')
            self.format_for_upperright_table(output, metric='Object ID', value = 'Voxel Volume (Scaled)', title = 'Overlay 1 Volumes')
            self.volume_dict[2] = output

        elif self.active_channel == 3:
            output = my_network.volumes('id_overlay')
            self.format_for_upperright_table(output, metric='Object ID', value = 'Voxel Volume (Scaled)', title = 'Overlay 2 Volumes')
            self.volume_dict[3] = output

        

    def format_for_upperright_table(self, data, metric='Metric', value='Value', title=None):
        """
        Format dictionary or list data for display in upper right table.
        
        Args:
            data: Dictionary with keys and single/multiple values, or a list of values
            metric: String for the key/index column header
            value: String or list of strings for value column headers (used for dictionaries only)
            title: Optional custom title for the tab
        """
        def convert_to_numeric(val):
            """Helper function to convert strings to numeric types when possible"""
            if isinstance(val, str):
                try:
                    # First try converting to int
                    if '.' not in val:
                        return int(val)
                    # If that fails or if there's a decimal point, try float
                    return float(val)
                except ValueError:
                    return val
            return val
        
        if isinstance(data, (list, tuple, np.ndarray)):
            # Handle list input - create single column DataFrame
            df = pd.DataFrame({
                metric: [convert_to_numeric(val) for val in data]
            })
            
            # Format floating point numbers
            df[metric] = df[metric].apply(lambda x: f"{x:.3f}" if isinstance(x, (float, np.float64)) else str(x))
            
        else:  # Dictionary input
            # Get sample value to determine structure
            sample_value = next(iter(data.values()))
            is_multi_value = isinstance(sample_value, (list, tuple, np.ndarray))
            
            if is_multi_value:
                # Handle multi-value case
                if isinstance(value, str):
                    # If single string provided for multi-values, generate numbered headers
                    n_cols = len(sample_value)
                    value_headers = [f"{value}_{i+1}" for i in range(n_cols)]
                else:
                    # Use provided list of headers
                    value_headers = value
                    if len(value_headers) != len(sample_value):
                        raise ValueError("Number of headers must match number of values per key")
                
                # Create lists for each column
                dict_data = {metric: list(data.keys())}
                for i, header in enumerate(value_headers):
                    # Convert values to numeric when possible before adding to DataFrame
                    dict_data[header] = [convert_to_numeric(data[key][i]) for key in data.keys()]
                
                df = pd.DataFrame(dict_data)
                
                # Format floating point numbers in all value columns
                for header in value_headers:
                    df[header] = df[header].apply(lambda x: f"{x:.3f}" if isinstance(x, (float, np.float64)) else str(x))
                    
            else:
                # Single-value case
                df = pd.DataFrame({
                    metric: data.keys(),
                    value: [convert_to_numeric(val) for val in data.values()]
                })
                
                # Format floating point numbers
                df[value] = df[value].apply(lambda x: f"{x:.3f}" if isinstance(x, (float, np.float64)) else str(x))
        
        # Create new table
        table = CustomTableView(self)
        table.setModel(PandasModel(df))
        
        # Add to tabbed widget
        if title is None:
            self.tabbed_data.add_table(f"{metric} Analysis", table)
        else:
            self.tabbed_data.add_table(f"{title}", table)
        
        # Adjust column widths to content
        for column in range(table.model().columnCount(None)):
            table.resizeColumnToContents(column)


    def show_watershed_dialog(self):
        """Show the watershed parameter dialog."""
        dialog = WatershedDialog(self)
        dialog.exec()

    def show_z_dialog(self):
        """Show the z-proj dialog."""
        dialog = ZDialog(self)
        dialog.exec()

    def show_calc_all_dialog(self):
        """Show the calculate all parameter dialog."""
        dialog = CalcAllDialog(self)
        dialog.exec()

    def show_calc_prox_dialog(self):
        """Show the proximity calc dialog"""
        dialog = ProxDialog(self)
        dialog.exec()

    def show_centroid_dialog(self):
        """show the centroid dialog"""
        dialog = CentroidDialog(self)
        dialog.exec()

    def show_dilate_dialog(self):
        """show the dilate dialog"""
        dialog = DilateDialog(self)
        dialog.exec()

    def show_erode_dialog(self):
        """show the erode dialog"""
        dialog = ErodeDialog(self)
        dialog.exec()

    def show_hole_dialog(self):
        """show the hole dialog"""
        dialog = HoleDialog(self)
        dialog.exec()

    def show_label_dialog(self):
        """Show the label dialog"""
        dialog = LabelDialog(self)
        dialog.exec()

    def show_thresh_dialog(self):
        """Show threshold dialog"""
        thresh_window = ThresholdWindow(self)
        thresh_window.show()  # Non-modal window

    def show_mask_dialog(self):
        """Show the mask dialog"""
        dialog = MaskDialog(self)
        dialog.exec()

    def show_skeletonize_dialog(self):
        """show the skeletonize dialog"""
        dialog = SkeletonizeDialog(self)
        dialog.exec()

    def show_centroid_node_dialog(self):
        """show the centroid node dialog"""
        dialog = CentroidNodeDialog(self)
        dialog.exec()


    def show_gennodes_dialog(self, down_factor = None, called = False):
        """show the gennodes dialog"""
        gennodes = GenNodesDialog(self, down_factor = down_factor, called = called)
        gennodes.exec()

    def show_branch_dialog(self):
        """Show the branch label dialog"""
        dialog = BranchDialog(self)
        dialog.exec()

    def voronoi(self):

        try:

            if my_network.nodes is not None:
                shape = my_network.nodes.shape
            else:
                shape = None

            if my_network.node_centroids is None:
                self.show_centroid_dialog()
                if my_network.node_centroids is None:
                    print("Node centroids must be set")
                    return

            array = pxt.create_voronoi_3d_kdtree(my_network.node_centroids, shape)
            self.load_channel(3, array, True)

        except Exception as e:
            print(f"Error generating voronoi: {e}")


    def show_modify_dialog(self):
        """Show the network modify dialog"""
        dialog = ModifyDialog(self)
        dialog.exec()


    def show_binarize_dialog(self):
        """show the binarize dialog"""
        dialog = BinarizeDialog(self)
        dialog.exec()


    def show_resize_dialog(self):
        """show the resize dialog"""
        dialog = ResizeDialog(self)
        dialog.exec()


    def show_properties_dialog(self):
        """Show the properties dialog"""
        dialog = PropertiesDialog(self)
        dialog.exec()
    
    def show_brightness_dialog(self):
        """Show the brightness/contrast control dialog."""
        self.brightness_dialog.show()

    def show_color_dialog(self):
        """Show the color control dialog."""
        dialog = ColorDialog(self)
        dialog.exec()



    def show_netoverlay_dialog(self):
        """show the net overlay dialog"""
        dialog = NetOverlayDialog(self)
        dialog.exec()

    def show_idoverlay_dialog(self):
        """show the id overlay dialog"""
        dialog = IdOverlayDialog(self)
        dialog.exec()

    def show_search_dialog(self):
        """Show the search dialog"""
        dialog = SearchOverlayDialog(self)
        dialog.exec()

    def show_white_dialog(self):
        """Show the white dialog"""
        dialog = WhiteDialog(self)
        dialog.exec()

    def show_shuffle_dialog(self):
        """Show the shuffle dialog"""
        dialog = ShuffleDialog(self)
        dialog.exec()

    def show3d_dialog(self):
        """Show the 3D control dialog"""
        dialog = Show3dDialog(self)
        dialog.exec()

    
    def load_misc(self, sort):
        """Loads various things"""

        def uncork(my_dict, trumper = None):

            if trumper is None:
                for thing in my_dict:
                    val = my_dict[thing]
                    new_val = val[0]
                    for i in range(1, len(val)):
                        try:
                            new_val += f" AND {val[i]}"
                        except:
                            break
                    my_dict[thing] = new_val
            elif trumper == '-':
                for key, value in my_dict.items():
                    my_dict[key] = value[0]
            else:
                for thing in my_dict:
                    val = my_dict[thing]
                    if trumper in val:
                        my_dict[thing] = trumper
                    else:
                        new_val = val[0]
                        for i in range(1, len(val)):
                            try:
                                new_val += f" AND {val[i]}"
                            except:
                                break
                        my_dict[thing] = new_val

            return my_dict

        if sort != 'Merge Nodes':

            try:

                filename, _ = QFileDialog.getOpenFileName(
                    self,
                    f"Load {sort}",
                    "",
                    "Spreadsheets (*.xlsx *.csv *.json)"
                )

                try:
                    if sort == 'Node Identities':
                        my_network.load_node_identities(file_path = filename)

                        first_value = list(my_network.node_identities.values())[0]  # Check that there are not multiple IDs
                        if isinstance(first_value, (list, tuple)):
                            trump_value, ok = QInputDialog.getText(
                                self,
                                'Multiple IDs Detected',
                                'The node identities appear to contain multiple ids per node in a list.\n'
                                'If you desire one node ID to trump all others, enter it here.\n'
                                '(Enter "-" to have the first IDs trump all others or press x to skip)'
                            )
                            if not ok or trump_value.strip() == '':
                                trump_value = None
                            elif trump_value.upper() == '-':
                                trump_value = '-'
                            my_network.node_identities = uncork(my_network.node_identities, trump_value)
                        else:
                            trump_value = None
                            my_network.node_identities = uncork(my_network.node_identities, trump_value)


                        if hasattr(my_network, 'node_identities') and my_network.node_identities is not None:
                            try:
                                self.format_for_upperright_table(my_network.node_identities, 'NodeID', 'Identity', 'Node Identities')
                            except Exception as e:
                                print(f"Error loading node identity table: {e}")

                    elif sort == 'Node Centroids':
                        my_network.load_node_centroids(file_path = filename)

                        if hasattr(my_network, 'node_centroids') and my_network.node_centroids is not None:
                            try:
                                self.format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                            except Exception as e:
                                print(f"Error loading node centroid table: {e}")

                    elif sort == 'Edge Centroids':
                        my_network.load_edge_centroids(file_path = filename)

                        if hasattr(my_network, 'edge_centroids') and my_network.edge_centroids is not None:
                            try:
                                self.format_for_upperright_table(my_network.edge_centroids, 'EdgeID', ['Z', 'Y', 'X'], 'Edge Centroids')
                            except Exception as e:
                                print(f"Error loading edge centroid table: {e}")


                except Exception as e:
                    import traceback
                    print(traceback.format_exc())
                    print(f"An error has occured: {e}")

            except Exception as e:
                import traceback
                print(traceback.format_exc())
                QMessageBox.critical(
                    self,
                    "Error Loading",
                    f"Failed to load {sort}: {str(e)}"
                )

        else:
            try:

                if len(np.unique(my_network.nodes)) < 3:
                    self.show_label_dialog()

                # First ask user what they want to select
                msg = QMessageBox()
                msg.setWindowTitle("Selection Type")
                msg.setText("Would you like to select a TIFF file or a directory?")
                tiff_button = msg.addButton("TIFF File", QMessageBox.ButtonRole.AcceptRole)
                dir_button = msg.addButton("Directory", QMessageBox.ButtonRole.AcceptRole)
                msg.addButton("Cancel", QMessageBox.ButtonRole.RejectRole)

                msg.exec()

                if msg.clickedButton() == tiff_button:
                    # Code for selecting TIFF files
                    filename, _ = QFileDialog.getOpenFileName(
                        self,
                        "Select TIFF file",
                        "",
                        "TIFF files (*.tiff *.tif)"
                    )
                    if filename:
                        selected_path = filename

                elif msg.clickedButton() == dir_button:
                    # Code for selecting directories
                    dialog = QFileDialog(self)
                    dialog.setOption(QFileDialog.Option.DontUseNativeDialog)
                    dialog.setOption(QFileDialog.Option.ReadOnly)
                    dialog.setFileMode(QFileDialog.FileMode.Directory)
                    dialog.setViewMode(QFileDialog.ViewMode.Detail)

                    if dialog.exec() == QFileDialog.DialogCode.Accepted:
                        selected_path = dialog.directory().absolutePath()

                my_network.merge_nodes(selected_path)
                self.load_channel(0, my_network.nodes, True)


                if hasattr(my_network, 'node_identities') and my_network.node_identities is not None:
                    try:
                        self.format_for_upperright_table(my_network.node_identities, 'NodeID', 'Identity', 'Node Identities')
                    except Exception as e:
                        print(f"Error loading node identity table: {e}")

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error Merging",
                    f"Failed to load {sort}: {str(e)}"
                )


    # Modify load_from_network_obj method
    def load_from_network_obj(self):
        try: 
            directory = QFileDialog.getExistingDirectory(
                self,
                f"Select Directory for Network3D Object",
                "",
                QFileDialog.Option.ShowDirsOnly
            )

            my_network.assemble(directory)

            # Load image channels
            try:
                self.load_channel(0, my_network.nodes, True)
            except Exception as e:
                print(e)
            try:
                self.load_channel(1, my_network.edges, True)
            except Exception as e:
                print(e)
            try:
                self.load_channel(2, my_network.network_overlay, True)
            except Exception as e:
                print(e)
            try:
                self.load_channel(3, my_network.id_overlay, True)
            except Exception as e:
                print(e)

            # Update slider range based on new data
            for channel in self.channel_data:
                if channel is not None:
                    self.slice_slider.setEnabled(True)
                    self.slice_slider.setMinimum(0)
                    self.slice_slider.setMaximum(channel.shape[0] - 1)
                    self.slice_slider.setValue(0)
                    self.current_slice = 0
                    break

            # Display network_lists in the network table
            # Create empty DataFrame for network table if network_lists is None
            if not hasattr(my_network, 'network_lists') or my_network.network_lists is None:
                empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
                model = PandasModel(empty_df)
                self.network_table.setModel(model)
            else:
                model = PandasModel(my_network.network_lists)
                self.network_table.setModel(model)
                # Adjust column widths to content
                for column in range(model.columnCount(None)):
                    self.network_table.resizeColumnToContents(column)

            if hasattr(my_network, 'node_centroids') and my_network.node_centroids is not None:
                try:
                    self.format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                except Exception as e:
                    print(f"Error loading node centroid table: {e}")

            if hasattr(my_network, 'edge_centroids') and my_network.edge_centroids is not None:
                try:
                    self.format_for_upperright_table(my_network.edge_centroids, 'EdgeID', ['Z', 'Y', 'X'], 'Edge Centroids')
                except Exception as e:
                    print(f"Error loading edge centroid table: {e}")

            if hasattr(my_network, 'node_identities') and my_network.node_identities is not None:
                try:
                    self.format_for_upperright_table(my_network.node_identities, 'NodeID', 'Identity', 'Node Identities')
                except Exception as e:
                    print(f"Error loading node identity table: {e}")


            if hasattr(my_network, 'communities') and my_network.communities is not None:
                try:
                    self.format_for_upperright_table(my_network.communities, 'NodeID', 'Community', 'Node Communities')
                except Exception as e:
                    print(f"Error loading node community table: {e}")

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Loading Network 3D Object",
                f"Failed to load Network 3D Object: {str(e)}"
            )



    def load_network(self):
        """Load in the network from a .xlsx (need to add .csv support)"""

        try:

            filename, _ = QFileDialog.getOpenFileName(
                self,
                f"Load Network",
                "",
                "Spreadsheets (*.xlsx *.csv *.json)"
            )

            my_network.load_network(file_path = filename)

            # Display network_lists in the network table
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error loading network table: {e}")

        except Exception as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.critical(
                self,
                "Error Loading File",
                f"Failed to load network: {str(e)}"
            )



    def set_active_channel(self, index):
        """Set the active channel and update UI accordingly."""
        self.active_channel = index
        # Update button appearances to show active channel
        for i, btn in enumerate(self.channel_buttons):
            if i == index and btn.isEnabled():
                btn.setStyleSheet("background-color: lightblue;")
            else:
                btn.setStyleSheet("")

    def reduce_rgb_dimension(self, array, method='first'):
        """
        Reduces a 4D array (Z, Y, X, C) to 3D (Z, Y, X) by dropping the color dimension
        using the specified method.
        
        Parameters:
        -----------
        array : numpy.ndarray
            4D array with shape (Z, Y, X, C) where C is the color channel dimension
        method : str, optional
            Method to use for reduction:
            - 'first': takes the first color channel (default)
            - 'mean': averages across color channels
            - 'max': takes maximum value across color channels
            - 'min': takes minimum value across color channels
        
        Returns:
        --------
        numpy.ndarray
            3D array with shape (Z, Y, X)
        
        Raises:
        -------
        ValueError
            If input array is not 4D or method is not recognized
        """
        if array.ndim != 4:
            raise ValueError(f"Expected 4D array, got {array.ndim}D array")
        
        if method not in ['first', 'mean', 'max', 'min']:
            raise ValueError(f"Unknown method: {method}")
        
        if method == 'first':
            return array[..., 0]
        elif method == 'mean':
            return np.mean(array, axis=-1)
        elif method == 'max':
            return np.max(array, axis=-1)
        else:  # min
            return np.min(array, axis=-1)

    def confirm_rgb_dialog(self):
        """Shows a dialog asking user to confirm if image is 2D RGB"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText("Image Format Detection")
        msg.setInformativeText("Is this a 2D color (RGB/CMYK) image?")
        msg.setWindowTitle("Confirm Image Format")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        return msg.exec() == QMessageBox.StandardButton.Yes

    def load_channel(self, channel_index, channel_data=None, data=False, assign_shape = True):
        """Load a channel and enable active channel selection if needed."""

        try:
            if not data:  # For solo loading
                import tifffile
                filename, _ = QFileDialog.getOpenFileName(
                    self,
                    f"Load Channel {channel_index + 1}",
                    "",
                    "TIFF Files (*.tif *.tiff)"
                )
                self.channel_data[channel_index] = tifffile.imread(filename)
                if len(self.channel_data[channel_index].shape) == 2:  # handle 2d data
                    self.channel_data[channel_index] = np.expand_dims(self.channel_data[channel_index], axis=0)

            else:
                self.channel_data[channel_index] = channel_data

            if len(self.channel_data[channel_index].shape) == 3:  # potentially 2D RGB
                if self.channel_data[channel_index].shape[-1] in (3, 4):  # last dim is 3 or 4
                    if self.confirm_rgb_dialog():
                        # User confirmed it's 2D RGB, expand to 4D
                        self.channel_data[channel_index] = np.expand_dims(self.channel_data[channel_index], axis=0)
                        
            if len(self.channel_data[channel_index].shape) == 4 and (channel_index == 0 or channel_index == 1):
                self.channel_data[channel_index] = self.reduce_rgb_dimension(self.channel_data[channel_index])



            if channel_index == 0:
                my_network.nodes = self.channel_data[channel_index]
            elif channel_index == 1:
                my_network.edges = self.channel_data[channel_index]
            elif channel_index == 2:
                my_network.network_overlay = self.channel_data[channel_index]
            elif channel_index == 3:
                my_network.id_overlay = self.channel_data[channel_index]
            
            # Enable the channel button
            self.channel_buttons[channel_index].setEnabled(True)
            self.delete_buttons[channel_index].setEnabled(True) 

            
            # Enable active channel selector if this is the first channel loaded
            if not self.active_channel_combo.isEnabled():
                self.active_channel_combo.setEnabled(True)
            
            # Update slider range if this is the first channel loaded
            if len(self.channel_data[channel_index].shape) == 3:
                if not self.slice_slider.isEnabled():
                    self.slice_slider.setEnabled(True)
                    self.slice_slider.setMinimum(0)
                    self.slice_slider.setMaximum(self.channel_data[channel_index].shape[0] - 1)
                    self.slice_slider.setValue(0)
                    self.current_slice = 0
                else:
                    self.slice_slider.setEnabled(True)
                    self.slice_slider.setMinimum(0)
                    self.slice_slider.setMaximum(self.channel_data[channel_index].shape[0] - 1)
                    self.slice_slider.setValue(0)
                    self.current_slice = 0
            else:
                self.slice_slider.setEnabled(False)

            
            # If this is the first channel loaded, make it active
            if all(not btn.isEnabled() for btn in self.channel_buttons[:channel_index]):
                self.set_active_channel(channel_index)

            if not self.channel_buttons[channel_index].isChecked():
                self.channel_buttons[channel_index].click()
            self.min_max[channel_index][0] = np.min(self.channel_data[channel_index])
            self.min_max[channel_index][1] = np.max(self.channel_data[channel_index])
            self.volume_dict[channel_index] = None #reset volumes

            if assign_shape: #keep original shape tracked to undo resampling.
                self.original_shape = self.channel_data[channel_index].shape
            
            self.update_display()

                
        except Exception as e:
            if not data:
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.critical(
                    self,
                    "Error Loading File",
                    f"Failed to load tiff file: {str(e)}"
                )

    def delete_channel(self, channel_index, called = True):
        """Delete the specified channel and update the display."""
        if called:
            # Confirm deletion
            reply = QMessageBox.question(
                self,
                'Delete Channel',
                f'Are you sure you want to delete the {self.channel_names[channel_index]} channel?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
        else:
            reply = False
        
        if reply == QMessageBox.StandardButton.Yes or not called:
            # Set channel data to None
            self.channel_data[channel_index] = None
            
            # Update corresponding network property
            if channel_index == 0:
                my_network.nodes = None
                my_network.node_centroids = None
                my_network.node_identities = None
            elif channel_index == 1:
                my_network.edges = None
                my_network.edge_centroids = None
            elif channel_index == 2:
                my_network.network_overlay = None
            elif channel_index == 3:
                my_network.id_overlay = None
            
            # Disable buttons
            self.channel_buttons[channel_index].setEnabled(False)
            self.channel_buttons[channel_index].setChecked(False)
            self.delete_buttons[channel_index].setEnabled(False)
            self.channel_visible[channel_index] = False
            
            # If this was the active channel, switch to the first available channel
            if self.active_channel == channel_index:
                for i in range(4):
                    if self.channel_data[i] is not None:
                        self.set_active_channel(i)
                        break
                else:
                    # If no channels are available, disable active channel selector
                    self.active_channel_combo.setEnabled(False)
            
            # Update display
            self.update_display()

    def reset(self, nodes = False, network = False, xy_scale = 1, z_scale = 1, edges = False, search_region = False, network_overlay = False, id_overlay = False):
        """Method to flexibly reset certain fields to free up the RAM as desired"""
        
        # Set scales first before any clearing operations
        my_network.xy_scale = xy_scale
        my_network.z_scale = z_scale

        if network:
            my_network.network = None
            my_network.communities = None

            # Create empty DataFrame
            empty_df = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
            
            # Clear network table
            self.network_table.setModel(PandasModel(empty_df))
            
            # Clear selection table
            self.selection_table.setModel(PandasModel(empty_df))

        if nodes:
            self.delete_channel(0, False)

        if edges:
            self.delete_channel(1, False)

        if search_region:
            my_network.search_region = None

        if network_overlay:
            self.delete_channel(2, False)

        if id_overlay:
            self.delete_channel(3, False)



    def save_network_3d(self, asbool = True):

        try:
            if asbool:  # Save As
                # First let user select parent directory
                parent_dir = QFileDialog.getExistingDirectory(
                    self,
                    "Select Location for Network3D Object Outputs",
                    "",
                    QFileDialog.Option.ShowDirsOnly
                )

                if parent_dir:  # If user didn't cancel
                    # Prompt user for new folder name
                    new_folder_name, ok = QInputDialog.getText(
                        self,
                        "New Folder",
                        "Enter name for new output folder:"
                    )
                
            else:  # Save
                parent_dir = None  # Let the backend handle default save location
            
            # Call appropriate save method
            if parent_dir is not None or not asbool:  # Proceed if we have a filename OR if it's a regular save
                if asbool:
                    my_network.dump(parent_dir = parent_dir, name = new_folder_name)
                else:
                    my_network.dump(name = 'my_network')
                
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Saving File",
                f"Failed to save file: {str(e)}"
            )


    def save(self, ch_index, asbool=True):
        """Handle both Save and Save As operations."""
        try:
            if asbool:  # Save As
                # Open file dialog for saving
                filename, _ = QFileDialog.getSaveFileName(
                    self,
                    f"Save Image As",
                    "",  # Default directory
                    "TIFF Files (*.tif *.tiff);;All Files (*)"  # File type filter
                )
                
                if filename:  # Only proceed if user didn't cancel
                    # If user didn't type an extension, add .tif
                    if not filename.endswith(('.tif', '.tiff')):
                        filename += '.tif'
            else:  # Save
                filename = None  # Let the backend handle default save location
            
            # Call appropriate save method
            if filename is not None or not asbool:  # Proceed if we have a filename OR if it's a regular save
                if ch_index == 0:
                    my_network.save_nodes(filename=filename)
                elif ch_index == 1:
                    my_network.save_edges(filename=filename)
                elif ch_index == 2:
                    my_network.save_network_overlay(filename=filename)
                elif ch_index == 3:
                    my_network.save_id_overlay(filename=filename)
                elif ch_index == 4:
                    if filename == None:
                        filename = "Highlighted_Element.tif"
                    tifffile.imwrite(f"{filename}", self.highlight_overlay)
                
                #print(f"Saved {self.channel_names[ch_index]}" + (f" to: {filename}" if filename else ""))  # Debug print
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error Saving File",
                f"Failed to save file: {str(e)}"
            )

    def toggle_channel(self, channel_index):
        """Toggle visibility of a channel."""
        # Store current zoom settings before toggling
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        
        self.channel_visible[channel_index] = self.channel_buttons[channel_index].isChecked()
        self.update_display(preserve_zoom=(current_xlim, current_ylim))

    
    def update_slice(self):
        """Queue a slice update when slider moves."""
        # Store current view settings
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        
        # Store the pending slice and view settings
        self.pending_slice = (self.slice_slider.value(), (current_xlim, current_ylim))
        
        # Reset and restart timer
        self._slice_update_timer.start(20)  # 20ms delay
        
    def _do_slice_update(self):
        """Actually perform the slice update after debounce delay."""
        if self.pending_slice is not None:
            slice_value, view_settings = self.pending_slice
            self.current_slice = slice_value
            self.update_display(preserve_zoom=view_settings)
            self.pending_slice = None

    def update_brightness(self, channel_index, values):
        """Update brightness/contrast settings for a channel."""

        # Store current zoom settings before toggling
        current_xlim = self.ax.get_xlim() if hasattr(self, 'ax') and self.ax.get_xlim() != (0, 1) else None
        current_ylim = self.ax.get_ylim() if hasattr(self, 'ax') and self.ax.get_ylim() != (0, 1) else None
        # Convert slider values (0-100) to data values (0-1)
        min_val, max_val = values
        self.channel_brightness[channel_index]['min'] = min_val / 255
        self.channel_brightness[channel_index]['max'] = max_val / 255
        self.update_display(preserve_zoom = (current_xlim, current_ylim))
    
    def update_display(self, preserve_zoom=None):
            """Update the display with currently visible channels and highlight overlay."""
            self.figure.clear()
            
            # Create subplot with tight layout and white figure background
            self.figure.patch.set_facecolor('white')
            self.ax = self.figure.add_subplot(111)
            
            # Store current zoom limits if they exist and weren't provided
            if preserve_zoom is None and hasattr(self, 'ax'):
                current_xlim = self.ax.get_xlim() if self.ax.get_xlim() != (0, 1) else None
                current_ylim = self.ax.get_ylim() if self.ax.get_ylim() != (0, 1) else None
            else:
                current_xlim, current_ylim = preserve_zoom if preserve_zoom else (None, None)
            
            # Define base colors for each channel with increased intensity
            base_colors = self.base_colors
            # Set only the axes (image area) background to black
            self.ax.set_facecolor('black')
            
            # Display each visible channel
            for channel in range(4):
                if (self.channel_visible[channel] and 
                    self.channel_data[channel] is not None):
                    
                    # Check if we're dealing with RGB data
                    is_rgb = len(self.channel_data[channel].shape) == 4 and self.channel_data[channel].shape[-1] == 3
                    
                    if len(self.channel_data[channel].shape) == 3 and not is_rgb:
                        current_image = self.channel_data[channel][self.current_slice, :, :]
                    elif is_rgb:
                        current_image = self.channel_data[channel][self.current_slice]  # Already has RGB channels
                    else:
                        current_image = self.channel_data[channel]

                    if is_rgb:
                        # For RGB images, just display directly without colormap
                        self.ax.imshow(current_image,
                                     alpha=0.7)
                    else:
                        # Regular channel processing with colormap
                        # Calculate brightness/contrast limits from entire volume
                        img_min = self.min_max[channel][0]
                        img_max = self.min_max[channel][1]
                        
                        # Calculate vmin and vmax, ensuring we don't get a zero range
                        if img_min == img_max:
                            vmin = img_min
                            vmax = img_min + 1
                        else:
                            vmin = img_min + (img_max - img_min) * self.channel_brightness[channel]['min']
                            vmax = img_min + (img_max - img_min) * self.channel_brightness[channel]['max']
                        
                        # Normalize the image safely
                        if vmin == vmax:
                            normalized_image = np.zeros_like(current_image)
                        else:
                            normalized_image = np.clip((current_image - vmin) / (vmax - vmin), 0, 1)
                        
                        # Create custom colormap with higher intensity
                        color = base_colors[channel]
                        custom_cmap = LinearSegmentedColormap.from_list(
                            f'custom_{channel}',
                            [(0,0,0,0), (*color,1)]
                        )
                        
                        # Display the image with slightly higher alpha
                        self.ax.imshow(normalized_image,
                                     alpha=0.7,
                                     cmap=custom_cmap,
                                     vmin=0,
                                     vmax=1)

            # Rest of the code remains the same...
            # Add highlight overlay if it exists
            if self.highlight_overlay is not None:
                highlight_slice = self.highlight_overlay[self.current_slice]
                highlight_cmap = LinearSegmentedColormap.from_list(
                    'highlight',
                    [(0, 0, 0, 0), (1, 1, 0, 1)]  # yellow
                )
                self.ax.imshow(highlight_slice,
                             cmap=highlight_cmap,
                             alpha=0.5)

            # Restore zoom limits if they existed
            if current_xlim is not None and current_ylim is not None:
                self.ax.set_xlim(current_xlim)
                self.ax.set_ylim(current_ylim)
            
            # Style the axes
            self.ax.set_xlabel('X')
            self.ax.set_ylabel('Y')
            self.ax.set_title(f'Slice {self.current_slice}')

            # Make axis labels and ticks black for visibility against white background
            self.ax.xaxis.label.set_color('black')
            self.ax.yaxis.label.set_color('black')
            self.ax.title.set_color('black')
            self.ax.tick_params(colors='black')
            for spine in self.ax.spines.values():
                spine.set_color('black')

            # Adjust the layout to ensure the plot fits well in the figure
            self.figure.tight_layout()

            # Redraw measurement points and their labels
            for point in self.measurement_points:
                x1, y1, z1 = point['point1']
                x2, y2, z2 = point['point2']
                pair_idx = point['pair_index']
                
                # Draw points and labels if they're on current slice
                if z1 == self.current_slice:
                    self.ax.plot(x1, y1, 'yo', markersize=8)
                    self.ax.text(x1, y1+5, str(pair_idx), 
                                color='white', ha='center', va='bottom')
                if z2 == self.current_slice:
                    self.ax.plot(x2, y2, 'yo', markersize=8)
                    self.ax.text(x2, y2+5, str(pair_idx), 
                                color='white', ha='center', va='bottom')
                    
                # Draw line if both points are on current slice
                if z1 == z2 == self.current_slice:
                    self.ax.plot([x1, x2], [y1, y2], 'r--', alpha=0.5)
        
            self.canvas.draw()

    def show_netshow_dialog(self):
        dialog = NetShowDialog(self)
        dialog.exec()

    def show_partition_dialog(self):
        dialog = PartitionDialog(self)
        dialog.exec()

    def show_radial_dialog(self):
        dialog = RadialDialog(self)
        dialog.exec()

    def show_degree_dist_dialog(self):
        dialog = DegreeDistDialog(self)
        dialog.exec()

    def show_neighbor_id_dialog(self):
        dialog = NeighborIdentityDialog(self)
        dialog.exec()

    def show_random_dialog(self):
        dialog = RandomDialog(self)
        dialog.exec()


    def show_interaction_dialog(self):
        dialog = InteractionDialog(self)
        dialog.exec()

    def show_degree_dialog(self):
        dialog = DegreeDialog(self)
        dialog.exec()


    def show_hub_dialog(self):
        dialog = HubDialog(self)
        dialog.exec()

    def show_mother_dialog(self):
        dialog = MotherDialog(self)
        dialog.exec()

    def show_code_dialog(self, sort = 'Community'):
        dialog = CodeDialog(self, sort = sort)
        dialog.exec()



#TABLE RELATED: 
class SearchWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Popup)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search...")
        self.search_input.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.search_input)
        
        close_button = QPushButton("×")
        close_button.setFixedSize(20, 20)
        close_button.clicked.connect(self.hide)
        layout.addWidget(close_button)
        
        # Store the last searched text and matches
        self.last_search = None
        self.current_match_index = -1
        self.current_matches = []
        
    def on_text_changed(self, text):
        self.last_search = text if text else None
        self.current_match_index = -1
        self.current_matches = []
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.hide()
        elif event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            if self.last_search is not None:
                table_view = self.parent()
                
                if table_view.is_top_table:
                    self.search_top_table(table_view)
                else:
                    # Use existing bottom table search logic
                    main_window = table_view.parent
                    if table_view == main_window.active_table:
                        try:
                            value = int(self.last_search)
                            main_window.highlight_value_in_tables(value)
                        except ValueError:
                            pass
        else:
            super().keyPressEvent(event)

    def search_top_table(self, table_view):
        """Search function for top tables that handles varying formats"""

        if not table_view.model():
            return
            
        model = table_view.model()
        
        try:
            df = model._data
            
            # If this is a new search, find all matches
            for row in range(df.shape[0]):
                for col in range(df.shape[1]):
                    cell_value = str(df.iloc[row, col]).lower()
                    if self.last_search.lower() in cell_value:
                        self.current_matches.append((row, col))
                
                        
            if not self.current_matches:
                return
                
            # Increment current match index or wrap around
            self.current_match_index = (self.current_match_index + 1) % len(self.current_matches)
            row, col = self.current_matches[self.current_match_index]
            
            # Create index for the current match
            model_index = model.index(row, col)
            
            # Highlight the cell in the model
            model.highlight_cell(row, col)
            
            # Select and scroll to the match
            table_view.setCurrentIndex(model_index)
            table_view.scrollTo(model_index)
            
            # Clear previous selection and select the current cell
            table_view.clearSelection()
            table_view.setFocus()
            
        except Exception as e:
            print(f"Error during search: {str(e)}")

class CustomTableView(QTableView):
    def __init__(self, parent=None, is_top_table=False):
        super().__init__(parent)
        self.search_widget = SearchWidget(self)
        self.search_widget.hide()
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        self.parent = parent  # Store reference to parent window
        self.is_top_table = is_top_table  # Flag to distinguish top tables
        
    def keyPressEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_F:
            pos = self.rect().topRight()
            self.search_widget.move(self.mapToGlobal(pos) - QPoint(self.search_widget.width(), 0))
            self.search_widget.show()
            self.search_widget.search_input.setFocus()
        elif (event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter) and self.search_widget.isVisible():
            self.search_widget.keyPressEvent(event)
        else:
            super().keyPressEvent(event)

    def show_context_menu(self, position):
        # Get the index at the clicked position
        index = self.indexAt(position)
        
        if index.isValid():  # Only show menu if we clicked on a valid cell
            # Create context menu
            context_menu = QMenu(self)
            
            # Add Sort submenu for all tables
            if self.model() and hasattr(self.model(), '_data'):
                sort_menu = context_menu.addMenu("Sort")
                
                # Get column names from the DataFrame
                columns = self.model()._data.columns.tolist()
                
                # Create submenus for each column
                for col in columns:
                    col_menu = sort_menu.addMenu("Sort by: " + str(col))
                    
                    # Add sorting options
                    asc_action = col_menu.addAction("Low to High")
                    desc_action = col_menu.addAction("High to Low")
                    
                    # Connect actions
                    asc_action.triggered.connect(lambda checked, c=col: self.sort_table(c, ascending=True))
                    desc_action.triggered.connect(lambda checked, c=col: self.sort_table(c, ascending=False))
            
            # Different menus for top and bottom tables
            if self == self.parent.data_table:  # Top table
                save_menu = context_menu.addMenu("Save As")
                save_csv = save_menu.addAction("CSV")
                save_excel = save_menu.addAction("Excel")
                
                # Connect the actions
                save_csv.triggered.connect(lambda: self.save_table_as('csv'))
                save_excel.triggered.connect(lambda: self.save_table_as('xlsx'))
            else:  # Bottom tables
                # Add Find action
                find_menu = context_menu.addMenu("Find")
                find_action = find_menu.addAction("Find Node/Edge")
                find_pair_action = find_menu.addAction("Find Pair")
                find_action.triggered.connect(lambda: self.handle_find_action(
                    index.row(), index.column(), 
                    self.model()._data.iloc[index.row(), index.column()]
                ))
                find_pair_action.triggered.connect(lambda: self.handle_find_action(
                    [index.row()], [0,1,2],
                    [self.model()._data.iloc[index.row(), 0], self.model()._data.iloc[index.row(), 1], self.model()._data.iloc[index.row(), 2]]
                    ))
                
                # Add separator
                context_menu.addSeparator()
                
                # Add Save As menu
                save_menu = context_menu.addMenu("Save As")
                save_csv = save_menu.addAction("CSV")
                save_excel = save_menu.addAction("Excel")
                
                # Connect the actions - ensure we're saving the active table
                save_csv.triggered.connect(lambda: self.parent.active_table.save_table_as('csv'))
                save_excel.triggered.connect(lambda: self.parent.active_table.save_table_as('xlsx'))

                if self == self.parent.selection_table:
                    set_action = context_menu.addAction("Swap with network table (also sets internal network properties - may affect related functions)")
                    set_action.triggered.connect(self.set_selection_to_active)
            
            # Show the menu at cursor position
            cursor_pos = QCursor.pos()
            context_menu.exec(cursor_pos)

    def sort_table(self, column, ascending=True):
        """Sort the table by the specified column."""
        try:
            # Get the current DataFrame
            df = self.model()._data
            
            # Create a copy of the DataFrame for sorting
            sorting_df = df.copy()
            
            # Check if column contains any numeric values
            has_numbers = pd.to_numeric(sorting_df[column], errors='coerce').notna().any()
            
            if has_numbers:
                # For columns with numbers, use numeric sorting
                sorted_index = sorting_df.sort_values(
                    by=column,
                    ascending=ascending,
                    na_position='last',
                    key=lambda x: pd.to_numeric(x, errors='coerce')
                ).index
            else:
                # For non-numeric columns, use regular sorting
                sorted_index = sorting_df.sort_values(
                    by=column,
                    ascending=ascending,
                    na_position='last'
                ).index
            
            # Use the sorted index on the original DataFrame
            sorted_df = df.loc[sorted_index]
            
            # Create new model with sorted DataFrame
            new_model = PandasModel(sorted_df)
            
            # Preserve any bold formatting from the old model
            if hasattr(self.model(), 'bold_cells'):
                new_model.bold_cells = self.model().bold_cells
            
            # Set the new model
            self.setModel(new_model)
            
            # Adjust column widths
            for col in range(new_model.columnCount(None)):
                self.resizeColumnToContents(col)
                
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error sorting table: {str(e)}"
            )

    def save_table_as(self, file_type):
        """Save the table data as either CSV or Excel file."""
        if not self.model():
            return
            
        df = self.model()._data
        
        # Get table name for the file dialog title
        if self == self.parent.data_table:
            table_name = "Statistics"
        elif self == self.parent.network_table:
            table_name = "Network"
        else:
            table_name = "Selection"
        
        # Get save file name
        file_filter = "CSV Files (*.csv)" if file_type == 'csv' else "Excel Files (*.xlsx)"
        filename, _ = QFileDialog.getSaveFileName(
            self,
            f"Save {table_name} Table As",
            "",
            file_filter
        )
        
        if filename:
            try:
                if file_type == 'csv':
                    # If user didn't type extension, add .csv
                    if not filename.endswith('.csv'):
                        filename += '.csv'
                    df.to_csv(filename, index=False)
                else:
                    # If user didn't type extension, add .xlsx
                    if not filename.endswith('.xlsx'):
                        filename += '.xlsx'
                    df.to_excel(filename, index=False)
                    
                QMessageBox.information(
                    self,
                    "Success",
                    f"{table_name} table successfully saved to {filename}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Failed to save file: {str(e)}"
                )

    def set_selection_to_active(self):
        """Set selection table to the active one"""

        try:

            # Confirm swap
            reply = QMessageBox.question(
                self,
                'Set Network',
                f'Are you sure you want to set the Selected Network as the Main Network? (Recommend Saving the Main Network first)',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )


            if reply == QMessageBox.StandardButton.Yes:

                df = self.model()._data
                old = self.parent.network_table.model()._data

                new_lists = [list(df.iloc[:, 0]), list(df.iloc[:, 1]), list(df.iloc[:, 2])]
                my_network.network_lists = new_lists

                model = PandasModel(my_network.network_lists)
                self.parent.network_table.setModel(model)
                # Adjust column widths to content
                for column in range(model.columnCount(None)):
                    self.parent.network_table.resizeColumnToContents(column)

                #move old model to selection
                new_lists = [list(old.iloc[:, 0]), list(old.iloc[:, 1]), list(old.iloc[:, 2])]
                model = PandasModel(new_lists)
                self.parent.selection_table.setModel(model)
                for column in range(model.columnCount(None)):
                    self.parent.selection_table.resizeColumnToContents(column)

        except Exception as e:
            print(f"Error setting new network: {e}")



    def handle_find_action(self, row, column, value):
        """Handle the Find action for bottom tables."""
        try:

            if type(column) is not list: #If highlighting one element
                value = int(value)
                
                # Get the currently active table
                active_table = self.parent.active_table
                
                # Determine if we're looking for a node or edge based on column
                if column < 2:  # First two columns are nodes

                    if my_network.node_centroids is None:
                        self.parent.show_centroid_dialog()

                    if value in my_network.node_centroids:
                        # Get centroid coordinates (Z, Y, X)
                        centroid = my_network.node_centroids[value]
                        # Set the active channel to nodes (0)
                        self.parent.set_active_channel(0)
                        # Toggle on the nodes channel if it's not already visible
                        if not self.parent.channel_visible[0]:
                            self.parent.channel_buttons[0].setChecked(True)
                            self.parent.toggle_channel(0)
                        # Navigate to the Z-slice
                        self.parent.slice_slider.setValue(int(centroid[0]))
                        print(f"Found node {value} at Z-slice {centroid[0]}")
                        self.parent.create_highlight_overlay(node_indices=[value])
                        self.parent.clicked_values['nodes'].append(value)
                        
                        # Highlight the value in both tables if it exists
                        self.highlight_value_in_table(self.parent.network_table, value, column)
                        self.highlight_value_in_table(self.parent.selection_table, value, column)
                    else:
                        print(f"Node {value} not found in centroids dictionary")
                        
                elif column == 2:  # Third column is edges
                    if value in my_network.edge_centroids:
                        if my_network.edge_centroids is None:
                            self.parent.show_centroid_dialog()
                        # Get centroid coordinates (Z, Y, X)
                        centroid = my_network.edge_centroids[value]
                        # Set the active channel to edges (1)
                        self.parent.set_active_channel(1)
                        # Toggle on the edges channel if it's not already visible
                        if not self.parent.channel_visible[1]:
                            self.parent.channel_buttons[1].setChecked(True)
                            self.parent.toggle_channel(1)
                        # Navigate to the Z-slice
                        self.parent.slice_slider.setValue(int(centroid[0]))
                        print(f"Found edge {value} at Z-slice {centroid[0]}")
                        self.parent.create_highlight_overlay(edge_indices=[value])
                        self.parent.clicked_values['edges'].append(value)

                        # Highlight the value in both tables if it exists
                        self.highlight_value_in_table(self.parent.network_table, value, column)
                        self.highlight_value_in_table(self.parent.selection_table, value, column)
                    else:
                        print(f"Edge {value} not found in centroids dictionary")
            else: #If highlighting paired elements
                if my_network.node_centroids is None:
                    self.parent.show_centroid_dialog()
                centroid1 = my_network.node_centroids[int(value[0])]
                centroid2 = my_network.node_centroids[int(value[1])]
                try:
                    centroid3 = my_network.edge_centroids[int(value[3])]
                except:
                    pass

                # Set the active channel to nodes (0)
                self.parent.set_active_channel(0)
                # Toggle on the nodes channel if it's not already visible
                if not self.parent.channel_visible[0]:
                    self.parent.channel_buttons[0].setChecked(True)
                    self.parent.toggle_channel(0)
                # Navigate to the Z-slice
                self.parent.slice_slider.setValue(int(centroid1[0]))
                print(f"Found node pair {value[0]} and {value[1]} at Z-slices {centroid1[0]} and {centroid2[0]}, respectively")
                try:
                    self.parent.create_highlight_overlay(node_indices=[int(value[0]), int(value[1])], edge_indices = int(value[2]))
                    self.parent.clicked_values['edges'].append(value[2])
                    self.parent.clicked_values['nodes'].append(value[0])
                    self.parent.clicked_values['nodes'].append(value[1])
                except:
                    self.parent.create_highlight_overlay(node_indices=[int(value[0]), int(value[1])])
                    self.parent.clicked_values['nodes'].append(value[0])
                    self.parent.clicked_values['nodes'].append(value[1])

        except (ValueError, TypeError) as e:
            print(f"Error processing value: {str(e)}")
            return


    def highlight_value_in_table(self, table, value, column):
        """Helper method to find and highlight a value in a specific table."""
        if table.model() is None:
            return
            
        df = table.model()._data
        
        if column < 2:  # Node
            col1_matches = df[df.columns[0]] == value
            col2_matches = df[df.columns[1]] == value
            all_matches = col1_matches | col2_matches
        else:  # Edge
            all_matches = df[df.columns[2]] == value
        
        if all_matches.any():
            match_indices = all_matches[all_matches].index.tolist()
            row_idx = match_indices[0]
            
            # Only scroll and select if this is the active table
            if table == self.parent.active_table:
                # Create index and scroll to it
                model_index = table.model().index(row_idx, 0)
                table.scrollTo(model_index)
                
                # Select the row
                table.clearSelection()
                table.selectRow(row_idx)
                table.setCurrentIndex(model_index)
            
            # Update bold formatting
            table.model().set_bold_value(value, column < 2 and 0 or 1)


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        if data is None:
            # Create an empty DataFrame with default columns
            import pandas as pd
            data = pd.DataFrame(columns=['Node 1A', 'Node 1B', 'Edge 1C'])
        elif type(data) == list:
            data = self.lists_to_dataframe(data[0], data[1], data[2], column_names=['Node 1A', 'Node 1B', 'Edge 1C'])
        self._data = data
        self.bold_cells = set()
        self.highlighted_cells = set()

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        elif role == Qt.ItemDataRole.FontRole:
            # Get the actual index from the DataFrame for this row
            df_index = self._data.index[index.row()]
            if (df_index, index.column()) in self.bold_cells or (index.row(), index.column()) in self.highlighted_cells:
                font = QFont()
                font.setBold(True)
                return font
        elif role == Qt.ItemDataRole.BackgroundRole:
            if (index.row(), index.column()) in self.highlighted_cells:
                return QColor(255, 255, 0, 70)  # Light yellow background
        return None

    def highlight_cell(self, row, col):
        """Highlight a specific cell"""
        self.highlighted_cells.clear()  # Clear previous highlights
        self.highlighted_cells.add((row, col))
        # Emit signal to refresh the view
        self.layoutChanged.emit()

    def set_bold_value(self, value, active_channel=0):
        """Set bold formatting for cells containing this value in relevant columns based on active channel"""
        # Clear previous bold cells
        self.bold_cells.clear()
        self.highlighted_cells.clear()  # Also clear highlighted cells
        
        if active_channel == 0:
            # For nodes, search first two columns
            for col in [0, 1]:
                matches = self._data.iloc[:, col] == value
                for idx in matches[matches].index:
                    self.bold_cells.add((idx, col))
        elif active_channel == 1:
            # For edges, only search third column
            matches = self._data.iloc[:, 2] == value
            for idx in matches[matches].index:
                self.bold_cells.add((idx, 2))
        
        # Emit signal to refresh the view
        self.layoutChanged.emit()

    @staticmethod
    def lists_to_dataframe(list1, list2, list3, column_names=['Column1', 'Column2', 'Column3']):
        """
        Convert three lists into a pandas DataFrame with specified column names.
        
        Parameters:
        list1, list2, list3: Lists of equal length
        column_names: List of column names (default provided)
        
        Returns:
        pandas.DataFrame: DataFrame with three columns
        """
        df = pd.DataFrame({
            column_names[0]: list1,
            column_names[1]: list2,
            column_names[2]: list3
        })
        return df

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Orientation.Vertical:
                return str(self._data.index[section])
        return None


# Tables related for the data tables:

class TabCornerWidget(QWidget):
    """Widget for the corner of the tab widget, can be used to add controls"""
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

class TabButton(QPushButton):
    """Custom close button for tabs"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(16, 16)
        self.setText("×")
        self.setStyleSheet("""
            QPushButton {
                border: none;
                color: gray;
                font-weight: bold;
                padding: 0px;
            }
            QPushButton:hover {
                color: red;
            }
        """)

class TabbedDataWidget(QTabWidget):
    """Widget that manages multiple data tables in tabs"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setTabsClosable(True)
        self.setMovable(True)
        self.setElideMode(Qt.TextElideMode.ElideRight)
        
        # Store tables with their associated names
        self.tables = {}
        self.tabCloseRequested.connect(self.close_tab)
        
        # Set corner widget
        self.setCornerWidget(TabCornerWidget(self))
        
    def add_table(self, name, table_widget, switch_to=True):
        """Add a new table with the given name"""
        if name in self.tables:
            # If tab already exists, update its content
            idx = self.indexOf(self.tables[name])
            self.removeTab(idx)
            
        # Create a new CustomTableView with is_top_table=True
        new_table = CustomTableView(self.parent_window, is_top_table=True)
        
        # If we received a model or table_widget, use its model
        if isinstance(table_widget, QAbstractTableModel):
            new_table.setModel(table_widget)
        elif isinstance(table_widget, QTableView):
            new_table.setModel(table_widget.model())
        
        self.tables[name] = new_table
        idx = self.addTab(new_table, name)
        
        if switch_to:
            self.setCurrentIndex(idx)
            
        # Update parent's data_table reference
        if self.parent_window:
            self.parent_window.data_table = new_table
            
    def close_tab(self, index):
        """Close the tab at the given index"""
        widget = self.widget(index)
        # Find and remove the table name from our dictionary
        name_to_remove = None
        for name, table in self.tables.items():
            if table == widget:
                name_to_remove = name
                break
                
        if name_to_remove:
            del self.tables[name_to_remove]
            
        self.removeTab(index)
        
        # Update parent's data_table reference to current table
        if self.parent_window and self.count() > 0:
            self.parent_window.data_table = self.currentWidget()
            
    def clear_all_tabs(self):
        """Remove all tabs"""
        while self.count() > 0:
            self.close_tab(0)
            
    def get_current_table(self):
        """Get the currently active table"""
        return self.currentWidget()


# IMAGE MENU RELATED

class PropertiesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Properties")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.xy_scale = QLineEdit(f"{my_network.xy_scale}")
        layout.addRow("xy_scale:", self.xy_scale)

        self.z_scale = QLineEdit(f"{my_network.z_scale}")
        layout.addRow("z_scale:", self.z_scale)

        layout.addRow("Note:", QLabel(f"The below properties reflect what properties are being held in RAM. \nDisabling their button will reset the property and clear them from RAM. \nEnabling their button when nothing was set beforehand will not do anything.\nPleaes use file -> load to load specific elements."))


        self.nodes = QPushButton("Nodes")
        self.nodes.setCheckable(True)
        self.nodes.setChecked(self.check_checked(my_network.nodes))
        layout.addRow("Nodes Status", self.nodes)

        self.edges = QPushButton("edges")
        self.edges.setCheckable(True)
        self.edges.setChecked(self.check_checked(my_network.edges))
        layout.addRow("Edges Status", self.edges)

        self.network_overlay = QPushButton("overlay 1")
        self.network_overlay.setCheckable(True)
        self.network_overlay.setChecked(self.check_checked(my_network.network_overlay))
        layout.addRow("Overlay 1 Status", self.network_overlay)

        self.id_overlay = QPushButton("overlay 2")
        self.id_overlay.setCheckable(True)
        self.id_overlay.setChecked(self.check_checked(my_network.id_overlay))
        layout.addRow("Overlay 2 Status", self.id_overlay)

        self.search_region = QPushButton("search region")
        self.search_region.setCheckable(True)
        self.search_region.setChecked(self.check_checked(my_network.search_region))
        layout.addRow("Node Search Region Status", self.search_region)

        self.network = QPushButton("Network")
        self.network.setCheckable(True)
        self.network.setChecked(self.check_checked(my_network.network))
        layout.addRow("Network Status", self.network)

        # Add Run button
        run_button = QPushButton("Enter")
        run_button.clicked.connect(self.run_properties)
        layout.addWidget(run_button)

    def check_checked(self, ques):

        if ques is None:
            return False
        else:
            return True


    def run_properties(self):

        try:
            
            # Get amount
            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else 1
            except ValueError:
                xy_scale = 1

            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else 1
            except ValueError:
                z_scale = 1

            nodes = not self.nodes.isChecked()
            edges = not self.edges.isChecked()
            network_overlay = not self.network_overlay.isChecked()
            id_overlay = not self.id_overlay.isChecked()
            search_region = not self.search_region.isChecked()
            network = not self.network.isChecked()

            self.parent().reset(nodes = nodes, edges = edges, network_overlay = network_overlay, id_overlay = id_overlay, search_region = search_region, network = network, xy_scale = xy_scale, z_scale = z_scale)
            
            self.accept()

        except Exception as e:
            print(f"Error: {e}")

class BrightnessContrastDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Brightness/Contrast Controls")
        self.setModal(False)  # Allows interaction with main window while open
        
        layout = QVBoxLayout(self)
        
        # Create range sliders for each channel
        self.brightness_sliders = []
        self.min_inputs = []  # Store min value inputs
        self.max_inputs = []  # Store max value inputs
        
        for i in range(4):
            channel_widget = QWidget()
            channel_layout = QVBoxLayout(channel_widget)
            
            # Add label
            label = QLabel(f"Channel {i+1} Brightness/Contrast")
            channel_layout.addWidget(label)
            
            # Create slider control container
            slider_container = QWidget()
            slider_layout = QHBoxLayout(slider_container)
            slider_layout.setContentsMargins(0, 0, 0, 0)
            
            # Create min value input
            min_input = QLineEdit()
            min_input.setFixedWidth(50)  # Make input fields compact
            min_input.setText("0")
            self.min_inputs.append(min_input)
            
            # Create range slider
            slider = QRangeSlider(Qt.Orientation.Horizontal)
            slider.setMinimum(0)
            slider.setMaximum(255)
            slider.setValue((0, 255))
            self.brightness_sliders.append(slider)
            
            # Create max value input
            max_input = QLineEdit()
            max_input.setFixedWidth(50)
            max_input.setText("255")
            self.max_inputs.append(max_input)
            
            # Add all components to slider container
            slider_layout.addWidget(min_input)
            slider_layout.addWidget(slider, stretch=1)  # Give slider stretch priority
            slider_layout.addWidget(max_input)
            
            channel_layout.addWidget(slider_container)
            layout.addWidget(channel_widget)
            
            # Connect signals
            slider.valueChanged.connect(lambda values, ch=i: self.on_slider_change(ch, values))
            min_input.editingFinished.connect(lambda ch=i: self.on_min_input_change(ch))
            max_input.editingFinished.connect(lambda ch=i: self.on_max_input_change(ch))
            
    def on_slider_change(self, channel, values):
        """Update text inputs when slider changes"""
        min_val, max_val = values
        self.min_inputs[channel].setText(str(min_val))
        self.max_inputs[channel].setText(str(max_val))
        self.parent().update_brightness(channel, values)
        
    def on_min_input_change(self, channel):
        """Handle changes to minimum value input"""
        try:
            min_val = self.parse_input_value(self.min_inputs[channel].text())
            current_min, current_max = self.brightness_sliders[channel].value()
            
            if min_val < 0:
                min_val = 0
            # Ensure min doesn't exceed max
            min_val = min(min_val, current_max - 1)
            
            # Update slider and text input
            self.brightness_sliders[channel].setValue((min_val, current_max))
            self.min_inputs[channel].setText(str(min_val))
            
        except ValueError:
            # Reset to current slider value if input is invalid
            current_min, _ = self.brightness_sliders[channel].value()
            self.min_inputs[channel].setText(str(current_min))
            
    def on_max_input_change(self, channel):
        """Handle changes to maximum value input"""
        try:
            max_val = self.parse_input_value(self.max_inputs[channel].text())
            current_min, current_max = self.brightness_sliders[channel].value()
            
            if max_val > 255:
                max_val = 255
            # Ensure max doesn't go below min
            max_val = max(max_val, current_min + 1)
            
            # Update slider and text input
            self.brightness_sliders[channel].setValue((current_min, max_val))
            self.max_inputs[channel].setText(str(max_val))
            
        except ValueError:
            # Reset to current slider value if input is invalid
            _, current_max = self.brightness_sliders[channel].value()
            self.max_inputs[channel].setText(str(current_max))
            
    def parse_input_value(self, text):
        """Parse and validate input value"""
        try:
            # Convert to float first to handle decimal inputs
            value = float(text)
            # Round to nearest integer
            value = int(round(value))
            # Clamp between 0 and 255
            return max(0, min(255, value))
        except ValueError:
            raise ValueError("Invalid input")

class ColorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Channel Colors")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # Store the combo boxes to access their values later
        self.color_combos = []
        
        # Create a dropdown for each channel
        for i in range(4):
            combo = QComboBox()
            # Add all color options from parent's color dictionary
            combo.addItems(self.parent().color_dictionary.keys())
            
            # Set current selection to match current color
            current_color = self.parent().base_colors[i]
            # Find the key for this color value in the dictionary
            current_key = [k for k, v in self.parent().color_dictionary.items() 
                         if v == current_color][0]
            combo.setCurrentText(current_key)
            
            # Add to layout with appropriate label
            layout.addRow(f"Channel {i+1} ({self.parent().channel_names[i]}):", combo)
            self.color_combos.append(combo)
        
        # Add Run button
        run_button = QPushButton("Apply Colors")
        run_button.clicked.connect(self.update_colors)
        layout.addWidget(run_button)

    def update_colors(self):
        """Update the colors in the parent class and refresh display"""
        # For each channel, check if color has changed
        for i, combo in enumerate(self.color_combos):
            new_color = self.parent().color_dictionary[combo.currentText()]
            if new_color != self.parent().base_colors[i]:
                self.parent().base_colors[i] = new_color
        
        # Update the display
        self.parent().update_display()
        self.accept()    

class Show3dDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Display Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.downsample = QLineEdit("1")
        layout.addRow("Downsample Factor (Expect Slowness on Large Images):", self.downsample)

        # Network Overlay checkbox (default True)
        self.overlay = QPushButton("Overlay 1")
        self.overlay.setCheckable(True)
        self.overlay.setChecked(True)
        layout.addRow("Include Overlay 1?", self.overlay)
        
        # Add Run button
        run_button = QPushButton("Show 3D")
        run_button.clicked.connect(self.show_3d)
        layout.addWidget(run_button)


    def show_3d(self):

        try:
            
            # Get amount
            try:
                downsample = float(self.downsample.text()) if self.downsample.text() else 1
            except ValueError:
                downsample = 1

            overlay = self.overlay.isChecked()
            if overlay:
        
                # Example analysis plot
                my_network.show_3D(my_network.network_overlay, downsample)
            else:
                my_network.show_3D(down_factor = downsample)
            
            self.accept()

        except Exception as e:
            print(f"Error: {e}")


class NetOverlayDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Generate Network Overlay?")
        self.setModal(True)

        layout = QFormLayout(self)

        # Add Run button
        run_button = QPushButton("Generate (Will go to Overlay 1)")
        run_button.clicked.connect(self.netoverlay)
        layout.addWidget(run_button)

    def netoverlay(self):

        try:

            if my_network.node_centroids is None:

                self.parent().show_centroid_dialog()

            if my_network.node_centroids is None:
                return

            my_network.network_overlay = my_network.draw_network()

            self.parent().load_channel(2, channel_data = my_network.network_overlay, data = True)

            self.accept()

        except Exception as e:

            print(f"Error with Overlay Generation: {e}")

class SearchOverlayDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Generate Search Region Overlay?")
        self.setModal(True)

        layout = QFormLayout(self)

        # Add Run button
        run_button = QPushButton("Generate (Will go to Overlay 2)")
        run_button.clicked.connect(self.searchoverlay)
        layout.addWidget(run_button)

    def searchoverlay(self):

        try:

            my_network.id_overlay = my_network.search_region

            self.parent().load_channel(3, channel_data = my_network.search_region, data = True)

            self.accept()

        except Exception as e:

            print(f"Error with Overlay Generation: {e}")

class IdOverlayDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Generate ID Overlay?")
        self.setModal(True)

        layout = QFormLayout(self)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Nodes", "Edges"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # Add Run button
        run_button = QPushButton("Generate (Will go to Overlay 2)")
        run_button.clicked.connect(self.idoverlay)
        layout.addWidget(run_button)

    def idoverlay(self):

        accepted_mode = self.mode_selector.currentIndex()

        if accepted_mode == 0:

            if my_network.node_centroids is None:

                self.parent().show_centroid_dialog()

            if my_network.node_centroids is None:
                return

        elif accepted_mode == 1:

            if my_network.edge_centroids is None:

                self.parent().show_centroid_dialog()

            if my_network.edge_centroids is None:
                return

        if accepted_mode == 0:

            my_network.id_overlay = my_network.draw_node_indices()

        elif accepted_mode == 1:

            my_network.id_overlay = my_network.draw_edge_indices()


        self.parent().load_channel(3, channel_data = my_network.id_overlay, data = True)

        self.accept()

class WhiteDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Generate White Overlay?")
        self.setModal(True)

        layout = QFormLayout(self)

        # Add Run button
        run_button = QPushButton("Generate (Will go to Overlay 2)")
        run_button.clicked.connect(self.white_overlay)
        layout.addWidget(run_button)

    def white_overlay(self):

        try:

            try:
                overlay = np.ones_like(my_network.nodes).astype(np.uint8) * 255
            except:
                overlay = np.ones_like(my_network.edges).astype(np.uint8) * 255
            finally:
                my_network.id_overlay = overlay

                self.parent().load_channel(3, channel_data = my_network.id_overlay, data = True)

                self.accept()

        except Exception as e:
            print(f"Error making white background: {e}")


class ShuffleDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Shuffle Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        layout.addRow(QLabel("Swap: "))

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Nodes", "Edges", "Overlay 1", "Overlay 2", "Highlight Overlay"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Channel 1:", self.mode_selector)

        layout.addRow(QLabel("With: "))

        # Add mode selection dropdown
        self.target_selector = QComboBox()
        self.target_selector.addItems(["Nodes", "Edges", "Overlay 1", "Overlay 2", 'Highlight Overlay'])
        self.target_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Channel 2:", self.target_selector)

        # Add Run button
        run_button = QPushButton("swap")
        run_button.clicked.connect(self.swap)
        layout.addWidget(run_button)

    def swap(self):

        try:

            accepted_mode = self.mode_selector.currentIndex()
            accepted_target = self.target_selector.currentIndex()

            if accepted_mode == 4:
                active_data = self.parent().highlight_overlay
            else:
                active_data = self.parent().channel_data[accepted_mode]

            if accepted_target == 4:
                target_data = self.parent().highlight_overlay
            else:
                target_data = self.parent().channel_data[accepted_target]


            if accepted_mode == 4:

                self.parent().highlight_overlay = n3d.binarize(target_data)
            else:
                self.parent().load_channel(accepted_mode, channel_data = target_data, data = True)



            if accepted_target == 4:

                self.parent().highlight_overlay = n3d.binarize(active_data)
            else:
                self.parent().load_channel(accepted_target, channel_data = active_data, data = True)


            self.parent().update_display()

            self.accept()

        except Exception as e:
            print(f"Error swapping: {e}")









# ANALYZE MENU RELATED

class NetShowDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Display Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # geo checkbox (default True)
        self.geo_layout = QPushButton("geo_layout")
        self.geo_layout.setCheckable(True)
        self.geo_layout.setChecked(False)
        layout.addRow("Use Geometric Layout:", self.geo_layout)
        
        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Default", "Community Coded (Uses current communities or label propogation by default if no communities have been found)", "Community Coded (Redo Label Propogation Algorithm)", "Community Coded (Redo Louvain Algorithm)", "Node ID Coded"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # weighted checkbox (default True)
        self.weighted = QPushButton("weighted")
        self.weighted.setCheckable(True)
        self.weighted.setChecked(True)
        layout.addRow("Use Weighted Network (Only for community graphs):", self.weighted)

        # Optional saving:
        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Does not save when empty")
        layout.addRow("Output Directory:", self.directory)
        
        # Add Run button
        run_button = QPushButton("Show Network")
        run_button.clicked.connect(self.show_network)
        layout.addWidget(run_button)
    
    def show_network(self):
        # Get parameters and run analysis
        geo = self.geo_layout.isChecked()
        if geo:
            if my_network.node_centroids is None:
                self.parent().show_centroid_dialog()
        accepted_mode = self.mode_selector.currentIndex()  # Convert to 1-based index
        # Get directory (None if empty)
        directory = self.directory.text() if self.directory.text() else None

        weighted = self.weighted.isChecked()

        try:
            if accepted_mode == 0:
                my_network.show_network(geometric=geo, directory = directory)
            elif accepted_mode == 1:
                my_network.show_communities_flex(geometric=geo, directory = directory, weighted = weighted, partition = my_network.communities)
                self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')
            elif accepted_mode == 2:
                my_network.show_communities_flex(geometric=geo, directory = directory, weighted = weighted, partition = my_network.communities, style = 0)
                self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')
            elif accepted_mode ==3:
                my_network.show_communities_flex(geometric=geo, directory = directory, weighted = weighted, partition = my_network.communities, style = 1)
                self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID')
            elif accepted_mode == 4:
                my_network.show_identity_network(geometric=geo, directory = directory)
            
            self.accept()
        except Exception as e:
            print(f"Error showing network: {e}")
            import traceback
            print(traceback.format_exc())

class PartitionDialog(QDialog):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Partition Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        # weighted checkbox (default True)
        self.weighted = QPushButton("weighted")
        self.weighted.setCheckable(True)
        self.weighted.setChecked(True)
        layout.addRow("Use Weighted Network:", self.weighted)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Label Propogation", "Louvain"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # stats checkbox (default True)
        self.stats = QPushButton("Stats")
        self.stats.setCheckable(True)
        self.stats.setChecked(True)
        layout.addRow("Community Stats:", self.stats)

        # Add Run button
        run_button = QPushButton("Partition")
        run_button.clicked.connect(self.partition)
        layout.addWidget(run_button)

    def partition(self):

        accepted_mode = self.mode_selector.currentIndex()
        weighted = self.weighted.isChecked()
        dostats = self.stats.isChecked()

        my_network.communities = None

        try:
            stats = my_network.community_partition(weighted = weighted, style = accepted_mode, dostats = dostats)
            print(f"Discovered communities: {my_network.communities}")

            self.parent().format_for_upperright_table(my_network.communities, 'NodeID', 'CommunityID', title = 'Community Partition')

            if len(stats.keys()) > 0:
                self.parent().format_for_upperright_table(stats, title = 'Community Stats')

            self.accept()

        except Exception as e:
            print(f"Error creating communities: {e}")

class RadialDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Radial Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        self.distance = QLineEdit("50")
        layout.addRow("Bucket Distance for Searching For Node Neighbors (automatically scaled by xy and z scales):", self.distance)

        self.directory = QLineEdit("")
        layout.addRow("Output Directory:", self.directory)

        # Add Run button
        run_button = QPushButton("Get Radial Distribution")
        run_button.clicked.connect(self.radial)
        layout.addWidget(run_button)

    def radial(self):

        distance = float(self.distance.text()) if self.distance.text().strip() else 50

        directory = str(self.distance.text()) if self.directory.text().strip() else None

        if my_network.node_centroids is None:
            self.parent().show_centroid_dialog()

        radial = my_network.radial_distribution(distance, directory = directory)

        self.parent().format_for_upperright_table(radial, 'Radial Distance From Any Node', 'Average Number of Neighboring Nodes', title = 'Radial Distribution Analysis')

        self.accept()

class DegreeDistDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Degree Distribution Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        self.directory = QLineEdit("")
        layout.addRow("Output Directory:", self.directory)

        # Add Run button
        run_button = QPushButton("Get Degree Distribution")
        run_button.clicked.connect(self.degreedist)
        layout.addWidget(run_button)

    def degreedist(self):

        try:

            directory = str(self.distance.text()) if self.directory.text().strip() else None

            degrees = my_network.degree_distribution(directory = directory)


            self.parent().format_for_upperright_table(degrees, 'Degree (k)', 'Proportion of nodes with degree (p(k))', title = 'Degree Distribution Analysis')

            self.accept()

        except Excpetion as e:
            print(f"An error occurred: {e}")

class NeighborIdentityDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle(f"Neighborhood Identity Distribution Parameters \n(Note - the same node is not included more than once as a neighbor even if it borders multiple nodes of the root ID)")
        self.setModal(True)

        layout = QFormLayout(self)

        if my_network.node_identities is not None:
            self.root = QComboBox()
            self.root.addItems(list(set(my_network.node_identities.values())))  
            self.root.setCurrentIndex(0)
            layout.addRow("Root Identity to Search for Neighbor's IDs (search uses nodes of this ID, finds what IDs they connect to", self.root)
        else:
            self.root = None

        self.directory = QLineEdit("")
        layout.addRow("Output Directory:", self.directory)

        self.mode = QComboBox()
        self.mode.addItems(["From Network - Based on Absolute Connectivity", "Use Labeled Nodes - Based on Morphological Neighborhood Densities"])
        self.mode.setCurrentIndex(0)
        layout.addRow("Mode", self.mode)

        self.search = QLineEdit("")
        layout.addRow("Search Radius (Ignore if using network):", self.search)

        # Add Run button
        run_button = QPushButton("Get Neighborhood Identity Distribution")
        run_button.clicked.connect(self.neighborids)
        layout.addWidget(run_button)

    def neighborids(self):

        try:

            try:
                root = self.root.currentText()
            except:
                pass

            directory = self.directory.text() if self.directory.text().strip() else None

            mode = self.mode.currentIndex()

            search = float(self.search.text()) if self.search.text().strip() else 0


            result, result2, title1, title2, densities = my_network.neighborhood_identities(root = root, directory = directory, mode = mode, search = search)

            self.parent().format_for_upperright_table(result, 'Node Identity', 'Amount', title = title1)
            self.parent().format_for_upperright_table(result2, 'Node Identity', 'Proportion', title = title2)

            if mode == 1:

                self.parent().format_for_upperright_table(densities, 'Node Identity', 'Density in search/density total', title = f'Clustering Factor of Node Identities with {search} from nodes {root}')


            self.accept()
        except Exception as e:
            print(f"Error: {e}")








class RandomDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Degree Distribution Parameters")
        self.setModal(True)

        layout = QFormLayout(self)


        # stats checkbox (default True)
        self.weighted = QPushButton("weighted")
        self.weighted.setCheckable(True)
        self.weighted.setChecked(True)
        layout.addRow("Allow Random Network to be weighted? (Whether or not edges can be repeatedly assigned between the same set of nodes to increase their weights, or if they must always find a new partner):", self.weighted)
        

        # Add Run button
        run_button = QPushButton("Get Random Network (Will go in Selection Table)")
        run_button.clicked.connect(self.random)
        layout.addWidget(run_button)

    def random(self):

        weighted = self.weighted.isChecked()

        _, df = my_network.assign_random(weighted = weighted)

        # Create new model with filtered DataFrame and update selection table
        new_model = PandasModel(df)
        self.parent().selection_table.setModel(new_model)
        
        # Switch to selection table
        self.parent().selection_button.click()

        self.accept()



class InteractionDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Partition Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        layout.addRow("Note:", QLabel(f"This is best done on original node/edge masks (nodes can be labeled first but edges will be significantly altered by labeling with Calculate All)\nConsider skeletonizing your edge mask first for increased standardization"))


        self.node_search = QLineEdit("0")
        layout.addRow("node_search:", self.node_search)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Include Regions Inside Node", "Exclude Regions Inside Node"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # Add Run button
        run_button = QPushButton("Calculate")
        run_button.clicked.connect(self.interaction)
        layout.addWidget(run_button)

    def interaction(self):

        try:

            accepted_mode = self.mode_selector.currentIndex()

            try:
                node_search = float(self.node_search.text()) if self.node_search.text() else 0
            except ValueError:
                node_search = 0

            result = my_network.interactions(search = node_search, cores = accepted_mode)

            self.parent().format_for_upperright_table(result, 'Node ID', ['Volume of Nearby Edge (Scaled)', 'Volume of Search Region'], title = 'Node/Edge Interactions')

            self.accept()

        except Exception as e:

            print(f"Error finding interactions: {e}")


class DegreeDialog(QDialog):


    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Degree Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        layout.addRow("Note:", QLabel(f"This operation will be executed on the image in 'Active Image', unless it is set to edges in which case it will use the nodes. \n (This is because you may want to run it on isolated nodes that have been placed in the Overlay channels)\nWe can draw optional overlays to Overlay 2 as described below:"))

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Just make table", "Draw degree of node as overlay (literally draws 1, 2, 3, etc... faster)", "Label nodes by degree (nodes will take on the value 1, 2, 3, etc, based on their degree, to export for array based analysis... slower)"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        self.mask_limiter = QLineEdit("1")
        layout.addRow("Masks smaller high degree proportion of nodes (ignore if only returning degrees)", self.mask_limiter)

        self.down_factor = QLineEdit("1")
        layout.addRow("down_factor (for speeding up overlay generation - ignore if only returning degrees:", self.down_factor)

        # Add Run button
        run_button = QPushButton("Get Degrees")
        run_button.clicked.connect(self.degs)
        layout.addWidget(run_button)

    def degs(self):

        try:

            accepted_mode = self.mode_selector.currentIndex()

            try:
                down_factor = float(self.down_factor.text()) if self.down_factor.text() else 1
            except ValueError:
                down_factor = 1

            try:
                mask_limiter = float(self.mask_limiter.text()) if self.mask_limiter.text() else 1
            except ValueError:
                mask_limiter = 1

            if self.parent().active_channel == 1:
                active_data = self.parent().channel_data[0]
            else:
                # Get the active channel data from parent
                active_data = self.parent().channel_data[self.parent().active_channel]
                if active_data is None:
                    raise ValueError("No active image selected")

            if my_network.node_centroids is None and accepted_mode > 0:
                self.parent().show_centroid_dialog()
                if my_network.node_centroids is None:
                    accepted_mode == 0
                    print("Error retrieving centroids")

            original_shape = copy.deepcopy(active_data.shape)


            if mask_limiter < 1 and accepted_mode != 0:

                if len(np.unique(active_data)) < 3:
                    active_data, _ = n3d.label_objects(active_data)

                node_list = list(my_network.network.nodes)
                node_dict = {}

                for node in node_list:
                    node_dict[node] = (my_network.network.degree(node))

                # Calculate the number of top proportion% entries
                num_items = len(node_dict)
                num_top_10_percent = max(1, int(num_items * mask_limiter))  # Ensure at least one item

                # Sort the dictionary by values in descending order and get the top 10%
                sorted_items = sorted(node_dict.items(), key=lambda item: item[1], reverse=True)
                top_10_percent_items = sorted_items[:num_top_10_percent]

                # Extract the keys from the top proportion% items
                top_10_percent_keys = [key for key, value in top_10_percent_items]

                mask = np.isin(active_data, top_10_percent_keys)
                nodes = mask * active_data
                new_centroids = {}
                for node in my_network.node_centroids:
                    if node in top_10_percent_keys:
                        new_centroids[node] = my_network.node_centroids[node]
                del mask

                temp_network = n3d.Network_3D(nodes = nodes, node_centroids = new_centroids, network = my_network.network, network_lists = my_network.network_lists)

                result, nodes = temp_network.get_degrees(called = True, no_img = accepted_mode, down_factor = down_factor)

            else:
                temp_network = n3d.Network_3D(nodes = active_data, node_centroids = my_network.node_centroids, network = my_network.network, network_lists = my_network.network_lists)

                result, nodes = temp_network.get_degrees(called = True, no_img = accepted_mode, down_factor = down_factor)



            self.parent().format_for_upperright_table(result, 'Node ID', 'Degree', title = 'Degrees of nodes')

            if nodes.shape != original_shape:

                nodes = n3d.upsample_with_padding(nodes, down_factor, original_shape)

            if accepted_mode > 0:
                self.parent().load_channel(3, channel_data = nodes, data = True)


            self.accept()

        except Exception as e:

            import traceback
            print(traceback.format_exc())

            print(f"Error finding degrees: {e}")


class HubDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Hub Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        layout.addRow("Note:", QLabel(f"Finds hubs, which are nodes in the network that have the shortest number of steps to the other nodes\nWe can draw optional overlays to Overlay 2 as described below:"))

        # Overlay checkbox (default True)
        self.overlay = QPushButton("Overlay")
        self.overlay.setCheckable(True)
        self.overlay.setChecked(True)
        layout.addRow("Make Overlay?:", self.overlay)


        self.proportion = QLineEdit("0.15")
        layout.addRow("Proportion of most connected hubs to keep (1 would imply returning entire network)", self.proportion)


        # Add Run button
        run_button = QPushButton("Get hubs")
        run_button.clicked.connect(self.hubs)
        layout.addWidget(run_button)

    def hubs(self):

        try:

            try:
                proportion = float(self.proportion.text()) if self.proportion.text() else 1
            except ValueError:
                proportion = 1

            overlay = self.overlay.isChecked()

            result, img = my_network.isolate_hubs(proportion = proportion, retimg = overlay)

            hub_dict = {}

            for node in result:
                hub_dict[node] = my_network.network.degree(node)

            self.parent().format_for_upperright_table(hub_dict, 'NodeID', 'Degree', title = f'Upper {proportion} Hub Nodes')

            if img is not None:

                self.parent().load_channel(3, channel_data = img, data = True)


            self.accept()

        except Exception as e:

            import traceback
            print(traceback.format_exc())

            print(f"Error finding hubs: {e}")



class MotherDialog(QDialog):


    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Mother Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        layout.addRow("Note:", QLabel(f"Mother nodes are those that exist between communities. \nWe can draw optional overlays to Overlay 1 as described below:"))

        # Overlay checkbox (default False)
        self.overlay = QPushButton("Overlay")
        self.overlay.setCheckable(True)
        self.overlay.setChecked(False)
        layout.addRow("Make Overlay?:", self.overlay)

        # Add Run button
        run_button = QPushButton("Get Mothers")
        run_button.clicked.connect(self.mothers)
        layout.addWidget(run_button)

    def mothers(self):

        try:

            overlay = self.overlay.isChecked()

            if my_network.node_centroids is None:
                self.parent().show_centroid_dialog()
                if my_network.node_centroids is None:
                    print("Error finding centroids")
                    overlay = False

            if my_network.communities is None:
                self.parent().show_partition_dialog()
                if my_network.communities is None:
                    return

            if not overlay:
                G = my_network.isolate_mothers(self, louvain = my_network.communities, ret_nodes = True, called = True)
            else:
                G, result = my_network.isolate_mothers(self, louvain = my_network.communities, ret_nodes = False, called = True)
                self.parent().load_channel(2, channel_data = result, data = True)

            degree_dict = {}

            for node in G.nodes():
                degree_dict[node] = my_network.network.degree(node)

            self.parent().format_for_upperright_table(degree_dict, 'Mother ID', 'Degree', title = 'Mother Nodes')


            self.accept()

        except Exception as e:

            print(f"Error finding mothers: {e}")


class CodeDialog(QDialog):

    def __init__(self, parent=None, sort = 'Community'):

        super().__init__(parent)
        self.setWindowTitle(f"{sort} Code Parameters (Will go to Overlay2)")
        self.setModal(True)

        layout = QFormLayout(self)

        self.sort = sort

        self.down_factor = QLineEdit("")
        layout.addRow("down_factor (for speeding up overlay generation - optional):", self.down_factor)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Color Coded", "Grayscale Coded"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)


        # Add Run button
        run_button = QPushButton(f"{sort} Code")
        run_button.clicked.connect(self.code)
        layout.addWidget(run_button)

    def code(self):

        try:

            mode = self.mode_selector.currentIndex()

            down_factor = float(self.down_factor.text()) if self.down_factor.text().strip() else None


            if self.sort == 'Community':
                if my_network.communities is None:
                    self.parent().show_partition_dialog()
                    if my_network.communities is None:
                        return
            elif my_network.node_identities is None:
                print("Node identities are not set")
                return

            if self.sort == 'Community':
                if mode == 0:
                    image, output = my_network.extract_communities(down_factor = down_factor)
                elif mode == 1:
                    image, output = my_network.extract_communities(color_code = False, down_factor = down_factor)
            else:
                if mode == 0:
                    image, output = my_network.extract_communities(down_factor = down_factor, identities = True)
                elif mode == 1:
                    image, output = my_network.extract_communities(color_code = False, down_factor = down_factor, identities = True)

            self.parent().format_for_upperright_table(output, f'{self.sort} Id', f'Encoding Val: {self.sort}', 'Legend')


            self.parent().load_channel(3, image, True)
            self.accept()

        except Exception as e:
            print(f"An error has occurred: {e}")
            import traceback
            print(traceback.format_exc())





# PROCESS MENU RELATED:


class ResizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resize Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        self.resize = QLineEdit()
        self.resize.setPlaceholderText("Will Override Below")
        layout.addRow("Resize Factor (All Dimensions):", self.resize)
        self.zsize = QLineEdit("1")
        layout.addRow("Resize Z Factor:", self.zsize)
        self.ysize = QLineEdit("1")
        layout.addRow("Resize Y Factor:", self.ysize)
        self.xsize = QLineEdit("1")
        layout.addRow("Resize X Factor:", self.xsize)


        # cubic checkbox (default False)
        self.cubic = QPushButton("Use Cubic Resize? (Will alter labels and require re-binarization -> labelling, but preserves shape better)")
        self.cubic.setCheckable(True)
        self.cubic.setChecked(False)
        layout.addRow("Use cubic algorithm:", self.cubic)
        
        if self.parent().original_shape is not None:
            undo_button = QPushButton(f"Resample to original shape: {self.parent().original_shape}")
            undo_button.clicked.connect(lambda: self.run_resize(undo = True))
            layout.addRow(undo_button)

        run_button = QPushButton("Run Resize")
        run_button.clicked.connect(self.run_resize)
        layout.addRow(run_button)

    def reset_fields(self):
        """Reset all input fields to default values"""
        self.resize.clear()
        self.zsize.setText("1")
        self.xsize.setText("1")
        self.ysize.setText("1")        

    def run_resize(self, undo = False):
        try:
            # Get parameters
            try:
                resize = float(self.resize.text()) if self.resize.text() else None
                zsize = float(self.zsize.text()) if self.zsize.text() else 1
                ysize = float(self.ysize.text()) if self.ysize.text() else 1
                xsize = float(self.xsize.text()) if self.xsize.text() else 1
            except ValueError as e:
                print(f"Invalid input value: {e}")
                self.reset_fields()
                return
            
            resize = resize if resize is not None else (zsize, ysize, xsize)
            
            # Get the shape from whichever array exists
            array_shape = None
            if my_network.nodes is not None:
                array_shape = my_network.nodes.shape
            elif my_network.edges is not None:
                array_shape = my_network.edges.shape
            elif my_network.network_overlay is not None:
                array_shape = my_network.network_overlay.shape
            elif my_network.id_overlay is not None:
                array_shape = my_network.id_overlay.shape
                
            if array_shape is None:
                QMessageBox.critical(self, "Error", "No valid array found to resize")
                self.reset_fields()
                return
                
            # Check if resize would result in valid dimensions
            if isinstance(resize, (int, float)):
                new_shape = tuple(int(dim * resize) for dim in array_shape)
            else:
                new_shape = tuple(int(dim * factor) for dim, factor in zip(array_shape, resize))
                
            if any(dim < 1 for dim in new_shape):
                QMessageBox.critical(self, "Error", f"Resize would result in invalid dimensions: {new_shape}")
                self.reset_fields()
                return

            cubic = self.cubic.isChecked()
            order = 3 if cubic else 0
                
            # Reset slider before modifying data
            self.parent().slice_slider.setValue(0)
            self.parent().current_slice = 0
            
            if not undo:
                # Process each channel
                for channel in range(4):
                    if self.parent().channel_data[channel] is not None:
                        resized_data = n3d.resize(self.parent().channel_data[channel], resize, order)
                        self.parent().load_channel(channel, channel_data=resized_data, data=True, assign_shape = False)

                
                # Process highlight overlay if it exists
                if self.parent().highlight_overlay is not None:
                    self.parent().highlight_overlay = n3d.resize(self.parent().highlight_overlay, resize, order)
                if my_network.search_region is not None:
                    my_network.search_region = n3d.resize(search_region, resize, order)


            else:
                # Process each channel
                if array_shape == self.parent().original_shape:
                    return
                for channel in range(4):
                    if self.parent().channel_data[channel] is not None:
                        resized_data = n3d.upsample_with_padding(self.parent().channel_data[channel], original_shape = self.parent().original_shape)
                        self.parent().load_channel(channel, channel_data=resized_data, data=True, assign_shape = False)

                
                # Process highlight overlay if it exists
                if self.parent().highlight_overlay is not None:
                    self.parent().highlight_overlay = n3d.upsample_with_padding(self.parent().highlight_overlay, original_shape = self.parent().original_shape)

                my_network.search_region = n3d.upsample_with_padding(search_region, original_shape = self.parent().original_shape)

            
            # Update slider range based on new z-dimension
            for channel in self.parent().channel_data:
                if channel is not None:
                    self.parent().slice_slider.setMinimum(0)
                    self.parent().slice_slider.setMaximum(channel.shape[0] - 1)
                    break

            if isinstance(resize, (int, float)):
                my_network.xy_scale = my_network.xy_scale/resize
                my_network.z_scale = my_network.z_scale/resize
                print("xy_scales and z_scales have been adjusted per resample. Check image -> properties to manually reset them to 1 if desired.")
            else:
                my_network.xy_scale = my_network.xy_scale/resize[1]
                my_network.z_scale = my_network.z_scale/resize[0]
                print("xy_scales and z_scales have been adjusted per resample. Check image -> properties to manually reset them to 1 if desired. Note that xy_scale will not correspond if you made your XY plane a non-square.")

            try:
                if my_network.node_centroids is not None:
                    centroids = copy.deepcopy(my_network.node_centroids)
                    if isinstance(resize, (int, float)):
                        for item in my_network.node_centroids:
                            centroids[item] = np.round((my_network.node_centroids[item]) * resize)
                    else:
                        for item in my_network.node_centroids:
                            centroids[item][0] = int(np.round((my_network.node_centroids[item][0]) * resize[0]))
                            centroids[item][1] = int(np.round((my_network.node_centroids[item][1]) * resize[1]))
                            centroids[item][2] = int(np.round((my_network.node_centroids[item][2]) * resize[2]))

                    my_network.node_centroids = centroids
                    print("Node centroids resampled")
            except:
                print("Could not resample node centroids")
                import traceback
                print(traceback.format_exc())
            try:
                if my_network.edge_centroids is not None:
                    centroids = copy.deepcopy(my_network.edge_centroids)
                    if isinstance(resize, (int, float)):
                        for item in my_network.edge_centroids:
                            centroids[item] = np.round((my_network.edge_centroids[item]) * resize)
                    else:
                        for item in my_network.edge_centroids:
                            centroids[item][0] = int(np.round((my_network.edge_centroids[item][0]) * resize[0]))
                            centroids[item][1] = int(np.round((my_network.edge_centroids[item][1]) * resize[1]))
                            centroids[item][2] = int(np.round((my_network.edge_centroids[item][2]) * resize[2]))

                    my_network.edge_centroids = centroids
                    print("Edge centroids resampled")
            except:
                print("Could not resample edge centroids")
                import traceback
                print(traceback.format_exc())

            if hasattr(my_network, 'node_centroids') and my_network.node_centroids is not None:
                try:
                    self.parent().format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                except Exception as e:
                    print(f"Error loading node centroid table: {e}")

            if hasattr(my_network, 'edge_centroids') and my_network.edge_centroids is not None:
                try:
                    self.parent().format_for_upperright_table(my_network.edge_centroids, 'EdgeID', ['Z', 'Y', 'X'], 'Edge Centroids')
                except Exception as e:
                    print(f"Error loading edge centroid table: {e}")

                    
            self.parent().update_display()
            self.reset_fields()
            self.accept()
            
        except Exception as e:
            print(f"Error during resize operation: {e}")
            import traceback
            print(traceback.format_exc())
            QMessageBox.critical(self, "Error", f"Failed to resize: {str(e)}")


class BinarizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Binarize Active Channel?")
        self.setModal(True)
        
        layout = QFormLayout(self)

       # Add Run button
        run_button = QPushButton("Run Binarize")
        run_button.clicked.connect(self.run_binarize)
        layout.addRow(run_button)

    def run_binarize(self):

        try:

            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")

            try:
                # Call binarize method with parameters
                result = n3d.binarize(
                    active_data
                    )

                # Update both the display data and the network object
                self.parent().channel_data[self.parent().active_channel] = result


                # Update the corresponding property in my_network
                setattr(my_network, network_properties[self.parent().active_channel], result)

                self.parent().update_display()
                self.accept()
                
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Error running binarize: {str(e)}"
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running binarize: {str(e)}"
            )

class LabelDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Label Active Channel?")
        self.setModal(True)
        
        layout = QFormLayout(self)

       # Add Run button
        run_button = QPushButton("Run Label")
        run_button.clicked.connect(self.run_label)
        layout.addRow(run_button)

    def run_label(self):

        try:

            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")

            try:
                # Call watershed method with parameters
                result, _ = n3d.label_objects(
                    active_data
                    )

                # Update both the display data and the network object
                self.parent().channel_data[self.parent().active_channel] = result


                # Update the corresponding property in my_network
                setattr(my_network, network_properties[self.parent().active_channel], result)

                self.parent().update_display()
                self.accept()
                
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Error",
                    f"Error running label: {str(e)}"
                )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running label: {str(e)}"
            )

class ThresholdWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Threshold Params (Active Image)")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QFormLayout(central_widget)

        self.min = QLineEdit("")
        layout.addRow("Minimum Value to retain:", self.min)
        
        # Create widgets
        self.max = QLineEdit("")
        layout.addRow("Maximum Value to retain:", self.max)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Using Volumes", "Using Label/Brightness"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # Add Run button
        prev_button = QPushButton("Preview")
        prev_button.clicked.connect(self.run_preview)
        layout.addRow(prev_button)
        
        # Add Run button
        run_button = QPushButton("Apply Threshold")
        run_button.clicked.connect(self.thresh)
        layout.addRow(run_button)
        
        # Set a reasonable default size
        self.setMinimumWidth(300)
        
    def run_preview(self):

        def get_valid_float(text, default_value):
            try:
                return float(text) if text.strip() else default_value
            except ValueError:
                print(f"Invalid input: {text}")
                return default_value

        try:
            channel = self.parent().active_channel
            accepted_mode = self.mode_selector.currentIndex()
            
            if accepted_mode == 0:
                if len(np.unique(self.parent().channel_data[self.parent().active_channel])) < 3:
                    self.parent().show_label_dialog()

                if self.parent().volume_dict[channel] is None:
                    self.parent().volumes()
                    
                volumes = self.parent().volume_dict[channel]
                default_max = max(volumes.values())
                default_min = min(volumes.values())
                
                max_val = get_valid_float(self.max.text(), default_max)
                min_val = get_valid_float(self.min.text(), default_min)
                
                valid_indices = [item for item in volumes 
                                if min_val <= volumes[item] <= max_val]
                                
            elif accepted_mode == 1:
                channel_data = self.parent().channel_data[self.parent().active_channel]
                default_max = np.max(channel_data)
                default_min = np.min(channel_data)
                
                max_val = int(get_valid_float(self.max.text(), default_max))
                min_val = int(get_valid_float(self.min.text(), default_min))
                
                if min_val > max_val:
                    min_val, max_val = max_val, min_val
                    
                valid_indices = list(range(min_val, max_val + 1))
            
            if channel == 0:
                self.parent().create_highlight_overlay(node_indices = valid_indices)
            elif channel == 1:
                self.parent().create_highlight_overlay(edge_indices = valid_indices)
            elif channel == 2:
                self.parent().create_highlight_overlay(overlay1_indices = valid_indices)
            elif channel == 3:
                self.parent().create_highlight_overlay(overlay2_indices = valid_indices)

        except Exception as e:
            print(f"Error showing preview: {e}")

    def thresh(self):
        try:

            self.run_preview()
            channel_data = self.parent().channel_data[self.parent().active_channel]
            mask = self.parent().highlight_overlay > 0
            channel_data = channel_data * mask
            self.parent().load_channel(self.parent().active_channel, channel_data, True)
            self.parent().update_display()
            self.close()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running threshold: {str(e)}"
            )


class SmartDilateDialog(QDialog):
    def __init__(self, parent, params):
        super().__init__(parent)
        self.setWindowTitle("Additional Smart Dilate Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        # GPU checkbox (default True)
        self.GPU = QPushButton("GPU")
        self.GPU.setCheckable(True)
        self.GPU.setChecked(True)
        layout.addRow("Use GPU:", self.GPU)

        self.down_factor = QLineEdit("")
        layout.addRow("Internal Downsample for GPU (if needed):", self.down_factor)

        self.params = params

        # Add Run button
        run_button = QPushButton("Dilate")
        run_button.clicked.connect(self.smart_dilate)
        layout.addRow(run_button)

    def smart_dilate(self):

        GPU = self.GPU.isChecked()
        down_factor = float(self.down_factor.text()) if self.down_factor.text().strip() else None
        active_data, amount, xy_scale, z_scale = self.params

        dilate_xy, dilate_z = n3d.dilation_length_to_pixels(xy_scale, z_scale, amount, amount)

        result = sdl.smart_dilate(active_data, dilate_xy, dilate_z, GPU = GPU, predownsample = down_factor)

        self.parent().load_channel(self.parent().active_channel, result, True)
        self.accept()



class DilateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dilate Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.amount = QLineEdit("1")
        layout.addRow("Dilation Radius:", self.amount)

        if my_network.xy_scale is not None:
            xy_scale = f"{my_network.xy_scale}"
        else:
            xy_scale = "1"

        self.xy_scale = QLineEdit(xy_scale)
        layout.addRow("xy_scale:", self.xy_scale)

        if my_network.z_scale is not None:
            z_scale = f"{my_network.z_scale}"
        else:
            z_scale = "1"

        self.z_scale = QLineEdit(z_scale)
        layout.addRow("z_scale:", self.z_scale)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Binary Dilation", "Preserve Labels (slower)", "Recursive Binary Dilation (Use if the dilation radius is much larger than your objects)"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

       # Add Run button
        run_button = QPushButton("Run Dilate")
        run_button.clicked.connect(self.run_dilate)
        layout.addRow(run_button)

    def run_dilate(self):
        try:

            accepted_mode = self.mode_selector.currentIndex()
            
            # Get amount
            try:
                amount = float(self.amount.text()) if self.amount.text() else 1
            except ValueError:
                amount = 1

            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else 1
            except ValueError:
                xy_scale = 1

            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else 1
            except ValueError:
                z_scale = 1
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")

            if accepted_mode == 1:
                dialog = SmartDilateDialog(self.parent(), [active_data, amount, xy_scale, z_scale])
                dialog.exec()
                self.accept()
                return

            if accepted_mode == 2:
                recursive = True
            else:
                recursive = False

            # Call dilate method with parameters
            result = n3d.dilate(
                active_data,
                amount,
                xy_scale = xy_scale,
                z_scale = z_scale,
                recursive = recursive
            )

            # Update both the display data and the network object
            self.parent().load_channel(self.parent().active_channel, result, True)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            import traceback
            print(traceback.format_exc())
            QMessageBox.critical(
                self,
                "Error",
                f"Error running dilate: {str(e)}"
            )

class ErodeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Erosion Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.amount = QLineEdit("1")
        layout.addRow("Erosion Radius:", self.amount)

        if my_network.xy_scale is not None:
            xy_scale = f"{my_network.xy_scale}"
        else:
            xy_scale = "1"

        self.xy_scale = QLineEdit(xy_scale)
        layout.addRow("xy_scale:", self.xy_scale)

        if my_network.z_scale is not None:
            z_scale = f"{my_network.z_scale}"
        else:
            z_scale = "1"

        self.z_scale = QLineEdit(z_scale)
        layout.addRow("z_scale:", self.z_scale)

       # Add Run button
        run_button = QPushButton("Run Erode")
        run_button.clicked.connect(self.run_erode)
        layout.addRow(run_button)

    def run_erode(self):
        try:
            
            # Get amount
            try:
                amount = float(self.amount.text()) if self.amount.text() else 1
            except ValueError:
                amount = 1

            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else 1
            except ValueError:
                xy_scale = 1

            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else 1
            except ValueError:
                z_scale = 1
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call dilate method with parameters
            result = n3d.erode(
                active_data,
                amount,
                xy_scale = xy_scale,
                z_scale = z_scale,
            )

            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running erode: {str(e)}"
            )

class HoleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fill Holes? (Active Image)")
        self.setModal(True)
        
        layout = QFormLayout(self)

       # Add Run button
        run_button = QPushButton("Run Fill Holes")
        run_button.clicked.connect(self.run_holes)
        layout.addRow(run_button)

    def run_holes(self):
        try:
            
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call dilate method with parameters
            result = n3d.fill_holes_3d(
                active_data
            )

            self.parent().load_channel(self.parent().active_channel, result, True)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running fill holes: {str(e)}"
            )

class MaskDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle("Mask Parameters")
        self.setModal(True)

        layout = QFormLayout(self)

        layout.addRow(QLabel("Use: "))

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Nodes", "Edges", "Overlay 1", "Overlay 2", "Highlight Overlay"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Masker:", self.mode_selector)

        layout.addRow(QLabel("To mask: "))

        # Add mode selection dropdown
        self.target_selector = QComboBox()
        self.target_selector.addItems(["Nodes", "Edges", "Overlay 1", "Overlay 2"])
        self.target_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("To be Masked:", self.target_selector)

        layout.addRow(QLabel("Place output in: "))

        # Add mode selection dropdown
        self.output_selector = QComboBox()
        self.output_selector.addItems(["Nodes", "Edges", "Overlay 1", "Overlay 2", "Highlight Overlay"])
        self.output_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Output Location:", self.output_selector)

        # Add Run button
        run_button = QPushButton("Mask")
        run_button.clicked.connect(self.mask)
        layout.addWidget(run_button)

    def mask(self):

        try:

            accepted_mode = self.mode_selector.currentIndex()
            accepted_target = self.target_selector.currentIndex()
            output_target = self.output_selector.currentIndex()

            if accepted_mode == 4:
                active_data = self.parent().highlight_overlay
            else:
                active_data = self.parent().channel_data[accepted_mode]

            target_data = self.parent().channel_data[accepted_target]


            try:
                result = n3d.mask(target_data, active_data)

                if output_target == 4:

                    self.parent().highlight_overlay = result

                else:


                    # Update both the display data and the network object
                    self.parent().load_channel(output_target, channel_data = result, data = True)

                self.parent().update_display()

                self.accept()

            except Exception as e:
                print(f"Error masking: {e}")

        except Exception as e:
            print(f"Error masking: {e}")



class SkeletonizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Skeletonize Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)

        self.remove = QLineEdit("0")
        layout.addRow("Remove Branches Pixel Length (int):", self.remove)

       # Add Run button
        run_button = QPushButton("Run Skeletonize")
        run_button.clicked.connect(self.run_skeletonize)
        layout.addRow(run_button)

    def run_skeletonize(self):
        try:
            
            # Get branch removal
            try:
                remove = int(self.remove.text()) if self.remove.text() else 0
            except ValueError:
                remove = 0
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call dilate method with parameters
            result = n3d.skeletonize(
                active_data
            )

            if remove > 0:
                result = n3d.remove_branches(result, remove)


            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running skeletonize: {str(e)}"
            )   


class WatershedDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Watershed Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # Directory (empty by default)
        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Leave empty for None")
        layout.addRow("Output Directory:", self.directory)
        
        # Proportion (default 0.1)
        self.proportion = QLineEdit("0.05")
        layout.addRow("Proportion:", self.proportion)
        
        # GPU checkbox (default True)
        self.gpu = QPushButton("GPU")
        self.gpu.setCheckable(True)
        self.gpu.setChecked(True)
        layout.addRow("Use GPU:", self.gpu)
        
        # Smallest radius (empty by default)
        self.smallest_rad = QLineEdit()
        self.smallest_rad.setPlaceholderText("Leave empty for None")
        layout.addRow("Smallest Radius:", self.smallest_rad)
        
        # Predownsample (empty by default)
        self.predownsample = QLineEdit()
        self.predownsample.setPlaceholderText("Leave empty for None")
        layout.addRow("Smart Dilate GPU Downsample:", self.predownsample)
        
        # Predownsample2 (empty by default)
        self.predownsample2 = QLineEdit()
        self.predownsample2.setPlaceholderText("Leave empty for None")
        layout.addRow("Smart Label GPU Downsample:", self.predownsample2)
        
        # Add Run button
        run_button = QPushButton("Run Watershed")
        run_button.clicked.connect(self.run_watershed)
        layout.addRow(run_button)

    def run_watershed(self):
        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get proportion (0.1 if empty or invalid)
            try:
                proportion = float(self.proportion.text()) if self.proportion.text() else 0.05
            except ValueError:
                proportion = 0.05
            
            # Get GPU state
            gpu = self.gpu.isChecked()
            
            # Get smallest_rad (None if empty)
            try:
                smallest_rad = float(self.smallest_rad.text()) if self.smallest_rad.text() else None
            except ValueError:
                smallest_rad = None
            
            # Get predownsample (None if empty)
            try:
                predownsample = float(self.predownsample.text()) if self.predownsample.text() else None
            except ValueError:
                predownsample = None
            
            # Get predownsample2 (None if empty)
            try:
                predownsample2 = float(self.predownsample2.text()) if self.predownsample2.text() else None
            except ValueError:
                predownsample2 = None
            
            # Get the active channel data from parent
            active_data = self.parent().channel_data[self.parent().active_channel]
            if active_data is None:
                raise ValueError("No active image selected")
            
            # Call watershed method with parameters
            result = n3d.watershed(
                active_data,
                directory=directory,
                proportion=proportion,
                GPU=gpu,
                smallest_rad=smallest_rad,
                predownsample=predownsample,
                predownsample2=predownsample2
            )

            # Update both the display data and the network object
            self.parent().channel_data[self.parent().active_channel] = result


            # Update the corresponding property in my_network
            setattr(my_network, network_properties[self.parent().active_channel], result)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running watershed: {str(e)}"
            )

class ZDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Z Parameters (Save your network first - this will alter all channels into 2D versions)")
        self.setModal(True)
        
        layout = QFormLayout(self)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["max", "mean", "min", "sum", "std"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # Add Run button
        run_button = QPushButton("Run Z Project")
        run_button.clicked.connect(self.run_z)
        layout.addRow(run_button)

    def run_z(self):

        mode = self.mode_selector.currentText()

        for i in range(len(self.parent().channel_data)):
            try:
                self.parent().channel_data[i] = n3d.z_project(self.parent().channel_data[i], mode)
                self.parent().load_channel(i, self.parent().channel_data[i], True)
            except:
                pass

        self.accept()


class CentroidNodeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Nodes from Centroids")
        self.setModal(True)
        
        layout = QFormLayout(self)

        # Add Run button
        run_button = QPushButton("Run Node Generation? (Will override current nodes). Note it is presumed your nodes begin at 1, not 0.")
        run_button.clicked.connect(self.run_nodes)
        layout.addRow(run_button)

    def run_nodes(self):

        try:

            if my_network.node_centroids is None and my_network.nodes is not None:
                self.parent().show_centroid_dialog()

                if my_network.node_centroids is None:

                    QMessageBox.critical(
                        self,
                        "Error",
                        f"Could not generate centroids from current nodes. Please load centroids in an Excel (.xlsx) or CSV (.csv) file with columns 'Node ID', 'Z', 'Y', and 'X' in that order. The first row should contain these column headers, followed by the numerical ID of each node and numeric values for each centroid. Note it is presumed your nodes begin at 1, not 0. Error"
                    )
                    return
            elif my_network.node_centroids is None:

                QMessageBox.critical(
                    self,
                    "Error",
                    f"Could not find centroids. Please load centroids in an Excel (.xlsx) or CSV (.csv) file with columns 'Node ID', 'Z', 'Y', and 'X' in that order. The first row should contain these column headers, followed by numeric values for each centroid. Note it is presumed your nodes begin at 1, not 0. Error:"
                )
                return

            my_network.nodes = my_network.centroid_array()

            self.parent().load_channel(0, channel_data = my_network.nodes, data = True)

            self.accept()

        except Exception as e:

            print(f"Error generating centroids: {e}")




class GenNodesDialog(QDialog):

    def __init__(self, parent=None, down_factor = None, called = False):
        super().__init__(parent)
        self.setWindowTitle("Create Nodes from Edge Vertices")
        self.setModal(True)

        layout = QFormLayout(self)
        self.called = called

        self.branch_removal = QLineEdit("0")
        layout.addRow("Skeleton Voxel Branch Length to Remove (int) (Compensates for spines off medial axis):", self.branch_removal)

        self.max_vol = QLineEdit("0")
        layout.addRow("Maximum Voxel Volume of Vertices to Retain (int - Compensates for skeleton looping - occurs before any node merging - the smallest objects are always 27 voxels):", self.max_vol)

        self.comp_dil = QLineEdit("0")
        layout.addRow("Voxel distance to merge nearby nodes (Int - compensates for multi-branch identification along thick branch regions):", self.comp_dil)

        if not down_factor:
            down_factor = None
        if down_factor is None:
            self.down_factor = QLineEdit("0")
            layout.addRow("Downsample Factor (Speeds up calculation at the cost of fidelity):", self.down_factor)
        else:
            self.down_factor = down_factor

        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Leave empty to save in active dir")
        layout.addRow("Output Directory:", self.directory)

        # retain checkbox (default True)
        if not called:
            self.retain = QPushButton("Retain")
            self.retain.setCheckable(True)
            self.retain.setChecked(True)
            layout.addRow("Retain Original Edges? (Will be moved to overlay 2):", self.retain)
        else:
            self.retain = True

        # Add Run button
        run_button = QPushButton("Run Node Generation")
        run_button.clicked.connect(self.run_gennodes)
        layout.addRow(run_button)

    def run_gennodes(self):

        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get branch_removal
            try:
                branch_removal = int(self.branch_removal.text()) if self.branch_removal.text() else 0
            except ValueError:
                branch_removal = 0
                
            # Get max_vol
            try:
                max_vol = int(self.max_vol.text()) if self.max_vol.text() else 0
            except ValueError:
                max_vol = 0
            
            # Get comp_dil
            try:
                comp_dil = int(self.comp_dil.text()) if self.comp_dil.text() else 0
            except ValueError:
                comp_dil = 0
                
            # Get down_factor
            if type(self.down_factor) is int:
                down_factor = self.down_factor
            else:
                try:
                    down_factor = int(self.down_factor.text()) if self.down_factor.text() else 0
                except ValueError:
                    down_factor = 0
                
            try:
                retain = self.retain.isChecked()
            except:
                retain = True

            
            result, skele = n3d.label_vertices(
                my_network.edges,
                max_vol=max_vol,
                branch_removal=branch_removal,
                comp_dil=comp_dil,
                down_factor=down_factor,
                return_skele = True

            )

            if down_factor > 0 and not self.called:
                my_network.edges = n3d.downsample(my_network.edges, down_factor)
                my_network.xy_scale = my_network.xy_scale * down_factor
                my_network.z_scale = my_network.z_scale * down_factor
                print("xy_scales and z_scales have been adjusted per downsample. Check image -> properties to manually reset them to 1 if desired.")

            try: #Resets centroid fields
                if my_network.node_centroids is not None:
                    my_network.node_centroids = None
            except:
                pass
            try:
                if my_network.edge_centroids is not None:
                    my_network.edge_centroids = None
            except:
                pass


            if retain:
                self.parent().load_channel(3, channel_data = my_network.edges, data = True)

            self.parent().load_channel(1, channel_data = skele, data = True)

            self.parent().load_channel(0, channel_data = result, data = True)

            self.parent().update_display()
            self.accept()
            
        except Exception as e:


            QMessageBox.critical(
                self,
                "Error",
                f"Error running generate nodes: {str(e)}"
            )


class BranchDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Label Branches (of edges)")
        self.setModal(True)

        layout = QFormLayout(self)

        # Nodes checkbox (default True)
        self.nodes = QPushButton("Generate Nodes")
        self.nodes.setCheckable(True)
        self.nodes.setChecked(True)
        layout.addRow("Generate nodes from edges? (Skip if already completed - presumes your edge skeleton from generate nodes is in Edges and that your original Edges are in Overlay 2):", self.nodes)

        # GPU checkbox (default True)
        self.GPU = QPushButton("GPU")
        self.GPU.setCheckable(True)
        self.GPU.setChecked(False)
        layout.addRow("Use GPU (Note this may need to temporarily downsample your large images which may simplify outputs - Only memory errors but not permission errors for accessing GRAM are handled by default - CPU will never try to downsample):", self.GPU)

        self.down_factor = QLineEdit("0")
        layout.addRow("Internal downsample (will have to recompute nodes)?:", self.down_factor)

        # Add Run button
        run_button = QPushButton("Run Branch Label")
        run_button.clicked.connect(self.branch_label)
        layout.addRow(run_button)

    def branch_label(self):

        try:

            try:
                down_factor = int(self.down_factor.text()) if self.down_factor.text() else 0
            except ValueError:
                down_factor = 0

            nodes = self.nodes.isChecked()
            GPU = self.GPU.isChecked()

            original_shape = my_network.edges.shape

            if down_factor > 0:
                self.parent().show_gennodes_dialog(down_factor = down_factor, called = True)
            elif nodes:
                self.parent().show_gennodes_dialog(called = True)
                down_factor = None

            if my_network.edges is not None and my_network.nodes is not None and my_network.id_overlay is not None:

                output = n3d.label_branches(my_network.edges, nodes = my_network.nodes, bonus_array = my_network.id_overlay, GPU = GPU, down_factor = down_factor)

                if down_factor is not None:

                    self.parent().reset(nodes = True, id_overlay = True)

                else:
                    self.parent().reset(id_overlay = True)

                self.parent().load_channel(1, channel_data = output, data = True)

            self.parent().update_display()
            self.accept()

        except Exception as e:
            print(f"Error labeling branches: {e}")



class IsolateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Node types to isolate")
        self.setModal(True)
        layout = QFormLayout(self)
        
        self.combo1 = QComboBox()
        self.combo1.addItems(list(set(my_network.node_identities.values())))  
        self.combo1.setCurrentIndex(0)
        layout.addRow("ID 1:", self.combo1)
        
        self.combo2 = QComboBox()
        self.combo2.addItems(list(set(my_network.node_identities.values())))      
        self.combo2.setCurrentIndex(1)
        layout.addRow("ID 2:", self.combo2)
        
        # Add submit button
        sub_button = QPushButton("Submit")
        sub_button.clicked.connect(self.submit_ids)
        layout.addRow(sub_button)

    def submit_ids(self):
        try:
            id1 = self.combo1.currentText()
            id2 = self.combo2.currentText()
            if id1 == id2:
                print("Please select different identities")
                self.parent().show_isolate_dialog()
                return
            else:
                my_network.isolate_internode_connections(id1, id2)
                self.accept()
        except Exception as e:
            print(f"An error occurred: {e}")

class AlterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Node/Edge groups to add/remove")
        self.setModal(True)
        layout = QFormLayout(self)
        
        # Node 1
        self.node1 = QLineEdit()
        self.node1.setPlaceholderText("Enter integer")
        layout.addRow("Node1:", self.node1)
        
        # Node 2
        self.node2 = QLineEdit()
        self.node2.setPlaceholderText("Enter integer")
        layout.addRow("Node2:", self.node2)
        
        # Edge
        self.edge = QLineEdit()
        self.edge.setPlaceholderText("Optional - Enter integer")
        layout.addRow("Edge:", self.edge)
        
        # Add add button
        addbutton = QPushButton("Add pair")
        addbutton.clicked.connect(self.add)
        layout.addRow(addbutton)
        
        # Add remove button
        removebutton = QPushButton("Remove pair")
        removebutton.clicked.connect(self.remove)
        layout.addRow(removebutton)

    def add(self):
        try:
            node1 = int(self.node1.text()) if self.node1.text().strip() else None
            node2 = int(self.node2.text()) if self.node2.text().strip() else None
            edge = int(self.edge.text()) if self.edge.text().strip() else None
            
            # Check if we have valid node pairs
            if node1 is not None and node2 is not None:
                # Add the node pair and its reverse
                my_network.network_lists[0].append(node1)
                my_network.network_lists[1].append(node2)
                # Add edge value (0 if none provided)
                my_network.network_lists[2].append(edge if edge is not None else 0)
                
                # Add reverse pair with same edge value
                my_network.network_lists[0].append(node2)
                my_network.network_lists[1].append(node1)
                my_network.network_lists[2].append(edge if edge is not None else 0)
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.parent().network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.parent().network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error showing network table: {e}")
        except ValueError:
            import traceback
            print(traceback.format_exc())
            pass  # Invalid input - do nothing

    def remove(self):
        try:
            node1 = int(self.node1.text()) if self.node1.text().strip() else None
            node2 = int(self.node2.text()) if self.node2.text().strip() else None
            edge = int(self.edge.text()) if self.edge.text().strip() else None
            
            # Check if we have valid node pairs
            if node1 is not None and node2 is not None:
                # Create lists for indices to remove
                indices_to_remove = []
                
                # Loop through the lists to find matching pairs
                for i in range(len(my_network.network_lists[0])):
                    forward_match = (my_network.network_lists[0][i] == node1 and 
                                   my_network.network_lists[1][i] == node2)
                    reverse_match = (my_network.network_lists[0][i] == node2 and 
                                   my_network.network_lists[1][i] == node1)
                    
                    if forward_match or reverse_match:
                        # If edge value specified, only remove if edge matches
                        if edge is not None:
                            if my_network.network_lists[2][i] == edge:
                                indices_to_remove.append(i)
                        else:
                            # If no edge specified, remove all matching pairs
                            indices_to_remove.append(i)
                
                # Remove elements in reverse order to maintain correct indices
                for i in sorted(indices_to_remove, reverse=True):
                    my_network.network_lists[0].pop(i)
                    my_network.network_lists[1].pop(i)
                    my_network.network_lists[2].pop(i)

            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.parent().network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.parent().network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error showing network table: {e}")
                    
        except ValueError:
            import traceback
            print(traceback.format_exc())
            pass  # Invalid input - do nothing


class ModifyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Nodes from Edge Vertices")
        self.setModal(True)
        layout = QFormLayout(self)
        
        # trunk checkbox (default false)
        self.trunk = QPushButton("Remove Trunk")
        self.trunk.setCheckable(True)
        self.trunk.setChecked(False)
        layout.addRow("Remove Trunk? (Most connected edge - overrides below):", self.trunk)
        
        # trunk checkbox (default false)
        self.trunknode = QPushButton("Trunk -> Node")
        self.trunknode.setCheckable(True)
        self.trunknode.setChecked(False)
        layout.addRow("Convert Trunk to Node? (Most connected edge):", self.trunknode)
        
        # edgenode checkbox (default false)
        self.edgenode = QPushButton("Edges -> Nodes")
        self.edgenode.setCheckable(True)
        self.edgenode.setChecked(False)
        layout.addRow("Convert 'Edges (Labeled objects)' to node objects?:", self.edgenode)
        
        # edgeweight checkbox (default false)
        self.edgeweight = QPushButton("Remove weights")
        self.edgeweight.setCheckable(True)
        self.edgeweight.setChecked(False)
        layout.addRow("Remove network weights?:", self.edgeweight)
        
        # prune checkbox (default false)
        self.prune = QPushButton("Prune Same Type")
        self.prune.setCheckable(True)
        self.prune.setChecked(False)
        layout.addRow("Prune connections between nodes of the same type (if assigned)?:", self.prune)
        
        # isolate checkbox (default false)
        self.isolate = QPushButton("Isolate Two Types")
        self.isolate.setCheckable(True)
        self.isolate.setChecked(False)
        layout.addRow("Isolate connections between two specific node types (if assigned)?:", self.isolate)

        #change button
        change_button = QPushButton("Add/Remove Network Pairs")
        change_button.clicked.connect(self.show_alter_dialog)
        layout.addRow(change_button)
                
        # Add Run button
        run_button = QPushButton("Make Changes")
        run_button.clicked.connect(self.run_changes)
        layout.addRow(run_button)

    def show_isolate_dialog(self):

        dialog = IsolateDialog(self)
        dialog.exec()

    def show_alter_dialog(self):

        dialog = AlterDialog(self.parent())
        dialog.exec()

    def run_changes(self):

        try:

            trunk = self.trunk.isChecked()
            if not trunk:
                trunknode = self.trunknode.isChecked()
            else:
                trunknode = False
            edgenode = self.edgenode.isChecked()
            edgeweight = self.edgeweight.isChecked()
            prune = self.prune.isChecked()
            isolate = self.isolate.isChecked()

            if isolate and my_network.node_identities is not None:
                self.show_isolate_dialog()

            if edgeweight:
                my_network.remove_edge_weights()
            if prune and my_network.node_identities is not None:
                my_network.prune_samenode_connections()
            if trunk:
                my_network.remove_trunk_post()
            if trunknode:
                if my_network.node_centroids is None or my_network.edge_centroids is None:
                    self.parent().show_centroid_dialog()
                my_network.trunk_to_node()
                self.parent().load_channel(0, my_network.nodes, True)
            if edgenode:
                if my_network.node_centroids is None or my_network.edge_centroids is None:
                    self.parent().show_centroid_dialog()
                my_network.edge_to_node()
                self.parent().load_channel(0, my_network.nodes, True)
                self.parent().load_channel(1, my_network.edges, True)
                try:
                    self.parent().format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                except:
                    pass
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.parent().network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.parent().network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error showing network table: {e}")

            if hasattr(my_network, 'node_identities') and my_network.node_identities is not None:
                try:
                    self.parent().format_for_upperright_table(my_network.node_identities, 'NodeID', 'Identity', 'Node Identities')
                except Exception as e:
                    print(f"Error loading node identity table: {e}")

            self.parent().update_display()
            self.accept()

        except Exception as e:
            print(f"An error occurred: {e}")







class CentroidDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculate Centroids")
        self.setModal(True)

        layout = QFormLayout(self)

        self.directory = QLineEdit()
        self.directory.setPlaceholderText("Leave empty for active directory")
        layout.addRow("Output Directory:", self.directory)

        self.downsample = QLineEdit("1")
        layout.addRow("Downsample Factor:", self.downsample)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Nodes and Edges", "Nodes", "Edges"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        # Add Run button
        run_button = QPushButton("Run Calculate Centroids")
        run_button.clicked.connect(self.run_centroids)
        layout.addRow(run_button)

    def run_centroids(self):

        try:

            chan = self.mode_selector.currentIndex()

            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get downsample
            try:
                downsample = float(self.downsample.text()) if self.downsample.text() else 1
            except ValueError:
                downsample = 1

            if chan == 0 and my_network.edges is None: #if we don't have edges, just do nodes by default
                chan = 1

            if chan == 1:
                my_network.calculate_node_centroids(
                    down_factor = downsample
                )
                my_network.save_node_centroids(directory = directory)

            elif chan == 2:
                my_network.calculate_edge_centroids(
                    down_factor = downsample
                )
                my_network.save_edge_centroids(directory = directory)

            elif chan == 0:
                my_network.calculate_node_centroids(
                    down_factor = downsample
                )
                my_network.save_node_centroids(directory = directory)

                my_network.calculate_edge_centroids(
                    down_factor = downsample
                )
                my_network.save_edge_centroids(directory = directory)

            if hasattr(my_network, 'node_centroids') and my_network.node_centroids is not None:
                try:
                    self.parent().format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                except Exception as e:
                    print(f"Error loading node centroid table: {e}")

            if hasattr(my_network, 'edge_centroids') and my_network.edge_centroids is not None:
                try:
                    self.parent().format_for_upperright_table(my_network.edge_centroids, 'EdgeID', ['Z', 'Y', 'X'], 'Edge Centroids')
                except Exception as e:
                    print(f"Error loading edge centroid table: {e}")


            self.parent().update_display()
            self.accept()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error finding centroids: {str(e)}"
            )
            import traceback
            print(traceback.format_exc())




class CalcAllDialog(QDialog):
    # Class variables to store previous settings
    prev_directory = ""
    prev_xy_scale = "1"
    prev_z_scale = "1"
    prev_search = ""
    prev_diledge = ""
    prev_down_factor = ""
    prev_GPU_downsample = ""
    prev_other_nodes = ""
    prev_remove_trunk = ""
    prev_gpu = True
    prev_label_nodes = True
    prev_inners = True
    prev_skeletonize = False
    prev_overlays = False
    prev_updates = True

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculate All Parameters")
        self.setModal(True)
        
        layout = QFormLayout(self)
        
        # Directory (empty by default)
        self.directory = QLineEdit(self.prev_directory)
        self.directory.setPlaceholderText("Leave empty for 'my_network'")
        layout.addRow("Output Directory:", self.directory)
        
        # Load previous values for all inputs
        self.xy_scale = QLineEdit(self.prev_xy_scale)
        layout.addRow("xy_scale:", self.xy_scale)
        
        self.z_scale = QLineEdit(self.prev_z_scale)
        layout.addRow("z_scale:", self.z_scale)

        self.search = QLineEdit(self.prev_search)
        self.search.setPlaceholderText("Leave empty for None")
        layout.addRow("Node Search (float):", self.search)

        self.diledge = QLineEdit(self.prev_diledge)
        self.diledge.setPlaceholderText("Leave empty for None")
        layout.addRow("Edge Reconnection Distance (int):", self.diledge)

        self.down_factor = QLineEdit(self.prev_down_factor)
        self.down_factor.setPlaceholderText("Leave empty for None")
        layout.addRow("Downsample for Centroids (int):", self.down_factor)

        self.GPU_downsample = QLineEdit(self.prev_GPU_downsample)
        self.GPU_downsample.setPlaceholderText("Leave empty for None")
        layout.addRow("Downsample for Distance Transform (GPU) (int):", self.GPU_downsample)

        self.other_nodes = QLineEdit(self.prev_other_nodes)
        self.other_nodes.setPlaceholderText("Leave empty for None")
        layout.addRow("Filepath or directory containing additional node images:", self.other_nodes)

        self.remove_trunk = QLineEdit(self.prev_remove_trunk)
        self.remove_trunk.setPlaceholderText("Leave empty for 0")
        layout.addRow("Times to remove edge trunks (int): ", self.remove_trunk)

        # Load previous button states
        self.gpu = QPushButton("GPU")
        self.gpu.setCheckable(True)
        self.gpu.setChecked(self.prev_gpu)
        layout.addRow("Use GPU:", self.gpu)

        self.label_nodes = QPushButton("Label")
        self.label_nodes.setCheckable(True)
        self.label_nodes.setChecked(self.prev_label_nodes)
        layout.addRow("Label Nodes:", self.label_nodes)

        self.inners = QPushButton("Inner Edges")
        self.inners.setCheckable(True)
        self.inners.setChecked(self.prev_inners)
        layout.addRow("Use Inner Edges:", self.inners)

        self.skeletonize = QPushButton("Skeletonize")
        self.skeletonize.setCheckable(True)
        self.skeletonize.setChecked(self.prev_skeletonize)
        layout.addRow("Skeletonize Edges:", self.skeletonize)

        self.overlays = QPushButton("Overlays")
        self.overlays.setCheckable(True)
        self.overlays.setChecked(self.prev_overlays)
        layout.addRow("Generate Overlays:", self.overlays)

        self.update = QPushButton("Update")
        self.update.setCheckable(True)
        self.update.setChecked(self.prev_updates)
        layout.addRow("Update Node/Edge in NetTracer3D:", self.update)
        
        # Add Run button
        run_button = QPushButton("Run Calculate All")
        run_button.clicked.connect(self.run_calc_all)
        layout.addRow(run_button)

    def run_calc_all(self):

        try:
            # Get directory (None if empty)
            directory = self.directory.text() if self.directory.text() else None
            
            # Get xy_scale and z_scale (1 if empty or invalid)
            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else 1
            except ValueError:
                xy_scale = 1
                
            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else 1
            except ValueError:
                z_scale = 1
            
            # Get search value (None if empty)
            try:
                search = float(self.search.text()) if self.search.text() else None
            except ValueError:
                search = None
                
            # Get diledge value (None if empty)
            try:
                diledge = int(self.diledge.text()) if self.diledge.text() else None
            except ValueError:
                diledge = None
                
            # Get down_factor value (None if empty)
            try:
                down_factor = int(self.down_factor.text()) if self.down_factor.text() else None
            except ValueError:
                down_factor = None
                
            # Get GPU_downsample value (None if empty)
            try:
                GPU_downsample = int(self.GPU_downsample.text()) if self.GPU_downsample.text() else None
            except ValueError:
                GPU_downsample = None
                
            # Get other_nodes path (None if empty)
            other_nodes = self.other_nodes.text() if self.other_nodes.text() else None
            
            # Get remove_trunk value (0 if empty)
            try:
                remove_trunk = int(self.remove_trunk.text()) if self.remove_trunk.text() else 0
            except ValueError:
                remove_trunk = 0
                
            # Get button states
            gpu = self.gpu.isChecked()
            label_nodes = self.label_nodes.isChecked()
            inners = self.inners.isChecked()
            skeletonize = self.skeletonize.isChecked()
            overlays = self.overlays.isChecked()
            update = self.update.isChecked()

            if not update:
                temp_nodes = my_network.nodes.copy()
                temp_edges = my_network.edges.copy()
            
            my_network.calculate_all(
                my_network.nodes,
                my_network.edges,
                directory=directory,
                xy_scale=xy_scale,
                z_scale=z_scale,
                search=search,
                diledge=diledge,
                down_factor=down_factor,
                GPU_downsample=GPU_downsample,
                other_nodes=other_nodes,
                remove_trunk=remove_trunk,
                GPU=gpu,
                label_nodes=label_nodes,
                inners=inners,
                skeletonize=skeletonize
            )

            # Store current values as previous values
            CalcAllDialog.prev_directory = self.directory.text()
            CalcAllDialog.prev_xy_scale = self.xy_scale.text()
            CalcAllDialog.prev_z_scale = self.z_scale.text()
            CalcAllDialog.prev_search = self.search.text()
            CalcAllDialog.prev_diledge = self.diledge.text()
            CalcAllDialog.prev_down_factor = self.down_factor.text()
            CalcAllDialog.prev_GPU_downsample = self.GPU_downsample.text()
            CalcAllDialog.prev_other_nodes = self.other_nodes.text()
            CalcAllDialog.prev_remove_trunk = self.remove_trunk.text()
            CalcAllDialog.prev_gpu = self.gpu.isChecked()
            CalcAllDialog.prev_label_nodes = self.label_nodes.isChecked()
            CalcAllDialog.prev_inners = self.inners.isChecked()
            CalcAllDialog.prev_skeletonize = self.skeletonize.isChecked()
            CalcAllDialog.prev_overlays = self.overlays.isChecked()
            CalcAllDialog.prev_updates = self.update.isChecked()


            # Update both the display data and the network object
            if update:
                self.parent().channel_data[0] = my_network.nodes
                self.parent().channel_data[1] = my_network.edges
            else:
                my_network.nodes = temp_nodes.copy()
                del temp_nodes
                my_network.edges = temp_edges.copy()
                del temp_edges
                self.parent().channel_data[0] = my_network.nodes
                self.parent().channel_data[1] = my_network.edges


            # Then handle overlays
            if overlays:
                if directory is None:
                    directory = 'my_network'
                
                # Generate and update overlays
                my_network.network_overlay = my_network.draw_network(directory=directory)
                my_network.id_overlay = my_network.draw_node_indices(directory=directory)
                
                # Update channel data
                self.parent().channel_data[2] = my_network.network_overlay
                self.parent().channel_data[3] = my_network.id_overlay
                
                # Enable the overlay channel buttons
                self.parent().channel_buttons[2].setEnabled(True)
                self.parent().channel_buttons[3].setEnabled(True)


            self.parent().update_display()
            self.accept()

            # Display network_lists in the network table
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.parent().network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.parent().network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error loading network_lists: {e}")

            #Display the other things if they exist
            try:

                if hasattr(my_network, 'node_identities') and my_network.node_identities is not None:
                    try:
                        self.parent().format_for_upperright_table(my_network.node_identities, 'NodeID', 'Identity', 'Node Identities')
                    except Exception as e:
                        print(f"Error loading node identity table: {e}")

                if hasattr(my_network, 'node_centroids') and my_network.node_centroids is not None:
                    try:
                        self.parent().format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                    except Exception as e:
                        print(f"Error loading node centroid table: {e}")


                if hasattr(my_network, 'edge_centroids') and my_network.edge_centroids is not None:
                    try:
                        self.parent().format_for_upperright_table(my_network.edge_centroids, 'EdgeID', ['Z', 'Y', 'X'], 'Edge Centroids')
                    except Exception as e:
                        print(f"Error loading edge centroid table: {e}")


            except Exception as e:
                print(f"An error has occured: {e}")

            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Error running calculate all: {str(e)}"
            )

class ProxDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculate Proximity Network")
        self.setModal(True)

        layout = QFormLayout(self)

        # Directory (empty by default)
        self.directory = QLineEdit('')
        self.directory.setPlaceholderText("Leave empty for 'my_network'")
        layout.addRow("Output Directory:", self.directory)

        self.search = QLineEdit()
        self.search.setPlaceholderText("search")
        layout.addRow("Search Region Distance? (enter true value corresponding to scaling, ie in microns):", self.search)

        # Load previous values for all inputs
        self.xy_scale = QLineEdit(f"{my_network.xy_scale}")
        layout.addRow("xy_scale:", self.xy_scale)
        
        self.z_scale = QLineEdit(f"{my_network.z_scale}")
        layout.addRow("z_scale:", self.z_scale)

        # Add mode selection dropdown
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["From Centroids (fast but ignores shape - use for small or spherical objects - search STARTS at centroid)", "From Morphological Shape (slower but preserves shape - use for oddly shaped objects - search STARTS at object border)"])
        self.mode_selector.setCurrentIndex(0)  # Default to Mode 1
        layout.addRow("Execution Mode:", self.mode_selector)

        if my_network.node_identities is not None:
            self.id_selector = QComboBox()
            # Add all options from id dictionary
            self.id_selector.addItems(['None'] + list(set(my_network.node_identities.values())))
            self.id_selector.setCurrentIndex(0)  # Default to Mode 1
            layout.addRow("Create Networks only from a specific node identity?:", self.id_selector)
        else:
            self.id_selector = None

        self.overlays = QPushButton("Overlays")
        self.overlays.setCheckable(True)
        self.overlays.setChecked(True)
        layout.addRow("Generate Overlays:", self.overlays)

        self.populate = QPushButton("Populate Nodes from Centroids?")
        self.populate.setCheckable(True)
        self.populate.setChecked(False)
        layout.addRow("If using centroid search:", self.populate)

        # Add Run button
        run_button = QPushButton("Run Proximity Network")
        run_button.clicked.connect(self.prox)
        layout.addRow(run_button)

    def prox(self):

        try:

            populate = self.populate.isChecked()

            mode = self.mode_selector.currentIndex()

            if self.id_selector is not None and self.id_selector.currentText() != 'None':
                target = self.id_selector.currentText()
                targets = []
                for node in my_network.node_identities:
                    if target == my_network.node_identities[node]:
                        targets.append(int(node))
            else:
                targets = None

            try:
                directory = self.directory.text() if self.directory.text() else None
            except:
                directory = None

            # Get xy_scale and z_scale (1 if empty or invalid)
            try:
                xy_scale = float(self.xy_scale.text()) if self.xy_scale.text() else my_network.xy_scale
            except ValueError:
                xy_scale = my_network.xy_scale
                
            try:
                z_scale = float(self.z_scale.text()) if self.z_scale.text() else my_network.z_scale
            except ValueError:
                z_scale = my_network.z_scale

            # Get search value (None if empty)
            try:
                search = float(self.search.text()) if self.search.text() else None
            except ValueError:
                search = None

            overlays = self.overlays.isChecked()        

            my_network.xy_scale = xy_scale
            my_network.z_scale = z_scale


            if mode == 1:
                if len(np.unique(my_network.nodes)) < 3:
                    my_network.nodes, _ = n3d.label_objects(my_network.nodes)
                if my_network.node_centroids is None:
                    self.parent().show_centroid_dialog()
                my_network.morph_proximity(search = search, targets = targets)

                self.parent().load_channel(0, channel_data = my_network.nodes, data = True)
            elif mode == 0:

                if my_network.node_centroids is None and my_network.nodes is not None:
                    self.parent().show_centroid_dialog()

                    if my_network.node_centroids is None:

                        QMessageBox.critical(
                            self,
                            "Error",
                            f"Could not generate centroids from current nodes. Please load centroids in an Excel (.xlsx) or CSV (.csv) file with columns 'Node ID', 'Z', 'Y', and 'X' in that order. The first row should contain these column headers, followed by the numerical ID of each node and numeric values for each centroid. Note it is presumed your nodes begin at 1, not 0. Error"
                        )
                        return
                elif my_network.node_centroids is None:

                    QMessageBox.critical(
                        self,
                        "Error",
                        f"Could not find centroids. Please load centroids in an Excel (.xlsx) or CSV (.csv) file with columns 'Node ID', 'Z', 'Y', and 'X' in that order. The first row should contain these column headers, followed by numeric values for each centroid. Note it is presumed your nodes begin at 1, not 0. Error:"
                    )
                    return
                    
                if populate:
                    my_network.nodes = my_network.kd_network(distance = search, targets = targets)
                    self.parent().load_channel(0, channel_data = my_network.nodes, data = True)
                else:
                    my_network.kd_network(distance = search, targets = targets)


            my_network.dump(directory = directory)


            # Then handle overlays
            if overlays:

                if my_network.node_centroids is not None:
                    if directory is None:
                        directory = 'my_network'
                    
                    # Generate and update overlays
                    my_network.network_overlay = my_network.draw_network(directory=directory)
                    my_network.id_overlay = my_network.draw_node_indices(directory=directory)
                    
                    # Update channel data
                    self.parent().channel_data[2] = my_network.network_overlay
                    self.parent().channel_data[3] = my_network.id_overlay
                    
                    # Enable the overlay channel buttons
                    self.parent().channel_buttons[2].setEnabled(True)
                    self.parent().channel_buttons[3].setEnabled(True)


            self.parent().update_display()
            self.accept()

            # Display network_lists in the network table
            try:
                if hasattr(my_network, 'network_lists'):
                    model = PandasModel(my_network.network_lists)
                    self.parent().network_table.setModel(model)
                    # Adjust column widths to content
                    for column in range(model.columnCount(None)):
                        self.parent().network_table.resizeColumnToContents(column)
            except Exception as e:
                print(f"Error loading network_lists: {e}")

            #Display the other things if they exist
            try:

                if hasattr(my_network, 'node_identities') and my_network.node_identities is not None:
                    try:
                        self.parent().format_for_upperright_table(my_network.node_identities, 'NodeID', 'Identity', 'Node Identities')
                    except Exception as e:
                        print(f"Error loading node identity table: {e}")

                if hasattr(my_network, 'node_centroids') and my_network.node_centroids is not None:
                    try:
                        self.parent().format_for_upperright_table(my_network.node_centroids, 'NodeID', ['Z', 'Y', 'X'], 'Node Centroids')
                    except Exception as e:
                        print(f"Error loading node centroid table: {e}")


                if hasattr(my_network, 'edge_centroids') and my_network.edge_centroids is not None:
                    try:
                        self.parent().format_for_upperright_table(my_network.edge_centroids, 'EdgeID', ['Z', 'Y', 'X'], 'Edge Centroids')
                    except Exception as e:
                        print(f"Error loading edge centroid table: {e}")
            except:
                pass

            if my_network.network is None:
                my_network.network = my_network.network_lists

        except Exception as e:
            print(f"Error running proximity network: {str(e)}")
            import traceback
            print(traceback.format_exc())








# Initiating this program from the script line:

def run_gui():
    global my_network
    my_network = n3d.Network_3D()
    global network_properties
    # Update the corresponding network property based on active channel
    network_properties = {
        0: 'nodes',
        1: 'edges',
        2: 'network_overlay',
        3: 'id_overlay'
    }

    app = QApplication(sys.argv)
    window = ImageViewerWindow()
    window.show()
    sys.exit(app.exec())




if __name__ == '__main__':
    global my_network
    my_network = n3d.Network_3D()
    global network_properties
    # Update the corresponding network property based on active channel
    network_properties = {
        0: 'nodes',
        1: 'edges',
        2: 'network_overlay',
        3: 'id_overlay'
    }

    app = QApplication(sys.argv)
    window = ImageViewerWindow()
    window.show()
    sys.exit(app.exec())

    #import traceback
    #print(traceback.format_exc())