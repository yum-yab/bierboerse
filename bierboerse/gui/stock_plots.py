from abc import abstractmethod
from typing import Dict
import pyqtgraph as pg

from bierboerse.boerse.market import Market
from bierboerse.boerse.stock import Stock



from PyQt6.QtWidgets import QGridLayout, QWidget




class StockPlotWidget(QWidget):

    def __init__(self, market: Market) -> None:
        super(StockPlotWidget, self).__init__()


        self.market = market

        self.init_plot()

    @abstractmethod
    def init_plot(self) -> None:
        """Initializes the plot depending on the type"""

        




    @abstractmethod    
    def update_plot(self) -> None:
        """Updates the plot for a specific implementation"""



class AllInOnePlot(StockPlotWidget):
   
    plot_widget: pg.PlotWidget

    def init_plot(self) -> None:

        layout = QGridLayout()

        self.plot_widget = pg.PlotWidget()

        for stock in self.market.stocks:
            
            pen = pg.mkPen(color=stock.color)

            self.plot_widget.plot(stock.get_data(), pen=pen)
        
        layout.addWidget(self.plot_widget)
        
        self.setLayout(layout)

    
    def update_plot(self) -> None:
        
        for stock in self.market.stocks:
            
            pen = pg.mkPen(color=stock.color)

            self.plot_widget.plot(stock.get_data(), pen=pen)


class OneForEachPlotWidget(StockPlotWidget):


    plot_map : Dict[Stock, pg.PlotWidget]

    
    def init_plot(self) -> None:
        
        layout = QGridLayout() 

        self.plot_map = {}

        for stock in self.market.stocks:

            self.plot_map[stock] = pg.PlotWidget()

            pen = pg.mkPen(color=stock.color)

            self.plot_map[stock].plot(stock.get_data(), pen=pen)

            layout.addWidget(self.plot_map[stock])


        self.setLayout(layout)



    def update_plot(self) -> None:
        for stock, plot in self.plot_map.items():

            pen = pg.mkPen(color=stock.color)

            plot.plot(stock.get_data(), pen=pen)
