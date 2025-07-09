#import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV and skip the Ticker row
df = pd.read_csv("nasdaq_1990_1995.csv", skiprows=[1])

# Rename 'Price' to 'Date'
df = df.rename(columns={'Price': 'Date'})

# Drop rows where Date == 'Date'
df = df[df['Date'] != 'Date']

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Sort by date
df = df.sort_values('Date')

# Plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='NASDAQ Close', color='green')
plt.title("NASDAQ Composite Index (1990–1995)")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
