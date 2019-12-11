from time import perf_counter
start = perf_counter()

import click
from datetime import timedelta
from osm_graphml_downloader import osm_graphml_downloader

@click.command()
@click.option('-x', '--network_type', help = 'Network type: "walk", "bike", "drive", "drive_service", "all", "all_private", "none"')
@click.option('-o', '--out_dir', help = 'Path to directory where you want the results to go')
@click.option('-f', '--filename', default = None)
@click.option('-n', '--north')
@click.option('-s', '--south')
@click.option('-e', '--east')
@click.option('-w', '--west')
@click.option('--reproject', is_flag = True, help = 'Option to reproject the graph from WGS84 to something else')
@click.option('--epsg_code', help = 'EPSG code value. Only used if --reproject flag is used', default = 2264)
def main(network_type, out_dir, filename, north, south, east, west, reproject, epsg_code):
    osm_graphml_downloader(network_type = network_type,
                         out_dir = out_dir,
                         filename = filename,
                         bbox = [float(west), float(south), float(east), float(north)],
                         reproject = reproject,
                         epsg_code = float(epsg_code))

    end = perf_counter()
    completion_seconds = end - start
    print(f"Elapsed time: {timedelta(seconds = completion_seconds)}")

if __name__ == "__main__":
    main()