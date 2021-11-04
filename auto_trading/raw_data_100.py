import pandas as pd
from yahoo_finance_api2 import share

class RawData:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
    
    @property
    def time_series_data(self):
        if self.nationality == 'JP':
            if self.name[-2:] != '.T':
                self.name += '.T'
            else:
                pass
        else:
            pass
        my_share = share.Share(self.name)
        symbol_data = None

        try:
            symbol_data = my_share.get_historical(
                share.PERIOD_TYPE_WEEK, 30,
                share.FREQUENCY_TYPE_DAY, 1)
        except YahooFinanceError as e:
            print(e.message)
            sys.exit(1)

        df = pd.DataFrame(symbol_data)
        df["datetime"] = pd.to_datetime(df.timestamp, unit="ms")
        df = df.iloc[::-1,1:][0:100]
        return df
    
    if __name__ == '__main__':
        __init__()
        time_series_data()