from PyQt6.QtWidgets import QWidget, QVBoxLayout

from bierboerse.boerse.market import Market
from bierboerse.gui.stock_widget import StockWidget




class StockListWidget(QWidget):

    def __init__(self, market: Market) -> None:
        super().__init__()

        layout = QVBoxLayout()

        #self.setStyleSheet("border: 1px solid red")
        self.market = market

        for stock in self.market.stocks:

            layout.addWidget(StockWidget(stock))

        self.setLayout(layout)


    def update_list(self) -> None:

        for widget in self.children():

            if isinstance(widget, StockWidget):
                widget.update_stock()
