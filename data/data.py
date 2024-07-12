import yfinance as yf

#fecthes the stock data from yahoo finance
def fetch(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval='1mo')
    stock_data.to_csv(f'{ticker}.csv')

if __name__ == "__main__":
    stock = 'AAPL'
    start_date = '2000-01-01'
    end_date = '2023-12-31'

    fetch(stock, start_date, end_date)
    print("done")