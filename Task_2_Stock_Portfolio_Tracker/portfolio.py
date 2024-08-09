import os
import pandas as pd
import requests
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

@dataclass
class Stock:
    symbol: str
    shares: int

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, symbol: str, shares: int):
        stock = self.get_stock(symbol)
        if stock:
            stock.shares += shares
        else:
            self.stocks.append(Stock(symbol, shares))

    def remove_stock(self, symbol: str, shares: int):
        stock = self.get_stock(symbol)
        if stock:
            if stock.shares > shares:
                stock.shares -= shares
            else:
                self.stocks.remove(stock)
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def get_stock(self, symbol: str):
        return next((stock for stock in self.stocks if stock.symbol == symbol), None)

    def get_portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            try:
                price = self.get_stock_price(stock.symbol)
                total_value += price * stock.shares
            except Exception as e:
                print(f"Error getting price for {stock.symbol}: {str(e)}")
        return total_value

    def get_stock_price(self, symbol: str):
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            raise ValueError(f"Unable to fetch price for {symbol}")