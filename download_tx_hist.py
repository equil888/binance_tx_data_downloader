from binance.client import Client
from datetime import datetime
import dateparser
import pytz
import time
import json
from pathlib import Path
#--for Google Cloud Storage ----# 
from google.cloud import storage
from os import listdir, remove
from os.path import isfile, join
from google.oauth2 import service_account

DATA_FOLDER = "data"
LAST_UPLOAD_FILE = "{}//download.cfg".format(str(Path().absolute()))

#====== Main Program Here ======================
# Running Once Daily --
# Pairs Data To be Retrieved --> on download.cfg
#===============================================

with open(LAST_UPLOAD_FILE, 'r') as f:
    symbols = json.load(f)
client = Client("","")
stop_dt = datetime.utcnow().strftime('%d %b %Y 00:00')
last_dt =  datetime.utcnow().strftime('%d %b %Y 00:01')
i=0
for symbol in symbols:
    start_dt  = symbol[1]
    #print(symbol[0], "-", symbol[1])
    hist_data = client.get_historical_klines(symbol[0], Client.KLINE_INTERVAL_1MINUTE, start_dt, stop_dt)
    with open(
        "{}//{}//Binance_{}_{}_{}-{}.json".format(str(Path().absolute()), DATA_FOLDER, 
            symbol[0],
            '1MIN',
            str(start_dt).replace(" ", "_").replace(":", ""),
            str(stop_dt).replace(" ", "_").replace(":", "")
        ),
        'w'  # set file write mode
    ) as f:
        print("Downloading {}...".format(f.name) )
        f.write(json.dumps(hist_data))
    #update last download
    symbols[i][1] = last_dt
    i = i+1
print("--- done downloading ---")

#save last time download info ========
with open(LAST_UPLOAD_FILE, 'w') as f:
    json.dump(symbols, f)

#======== move file to cloud storage ============
# Google Cloud Storage
bucketName = 'cryptoexchangedata'
bucketFolder = 'klines_1min'
#Data
localFolder = "{}//{}//".format(str(Path().absolute()), DATA_FOLDER)
storage_client = storage.Client.from_service_account_json('gcs.json')
bucket = storage_client.get_bucket(bucketName)

files = [f for f in listdir(localFolder) if isfile(join(localFolder, f))]
for file in files:
    if file.endswith("json"):
        localFile = localFolder + file
        blob = bucket.blob(bucketFolder + '/' + file)
        blob.upload_from_filename(localFile)
        print("Uploading {} to Google Storage...".format(file) )
        remove(localFile)
print("--- done uploading ---")