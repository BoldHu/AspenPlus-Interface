import pandas as pd
import os

# if the .csv file has value of 'C9N', move the folder to drop_data folder
def move_data():
    # read the folder name in the data folder
    folder_name = []
    for i in os.listdir('data'):
        folder_name.append(i)
    for name in folder_name:
        # read the .csv file
        file_path = os.path.join('data', name, 'Result.csv')
        df = pd.read_csv(file_path)
        # check if the value of 'C9N' in the .csv file
        if 'C9N' in df['Component'].values:
            # move the folder to drop_data folder
            os.rename(os.path.join('data', name), os.path.join('drop_data', name))
            print(f'{name} has been moved to drop_data folder')

def check_C9N():
    # check if the value of 'C9N' in the .csv file
    folder_name = []
    for i in os.listdir('data'):
        folder_name.append(i)
    for name in folder_name:
        # read the .csv file
        file_path = os.path.join('data', name, 'Result.csv')
        df = pd.read_csv(file_path)
        # check if the value of 'C9N' in the .csv file
        if 'C9N' in df['Component'].values:
            # move the folder to drop_data folder
            os.rename(os.path.join('data', name), os.path.join('drop_data', name))
            print(f'{name} has been moved to drop_data folder')
        else:
            print(f'{name} has no C9N')
check_C9N()
        