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
1. Make 
