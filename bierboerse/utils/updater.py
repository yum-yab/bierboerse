import abc

from bierboerse.boerse.stock import Stock
from decimal import Decimal
from typing import List


class StockUpdater(abc.ABC):
    @abc.abstractmethod
    def update(self, bought_stock: Stock, stocks: List[Stock]) -> None:
        pass


class SimpleUpdate(StockUpdater):
    """Very basic upadte implementation. Increases price for bought stock, decreases every other item"""

    def __init__(self, up: Decimal, down: Decimal) -> None:
        self.up = up
        self.down = down

    def update(self, bought_stock: Stock, stocks: List[Stock]) -> None:
        for stock in stocks:
            if bought_stock == stock:
                stock.update(self.up)
            else:
                stock.update(-self.down)
