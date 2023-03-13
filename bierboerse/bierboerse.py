from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

import sys


from gui.MainWindow import BierboerseMainWindow 

app = QApplication(sys.argv)

main_window = BierboerseMainWindow()
main_window.show()

# window = QPushButton("Push me!")
# 
# # windows are hidden by default
# window.show()

app.exec()
