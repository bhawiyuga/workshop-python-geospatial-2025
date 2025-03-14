required_data_url = [
    "https://figshare.com/ndownloader/files/37729413",
    "https://figshare.com/ndownloader/files/37729416",
    "https://figshare.com/ndownloader/files/37729419"
]

# Download and placed it to data folder
import os

data_folder = os.path.abspath("data")
# Do the download using urllib
for url in required_data_url:
    # Download using curl
    os.system(f"curl -O -J -L {url} --output-dir {data_folder}/")