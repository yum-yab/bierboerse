import sys
import pyqtgraph as pg  # type: ignore

import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

from bierboerse.boerse.market import Market
from bierboerse.gui.stock_list import StockListWidget
from bierboerse.gui.stock_plots import PlotRepresentation, PlotWindow


class BierboerseMainWindow(QMainWindow):
    def __init__(self, market: Market) -> None:
        super().__init__()

        self.market = market

        self.setWindowTitle("Bierbörse!")

        # button = QPushButton("Press for getting started!")
        
        button = QPushButton("Buy Random!")
        button.clicked.connect(self.buy_random)

        root_widget = QWidget()

        layout = QHBoxLayout()

        root_widget.setLayout(layout)

        self.plot_widget = PlotWindow(market, PlotRepresentation.ALL_IN_ONE)

        layout.addWidget(self.plot_widget)

        layout.addWidget(StockListWidget(self.market))
        layout.addWidget(button)
        
        self.setCentralWidget(root_widget)

    def buy_random(self):

        updated_stock = random.choice(self.market.stocks)

        self.market.buy(updated_stock)

        self.plot_widget.update_plot()
