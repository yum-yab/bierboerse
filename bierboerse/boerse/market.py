from typing import Callable
from bierboerse.boerse.stock import Stock
from typing import List

from bierboerse.utils.updater import StockUpdater


class Market:
    def __init__(
        self,
        stocks: List[Stock],
        stock_updater: StockUpdater,
        reverse_order: bool = True,
    ) -> None:
        self.__stocks = stocks
        self.stock_updater = stock_updater
        self.__reverse_ordering = reverse_order

    def __update_stock_order(self) -> None:
        """Sorts the stock order in place by current price"""
        self.__stocks.sort(reverse=self.__reverse_ordering)

    def buy(self, bought_stock: Stock) -> None:
        self.stock_updater.update(bought_stock, self.__stocks)
