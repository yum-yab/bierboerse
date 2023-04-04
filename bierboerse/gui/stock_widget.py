from PyQt6.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout, QFrame

from bierboerse.boerse.stock import Stock
from bierboerse.gui.color_box import ColorBox




class StockWidget(QFrame):

   
    def __init__(self, stock: Stock) -> None:

        super(StockWidget, self).__init__()
        
        self.__setup_style()

        self.stock = stock

        root_layout = QHBoxLayout()


        name_layout = QHBoxLayout()

        name_layout.addWidget(ColorBox(self.stock.color))

        name_layout.addWidget(QLabel(self.stock.name))

        root_layout.addLayout(name_layout)
        
        self.price_label = QLabel(f"{self.stock.get_current_price():.2f} €")

        root_layout.addWidget(self.price_label)

        self.setLayout(root_layout)


    def __setup_style(self) -> None:


        self.setStyleSheet("StockWidget { background-color: rgb(255,0,0); margin:5px; border:1px solid rgb(0, 255, 0); }")

    def update_stock(self) -> None:

        self.price_label.setText(f"{self.stock.get_current_price():.2f} €")
