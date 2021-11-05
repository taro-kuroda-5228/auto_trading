import datetime
import pandas as pd
from yahoo_finance_api2 import share

class RawData:
    def __init__(self, name, nationality, date, days):
        self.name = name
        self.nationality = nationality
        self.date = date
        self.days = days
    
    @property
    def time_series_data(self):
        if self.nationality == 'JP':
            if self.name[-2:] != '.T':
                self.name += '.T'
         
        my_share = share.Share('MSFT')
        symbol_data = None

        try:
            symbol_data = my_share.get_historical(
                share.PERIOD_TYPE_WEEK, 30,
                share.FREQUENCY_TYPE_DAY, 1)
        except YahooFinanceError as e:
            print(e.message)
            sys.exit(1)

        df = pd.DataFrame(symbol_data)
        df["datetime"] = pd.to_datetime(df.timestamp, unit="ms").dt.strftime('%Y-%m-%d')
        df.set_index('datetime',drop=True,inplace=True)
        df = df.sort_index(ascending=False)
        df = df.loc[self.date:str((pd.to_datetime(self.date)-datetime.timedelta(days=self.days-1)).strftime('%Y-%m-%d')),:]
        return df
    
if __name__ == '__main__':
    time_series_data()