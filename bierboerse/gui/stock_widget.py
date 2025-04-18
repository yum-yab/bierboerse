from PyQt6.QtWidgets import QLabel, QHBoxLayout, QFrame

from bierboerse.boerse.stock import Stock
from bierboerse.gui.color_box import ColorBox




class StockWidget(QFrame):

   
class StockWidget(QWidget):
    def __init__(self, stock: Stock) -> None:
        super(StockWidget, self).__init__()
        
        self.__setup_style_sheet()

        self.stock = stock

        root_layout = QHBoxLayout()

        name_layout = QHBoxLayout()

        name_layout.addWidget(ColorBox(self.stock.color))

        name_layout.addWidget(QLabel(self.stock.name))

        root_layout.addLayout(name_layout)
        
        self.price_label = QLabel(f"{self.stock.get_current_price():.2f} €")

        root_layout.addWidget(self.price_label)

        self.setLayout(root_layout)


    def __setup_style_sheet(self) -> None:


        self.setStyleSheet("StockWidget { margin:5px; border:1px solid black; }")

    def update_stock(self) -> None:

        self.price_label.setText(f"{self.stock.get_current_price():.2f} €")
