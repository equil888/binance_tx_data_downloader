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

2. Prepare Google Cloud Service Account private key file :
From Google Cloud Console - API & Services - Credential - Create Credential (select Service Account).
Don't forget to give access/permission to role (e.g Project Owner). Download the credential as json file --> give this file name gcs.json

3
