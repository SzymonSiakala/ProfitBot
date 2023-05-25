'''
ProfitBot
Automated stock trading using machine learning and real-time data.
By: Szymon Siąkała
'''

# API KEY: QTJZYOOX54TQGK74


import requests

api_key = "QTJZYOOX54TQGK74"
symbol = "IBM"

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
response = requests.get(url)
data = response.json()

# Extract the stock price from the response
stock_price = data['Global Quote']['05. price']
print(f"The current stock price of {symbol} is {stock_price}")


# import polygon

# client = polygon.StocksClient(api_key="bp5FA7nAIp2aZFwNn1IdFUzwUlwcYaKY")

# ticker = "AMD"

# current_price = client.get_daily_open_close(ticker, date="2023-05-24")
# print(f'Current price for AMD is {current_price}')

# current_price = client.get_current_price(ticker)
# print(f'Current price for AMD is {current_price}')

# ticker = "AAPL"

# # List Aggregates (Bars)
# bars = client.get_aggs(ticker=ticker, multiplier=1, timespan="hour", from_="2023-05-24", to="2023-05-25")
# for bar in bars:
#     print(bar)