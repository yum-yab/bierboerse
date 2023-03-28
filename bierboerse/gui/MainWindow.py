import sys
import pyqtgraph as pg  # type: ignore


from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

from bierboerse.boerse.market import Market
from bierboerse.gui.stock_plots import PlotRepresentation, PlotWindow


class BierboerseMainWindow(QMainWindow):
    def __init__(self, market: Market) -> None:
        super().__init__()

        self.market = market

        self.setWindowTitle("Bierbörse!")

        # button = QPushButton("Press for getting started!")

        root_widget = QWidget()

        layout = QHBoxLayout()

        root_widget.setLayout(layout)

        plot_widget = PlotWindow(market, PlotRepresentation.ALL_IN_ONE)

        layout.addWidget(plot_widget)

        
        self.setCentralWidget(root_widget)
