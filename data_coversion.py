import os
import re
import csv

        
def data_conversion():
    # read the foler name in data
    folder_name_list = []
    for i in os.listdir('data'):
        if os.path.isdir(os.path.join('data', i)):
            folder_name_list.append(i)
    SEC1_PRESS = []
    SEC2_PRESS = []
    SEC3_PRESS = []
    SEC4_PRESS = []
    HEAT1_TEMP = []
    HEAT2_TEMP = []
    HEAT3_TEMP = []
    HEAT4_TEMP = []
    FLOWRATE = []
    oil_hydrogen_ratio = []
    setting = []
    result = []
    for name in folder_name_list:
        # check SEC1 PRESS
        if re.search('SEC1_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            SEC1_PRESS.append([setting[1][1], result[-1][2]])
        
        # check SEC2 PRESS
        if re.search('SEC2_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            SEC2_PRESS.append([setting[4][1], result[-1][2]])
        
        # check SEC3 PRESS
        if re.search('SEC3_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            SEC3_PRESS.append([setting[7][1], result[-1][2]])
        
        # check SEC4 PRESS
        if re.search('SEC4_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            SEC4_PRESS.append([setting[10][1], result[-1][2]])
        
        # check HEAT1 TEMP
        if re.search('HEAT_TEMP1_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            HEAT1_TEMP.append([setting[3][1], result[-1][2]])
        
        # check HEAT2 TEMP
        if re.search('HEAT_TEMP2_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            HEAT2_TEMP.append([setting[6][1], result[-1][2]])
        
        # check HEAT3 TEMP
        if re.search('HEAT_TEMP3_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            HEAT3_TEMP.append([setting[9][1], result[-1][2]])
        
        # check HEAT4 TEMP
        if re.search('HEAT_TEMP4_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            HEAT4_TEMP.append([setting[12][1], result[-1][2]])
        
        # check FLOWRATE
        if re.search('FLOWRATE_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            FLOWRATE.append([setting[13][1], result[-1][2]])
        
        # check oil_hydrogen_ratio
        if re.search('split_fraction_value=', name):
            # read the setting and result
            setting, result = read_csv(name)
            # write the setting and result to the SEC1_PRESS
            oil_hydrogen_ratio.append([setting[15][1], result[-1][2]])
            
    # save the data to csv
    save_csv(SEC1_PRESS, 'SEC1')
    save_csv(SEC2_PRESS, 'SEC2')
    save_csv(SEC3_PRESS, 'SEC3')
    save_csv(SEC4_PRESS, 'SEC4')
    save_csv(HEAT1_TEMP, 'HEAT1')
    save_csv(HEAT2_TEMP, 'HEAT2')
    save_csv(HEAT3_TEMP, 'HEAT3')
    save_csv(HEAT4_TEMP, 'HEAT4')
    save_csv(FLOWRATE, 'FLOWRATE')
    save_csv(oil_hydrogen_ratio, 'oil_hydrogen_ratio')


def read_csv(name):
    result = []
    setting = []
        # read the setting and result
    with open(os.path.join('data', name, 'Setting_parameter.csv')) as f:
        reader = csv.reader(f)
        for row in reader:
            setting.append(row)
    with open(os.path.join('data', name, 'Result.csv')) as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(row)
    return setting, result

def save_csv(data_list, file_name):
    if file_name == 'SEC1':
        with open('SEC1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['SEC1_PRESS', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'SEC2':
        with open('SEC2.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['SEC2_PRESS', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'SEC3':
        with open('SEC3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['SEC3_PRESS', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'SEC4':
        with open('SEC4.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['SEC4_PRESS', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'HEAT1':
        with open('HEAT1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['HEAT1_TEMP', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'HEAT2':
        with open('HEAT2.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['HEAT2_TEMP', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'HEAT3':
        with open('HEAT3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['HEAT3_TEMP', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'HEAT4':
        with open('HEAT4.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['HEAT4_TEMP', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'FLOWRATE':
        with open('FLOWRATE.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['FLOWRATE', 'Aromatic Yield'])
            writer.writerows(data_list)
    elif file_name == 'oil_hydrogen_ratio':
        with open('oil_hydrogen_ratio.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['oil_hydrogen_ratio', 'Aromatic Yield'])
            writer.writerows(data_list)

data_conversion()
        
            
        
        