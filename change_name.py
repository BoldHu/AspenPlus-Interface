import os
import pandas
import re
# change all Result.csv second column name to 'Component' and third column name to 'Mass_flow_rate_kg/hr' in data folder
for i in os.listdir('data'):
    # open csv file
    # read with id in first column
    df = pandas.read_csv(os.path.join('data', i, 'Result.csv'))
    if len(df.columns) == 3:
        print(i, 'has been changed')
        print(df.columns)
        pass
    elif len(df.columns) == 2:
        # set the index as a column and name it as 'Component'
        print(i, 'has not been changed')
        print(df.columns)
        df = df.reset_index()
        df = df.rename(columns={'index': 'Component'})
        df.columns = ['Stream_ID', 'Component', 'Mass_flow_rate_kg/hr']
        # save the index in first column as 'Stream_ID'
        df.to_csv(os.path.join('data', i, 'Result.csv'), index=False)
        
        
        
        