from decimal import Decimal

from PyQt6.QtGui import QColor
from bierboerse.utils.FixedLengthQueue import CircularQueue

from typing import List, Optional


class Stock:
    """A stock represents one traced thing"""

    def __init__(
            self, name: str, color: QColor, history_length: int, *initial_values: Decimal
    ) -> None:
        self.__queue = CircularQueue(history_length, *initial_values)

        self.name = name

        self.color = color

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Stock):
            return self.name == __value.name
        else:
            return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Stock):
            return self.get_current_price() < other.get_current_price()
        else:
            return True

    def get_current_price(self) -> Decimal:
        """Returns the current price of the stock as Decimal"""

        last_val = self.__queue.get()

        if last_val:
            return last_val
        else:
            return Decimal(0)

    def update(self, value: Decimal) -> None:
        """Adds the passed value to the latest value and puts the result in the queue"""
        last = self.__queue.get()

        if last:
            self.__queue.put(last + value)
        else:
            self.__queue.put(value)

    def get_data(self) -> List[float]:

        return [float(i) for i in self.__queue.get_content()]
