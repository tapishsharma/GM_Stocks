import wget

# URL of the ZIP file
url = "https://nsearchives.nseindia.com/content/historical/EQUITIES/2022/SEP/cm15SEP2022bhav.csv.zip"

try:
    # Download the file to the current working directory
    downloaded_file = wget.download(url)
    print(f"File '{downloaded_file}' downloaded successfully.")
except Exception as e:
    print(f"Failed to download the file: {str(e)}")
