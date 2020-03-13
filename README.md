# binance_tx_data_downloader
Download cryptocurrency trading history data (Binance Exchange) via Python wrapper, pushed to Google Cloud Storage 

*****************************************************************************
Credit to: https://github.com/sammchardy Python Wrapper for Binance Exchange.
*****************************************************************************
Data Flow: Binance API --> Transaction data history (OHLC data) in .json file format --> upload to Google Cloud Storage
*****************************************************************************
Google Cloud Storage Authentication: Access to Google Storage by service account key, read the docs here: https://google-cloud-python.readthedocs.io/en/0.32.0/core/auth.html
*****************************************************************************

How to Use
**********
1. Edit file download.cfg to include crypto pairs which transaction data you want to retrieve.
[["BTCUSDT", "11 Mar 2020 00:01"], ["ETHUSDT", "11 Mar 2020 00:01"], ["LINKUSDT", "11 Mar 2020 00:01"]]
Following the symbol is the date (in UTC) which will be used as starting date data to be retrieved.
Period : Starting Date up to Today 00:00. 
So, if you want to download data from 1 Jan 2019 --> put "1 Jan 2019 00:00" right after the pair symbol.

2. Prepare Google Cloud Storage:
From Cloud Console, create a cloud storage bucket, and a folder under this bucket. Make a note of the bucket name and the folder name.
Edit file download_tx_hist.py goto line 54, replace bucket name and folder with yours.
Prepare Cloud storage credential:
From Google Cloud Console - API & Services - Credential - Create Credential (select Service Account).
Don't forget to assign access/permission to a role (e.g Project Owner). Download the credential as json file --> give this file name gcs.json

3. Running the program:
   pyhton download_tx_hist.py

Here's what the program do:
- read file download.cfg into a list (pairs and start date)
- loop the pair list and call Binance API to download kline/candle data --> store on folder /data/
- update start_date on file download.cfg with today's date hour 00:01 for each time a pair finish download 
(this last update period is to enabling continous daily batching process, thus this download_tx_hist.py ideally should run daily, using crobjob or windows task scheduler)
- download data files then pushed uploaded into Google Cloud Storage
(it is intended to be later ingested into Google Big Query or Cloud SQL)

********

Any issues or questions, just ping me at my telegram @roytbr
