"""Name class is included.
"""

import pandas as pd
from yahoo_finance_api2 import share

class Name:
    """Module to get stock name.
    In this class, we get stock informaiton from yahoo finance api2 by adding company name
    
    Args:
        name: company's name
        nationality: listed country
    
    Typical usage example:
        my_share = Name(name, nationality).get_my_share
    """
    
    def __init__(self, name: str, nationality: str):
        self.name = name
        self.nationality = nationality 
    def add_suffix_tse(self)-> str:
        
        """Function to get Japanese stock's name properly.
        If nationality is Japan, add '.T' at the end of name
        """
        
        if self.nationality == 'JP':
            if self.name[-2:] != '.T':
                self.name += '.T'
                
    def get_my_share(self)-> yahoo_finance_api2.share.Share:
    
        """Function to get information from yahoo finance api2.
        You can get stock datas by adding company name
        """
        
        self.add_suffix_tse
        my_share = share.Share(self.name)
        symbol_data = None
        
        return my_share
    