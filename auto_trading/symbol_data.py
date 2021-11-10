"""SymbolData class is included.
"""

import sys
#from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
sys.path.append("C:\\Users\\User\\Work\\auto_trading\\auto_trading")
from name import Name 

class SymbolData(Name):
    
    """Module to get stock symbol.
    In this class, we get stock symbol with using  yahoo finance api2 and yahoo finance api2 exception
    
    Args:
        same as Name
    
    Typical usage example:
    symbol_data = self.get_symbol_data
    """
    
    def get_symbol_data():
        """Function to get long enough data.
        It is copied from Yahoo Finance API homepage.
        """
        try:
            symbol_data = self.get_my_share.get_historical(
                share.PERIOD_TYPE_WEEK, 30,
                share.FREQUENCY_TYPE_DAY, 1)
        except YahooFinanceError as e:
            print(e.message)
            sys.exit(1)
            
        return symbol_data
    