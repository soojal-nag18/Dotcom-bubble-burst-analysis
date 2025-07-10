import yfinance as yf

# Define the NASDAQ Composite symbol
symbol = "^IXIC"

# Define date range for Dotcom era
start_date = "1995-01-01"
end_date = "2000-03-31"

# Download the data
nasdaq_data = yf.download(symbol, start=start_date, end=end_date, interval='1d')

# Save to CSV
nasdaq_data.to_csv("nasdaq_1995_to_dotcom_bubble.csv")

print("Downloaded NASDAQ Composite data from 1995 to March 2000 and saved to 'nasdaq_1995_to_dotcom_bubble.csv'")
