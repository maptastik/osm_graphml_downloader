# osm_graphml_downloader
Download zipped graphml of various network types from OpenStreetMap

## CLI
```
-x  --network_type  required  Network type: walk, bike, drive, drive_service, all, all_private, none
-o  --out_dir       required  Path to directory where you want the results to go
-f  --filename                Name of .graphml output file
-n  --north         required  Area of interest north extent
-s  --south         required  Area of interest south extent
-e  --east          required  Area of interest east extent
-w  --west          required  Area of interest west extent
--reproject                   Option to reproject graph from WGS84 to something else
--epsg_code                   EPSG code value. Only used if --reproject flag is used
```

### Usage Examples

#### Minimal Example

This example demonstrates CLI command using only the minimum required options.

```bash
python osm_graphml_downloader_cli.py -x walk -o "C:\Data Directory" -n 35.802884 -s 35.793138 -e -78.597478 -w -78.612413

# C:\Data Directory\graph_walk.graphml
```

#### All options

This example demonstrates what the CLI call would look like if set values for all the options.

```bash
python osm_graphml_downloader_cli.py -x walk -o "C:\Data Directory" -f neighborhood_walk_2264 -n 35.802884 -s 35.793138 -e -78.597478 -w -78.612413 --reproject --epsg_code 2264

# C:\Data Directory\neighborhood_walk_2264.graphml
```