import pyqtgraph as pg
from enum import Enum

from bierboerse.boerse.market import Market


class PlotRepresentation(Enum):

    ALL_IN_ONE = 0
    ONE_FOR_EACH = 1


from PyQt6.QtWidgets import QGridLayout, QWidget




class PlotWindow(QWidget):

    def __init__(self, market: Market, plot_representation: PlotRepresentation) -> None:
        super().__init__()


        self.market = market
        
        
        layout = QGridLayout()

        self.setLayout(layout)

        
        if plot_representation == PlotRepresentation.ALL_IN_ONE:
            
            plot_widget = pg.PlotWidget()

            for stock in self.market.stocks:
                
                pen = pg.mkPen(color=stock.color)

                plot_widget.plot(stock.get_data(), pen=pen)
        
        elif plot_representation == PlotRepresentation.ONE_FOR_EACH:
            
            pass
        else:
            
            pass

        
        






