# Pandas Profiling library - credit to:
# https://github.com/pandas-profiling/pandas-profiling
# Bloddy Brillyant.

import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

# Put below code in function passing in club selection as parameter
def showClubProfile(selection):

    df = pd.read_excel('swingstats/golfstats.xlsx')
    cdf = df[df['Club'] == selection]
    cdf = cdf.drop(columns=['Club'])

    if cdf.empty:
        
        profile = ProfileReport(df, title='Swing Stats - ALL CLUBS', config_file='swingstats/min_config.yaml')
    
        return profile

    profile = ProfileReport(cdf, title=selection + ' Swing Stats', config_file='swingstats/min_config.yaml')
    
    return profile