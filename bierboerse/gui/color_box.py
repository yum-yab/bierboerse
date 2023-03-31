from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget 
from PyQt6.QtGui import QPalette

class ColorBox(QWidget):

    def __init__(self, color: QColor) -> None:
        super(ColorBox, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, color)
        self.setPalette(palette)
