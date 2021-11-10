import sys
import pandas as pd
sys.path.append("C:\\Users\\User\\Work\\auto_trading\\auto_trading")
from raw_data import RawData 

class DataMart(RawData):
    
    @property
    def data_mart(self):
        close = RawData(self.name, self.nationality, self.date,self.days).time_series_data['close']
        close_5 = close[0:5]
        
        signal = []
        for i in range(1,len(close_5)):
            if close_5.iloc[4-i] >= close_5.iloc[5-i]:
                signal.append(1)
            else:
                signal.append(0)
        signal.reverse()
        
        if close[4] > close[5]:
            signal.append(1)
        else:
            signal.append(0)
        
        df = pd.DataFrame({'close': close_5,
                          'signal': signal})
        return df
    