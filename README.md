# TVIC GTFS Manager

*2026, February, Release 2*

---
## About
TVIC GTFS Manager is a highly specific library for a highly specific problem. [Transport Victoria](https://transport.vic.gov.au/) (formerly PTV) [publishes GTFS schedules](https://opendata.transport.vic.gov.au/dataset/gtfs-schedule) in a horrid way in which you download a Zip, which contains folders for each mode of transport (operational branches), which contains another Zip file (unhelpfully called `google_transit.zip`), which contains the various [General Transit Feed Specification](https://gtfs.org/) files, [each of which are CSV files](https://gtfs.org/documentation/schedule/reference/) with the unhelpful extension of `.txt`.

This library hopefully solves a lot of pain of dealing with downloading and returning data for a operating branch.

## Installation
```bash
pip install tvic_gtfs_manager
```
or download from the releases

## Usage
For the simplest usage:
```python
from tvic_gtfs_manager import getGTFS
files = getGTFS()

print(files.keys())
> dict_keys(['pathways', 'transfers', 'agency', 'trips', 'calendar', 'routes', 'shapes', 'levels', 'stops', 'calendar_dates', 'stop_times'])
```
Or get a bit more nuanced:
```python
from tvic_gtfs_manager import getGTFS
from pathlib import Path as LibPath

getGTFS(
    URL="https://opendata.transport.vic.gov.au/dataset/3f4e292e-7f8a-4ffe-831f-1953be0fe448/resource/fb152201-859f-4882-9206-b768060b50ad/download/gtfs.zip", # GTFS Schedule Zip URL
    branch=2, # Metropolitan Trains
    filepath=LibPath(LibPath.cwd(), "gtfs.zip"), # Path to save to disk
    )
```

## Dependencies
This library requires [pandas](https://pandas.pydata.org/) and [Requests](https://requests.readthedocs.io/en/latest/) to function.

## License

[MIT](https://github.com/EscWasTaken/tvic-gtfs-manager/blob/main/LICENSE)
