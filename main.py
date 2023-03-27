import random


class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def update_price(self):
        self.price = round(self.price * (1 + random.uniform(-0.05, 0.05)), 2)

    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError("Insufficient stock available for purchase")
        self.quantity -= quantity

    def sell(self, quantity):
        self.quantity += quantity

    def __str__(self):
        return f"{self.symbol} - ${self.price} - {self.quantity} shares available"


class Portfolio:
    def __init__(self):
        self.stocks = {}
        self.balance = 0

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def remove_stock(self, symbol):
        del self.stocks[symbol]

    def buy_stock(self, symbol, quantity):
        if symbol not in self.stocks:
            raise ValueError("Stock not found in portfolio")
        stock = self.stocks[symbol]
        cost = stock.price * quantity
        if self.balance < cost:
            raise ValueError("Insufficient balance for purchase")
        self.balance -= cost
        stock.buy(quantity)

    def sell_stock(self, symbol, quantity):
        if symbol not in self.stocks:
            raise ValueError("Stock not found in portfolio")
        stock = self.stocks[symbol]
        if stock.quantity < quantity:
            raise ValueError("Insufficient stock available for sale")
        revenue = stock.price * quantity
        self.balance += revenue
        stock.sell(quantity)
        if stock.quantity == 0:
            self.remove_stock(symbol)

    def update_stocks(self):
        for stock in self.stocks.values():
            stock.update_price()

    def __str__(self):
        return f"Portfolio:\nBalance: ${self.balance}\n" + "\n".join(str(stock) for stock in self.stocks.values())


def main():
    # create some sample stocks
    stocks = [Stock("AAPL", 130.64, 100), Stock("GOOG", 1922.44, 50), Stock("MSFT", 235.99, 75)]

    # create a portfolio and add the stocks
    portfolio = Portfolio()
    for stock in stocks:
        portfolio.add_stock(stock)

    # simulate trading
    for i in range(10):
        print(f"\nTrading day {i + 1}")
        portfolio.update_stocks()
        print(portfolio)
        try:
            portfolio.buy_stock("AAPL", random.randint(1, 10))
            portfolio.sell_stock("GOOG", random.randint(1, 10))
        except ValueError as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    main()
