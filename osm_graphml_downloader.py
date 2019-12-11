import os
import osmnx as ox

def osm_graphml_downloader(network_type,
        out_dir,
        filename = None,
        bbox = [-78.893509, 35.677936, -78.453369, 36.028555],
        reproject = False,
        epsg_code = 2264):
    
    network_type_list = ["walk", "bike", "drive", "drive_service", "all", "all_private", "none"]
    if network_type not in network_type_list:
        raise ValueError("results: status must be one of %r." % network_type_list)

    if filename is None:
        filename = f'graph_{network_type}.graphml'
    else:
        filename_no_extension = filename.split('.')[0]
        filename = f'{filename_no_extension}.graphml'

    outgraph = os.path.join(out_dir, filename)

    print("Downloading and generating graph from OSM...")
    graph = ox.graph_from_bbox(bbox[3], bbox[1], bbox[2], bbox[0], network_type = network_type)

    if reproject:
        print(f"Reprojecting to {epsg_code}...")
        epsg_string = f'epsg:{epsg_code}'
        graph = ox.project_graph(graph, to_crs = epsg_string)
    
    print("Saving graph...")
    ox.save_graphml(graph, outgraph)

    print(f"Graph saved: {outgraph}")