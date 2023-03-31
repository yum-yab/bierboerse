from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication

import sys
from bierboerse.boerse.market import Market
from bierboerse.boerse.stock import Stock
from bierboerse.utils.helper_funs import get_list_of_decimals
from bierboerse.utils.updater import SimpleUpdate


from gui.MainWindow import BierboerseMainWindow  # type: ignore


from decimal import Decimal

def main():
    app = QApplication(sys.argv)
    

    stocks = []

    history_length = 1000

    stocks.append(Stock("Marathonbier", QColor("#5d17ea"), history_length, *get_list_of_decimals(0.0, 3.0, 30)))

    stocks.append(Stock("Bullshit", QColor("#ea2517"), history_length, *get_list_of_decimals(0.0, 3.0, 30)))
    stocks.append(Stock("Lalala", QColor("#17ea45"), history_length, *get_list_of_decimals(0.0, 3.0, 30)))
    

    
    market = Market(stocks, SimpleUpdate(Decimal(0.7), Decimal(0.3)))

    main_window = BierboerseMainWindow(market)
    main_window.show()

    # window = QPushButton("Push me!")
    #
    # # windows are hidden by default
    # window.show()

    app.exec()


if __name__ == "__main__":
    main()
