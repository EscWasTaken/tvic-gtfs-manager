# Internal libraries and modules
import os
import io
import inspect
from pathlib import Path as LibPath
from zipfile import ZipFile

# External Libraries
import requests
import pandas as pd

frame = inspect.stack()[-1]
caller_file = frame[1]
directory = os.path.dirname(os.path.abspath(caller_file))

def getGTFS(
    URL="https://opendata.transport.vic.gov.au/dataset/3f4e292e-7f8a-4ffe-831f-1953be0fe448/resource/fb152201-859f-4882-9206-b768060b50ad/download/gtfs.zip",
    branch=2,
    filepath=None,
):
    """Downloads, Extracts, and Returns GTFS Schedule Files from Transport Victoria URL.

    Keyword arguments:
    URL -- Link to gtfs.zip download
    branch -- TVIC operational branch to use. See https://opendata.transport.vic.gov.au/dataset/gtfs-schedule
    filepath -- Path to download and store GTFS zip, leave as None for memory only operations.
    """

    res = requests.get(URL, params={"user-agent": "tvic-gtfs-manager/" + __version__})

    res.raise_for_status()  # Will raise an error if code is 4xx or 5xx

    if filepath != None:
        LibPath(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(LibPath(filepath), mode="wb") as gtfs_zip:
            gtfs_zip.write(res.content)

        archive = ZipFile(LibPath(filepath), mode="r")
        with open("output.zip", "wb") as f:
            f.write(archive.read("2/google_transit.zip"))

        sub_archive = ZipFile("output.zip", mode="r")

    else:
        archive = ZipFile(io.BytesIO(res.content), mode="r")
        sub_archive = ZipFile(
            archive.open(str(branch) + "/google_transit.zip"), mode="r"
        )

    gtfs_data = {}
    for name in sub_archive.namelist():
        with sub_archive.open(name) as f:
            gtfs_data[name.split(".")[0]] = pd.read_csv(f, low_memory=False)

    return gtfs_data
