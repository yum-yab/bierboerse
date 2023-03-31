from PyQt6.QtWidgets import QWidget, QVBoxLayout

from bierboerse.boerse.market import Market
from bierboerse.gui.stock_widget import StockWidget




class StockListWidget(QWidget):

    def __init__(self, market: Market) -> None:
        super().__init__()

        layout = QVBoxLayout()


        self.market = market

        for stock in self.market.stocks:

            layout.addWidget(StockWidget(stock))

        self.setLayout(layout)
