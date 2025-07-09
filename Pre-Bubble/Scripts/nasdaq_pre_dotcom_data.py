#import libraries

import yfinance as yf
import pandas as pd

# Define the NASDAQ Composite Index symbol
symbol = "^IXIC"  # NASDAQ Composite Index on Yahoo Finance

# Set the date range
start_date = "1990-01-01"
end_date = "1995-12-31"

# Download the data
nasdaq_data = yf.download(symbol, start=start_date, end=end_date)

# Save to CSV
nasdaq_data.to_csv("nasdaq_1990_1995.csv")

#outro
print("NASDAQ data downloaded and saved as 'nasdaq_1990_1995.csv'")
