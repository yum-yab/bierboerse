import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class BierboerseMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bierbörse!")

        button = QPushButton("Press for getting started!")

        self.setCentralWidget(button)


