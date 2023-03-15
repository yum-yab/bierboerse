import sys
import pyqtgraph as pg


from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class BierboerseMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bierbörse!")

        # button = QPushButton("Press for getting started!")
        
        data_arr = [0.2, 0.3, 0.25, 0.4, 0.5, 0.7]

        plot_widget = pg.PlotWidget()

        plot_widget.plot(data_arr)
        self.setCentralWidget(plot_widget)


