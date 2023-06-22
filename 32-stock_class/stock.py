'''
Stock Class
'''

class Stock:
    def __init__(self, symbol, name, previous_closing_price):
        self.symbol = symbol
        self.name = name
        self.previous_closing_price = previous_closing_price
        
    