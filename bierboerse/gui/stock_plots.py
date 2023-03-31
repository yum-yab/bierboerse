import pyqtgraph as pg
from enum import Enum

from bierboerse.boerse.market import Market


class PlotRepresentation(Enum):

    ALL_IN_ONE = 0
    ONE_FOR_EACH = 1


from PyQt6.QtWidgets import QGridLayout, QWidget




class PlotWindow(QWidget):

    def __init__(self, market: Market, plot_representation: PlotRepresentation) -> None:
        super(PlotWindow, self).__init__()


        self.market = market
        
        self.__plot_repr = plot_representation
        

        self.init_plot()
        
    def init_plot(self):
        """Initializes the plot depending on the type"""
        layout = QGridLayout()

        
        match self.__plot_repr:
            case PlotRepresentation.ALL_IN_ONE:
    
                self.plot_widget = pg.PlotWidget()

                for stock in self.market.stocks:
                    
                    pen = pg.mkPen(color=stock.color)

                    self.plot_widget.plot(stock.get_data(), pen=pen)
                
                layout.addWidget(self.plot_widget)

            case PlotRepresentation.ONE_FOR_EACH:

                self.plot_map = {}

                for stock in self.market.stocks:

                    self.plot_map[stock] = pg.PlotWidget()

                    pen = pg.mkPen(color=stock.color)

                    self.plot_map[stock].plot(stock.get_data(), pen=pen)

                    layout.addWidget(self.plot_map[stock])


        self.setLayout(layout)

    
    def update_plot(self):


        match self.__plot_repr:
            case PlotRepresentation.ALL_IN_ONE:
    
                for stock in self.market.stocks:
                    
                    pen = pg.mkPen(color=stock.color)

                    self.plot_widget.plot(stock.get_data(), pen=pen)
                
            case PlotRepresentation.ONE_FOR_EACH:

                for stock, plot in self.plot_map.items():

                    pen = pg.mkPen(color=stock.color)

                    plot.plot(stock.get_data(), pen=pen)


