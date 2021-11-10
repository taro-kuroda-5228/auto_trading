"""RawData class is included.
"""

import sys
import datetime
import pandas as pd
#from yahoo_finance_api2 import share
sys.path.append("C:\\Users\\User\\Work\\auto_trading\\auto_trading")
from symbol_data import SymbolData

class RawData(SymbolData):
    
    """Module to get stock price information during the wanted duration.

    In this class, get price datas including datetime, timestamp, open, high, low, close, and volume

    Args:
        name: company's name
        nationality: listed country
        start_date: date information wanted
        days: how long days information you want before start_date

    Typical usage example:
    raw_data = RawData(name, nationality, start_date, days).time_series_data
    """
    
    def __init__(self, name: str, nationality: str, start_date: str, days: int):
        self.name = name
        self.nationality = nationality
        self.start_date = start_date
        self.days = days
        
    def preprocess_symbol_data(self)-> pd.DataFrame:
        
        """Function to get pd.DataFrame from symbol_data.
        
        return 
            columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
            index = ['datetime'], type = '%Y-%m-%d', ascending=False
            
        In this function, you can point the date from when you can get the price information before by appointing the date '%Y-%m-%d' type
        """
        
        df = pd.DataFrame(self.get_symbol_data)
        df["datetime"] = pd.to_datetime(df.timestamp, unit="ms").dt.strftime('%Y-%m-%d')
        df.set_index('datetime',drop=True,inplace=True)
        df = df.sort_index(ascending=False)
        end_date = pd.to_datetime(self.start_date)-datetime.timedelta(days=self.days-1)
        end_date = end_date.strftime('%Y-%m-%d')
        df = df.loc[self.start_date:end_date,:]
        return df
    
#     def add_suffix_tse(self)-> str:
        
#         """Function only for use in time_series_data
#         If nationality is Japan, add '.T' at the end of name
#         """
        
#         if self.nationality == 'JP':
#             if self.name[-2:] != '.T':
#                 self.name += '.T'
#         return self.name

#     def end_date(self):
#        """Function only for use in time_series_data
#        """
#         df = pd.to_datetime(self.start_date)-datetime.timedelta(days=self.days-1)
#         df = df.strftime('%Y-%m-%d')
#         return df

    @property
    def time_series_data(self)-> pd.DataFrame: 
        
        """Make timeseries table.
        Please see the docstring in 'preprocess_symbol_data' function
        """
        
        df = self.preprocess_symbol_data
        return df
    
#         self.add_suffix_tse        
#         my_share = share.Share(self.name)
#         symbol_data = None
#        my_share = self.get_my_share

#         try:
#             symbol_data = my_share.get_historical(
#                 share.PERIOD_TYPE_WEEK, 30,
#                 share.FREQUENCY_TYPE_DAY, 1)
#         except YahooFinanceError as e:
#             print(e.message)
#             sys.exit(1)
#         symbol_data = self.get_symbol_data

#         df = pd.DataFrame(self.get_symbol_data)
#         df["datetime"] = pd.to_datetime(df.timestamp, unit="ms").dt.strftime('%Y-%m-%d')
#         df.set_index('datetime',drop=True,inplace=True)
#         df = df.sort_index(ascending=False)
#         end_date = pd.to_datetime(self.start_date)-datetime.timedelta(days=self.days-1)
#         end_date = end_date.strftime('%Y-%m-%d')
#         df = df.loc[self.start_date:end_date,:]      
#         return df
    
#        df = self.preprocess_symbol_data
    
#        return df
    