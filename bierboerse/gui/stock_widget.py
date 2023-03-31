from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout

from bierboerse.boerse.stock import Stock
from bierboerse.gui.color_box import ColorBox




class StockWidget(QWidget):

   
    def __init__(self, stock: Stock) -> None:

        super(StockWidget, self).__init__()

        root_layout = QHBoxLayout()


        name_layout = QHBoxLayout()


        name_layout.addWidget(ColorBox(stock.color))

        name_layout.addWidget(QLabel(stock.name))

        root_layout.addLayout(name_layout)

        root_layout.addWidget(QLabel(f"{stock.get_current_price():.2f} €"))

        self.setLayout(root_layout)
