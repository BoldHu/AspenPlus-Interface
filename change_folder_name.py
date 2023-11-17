import os
import re
def change_folder_name(equipment_name, equipment_id, operation):
    # read the folder name in data
    folder_name_list = []
    for i in os.listdir('data'):
        if os.path.isdir(os.path.join('data', i)):
            folder_name_list.append(i)
    # change the fodler name which is like: {equipment_name}_{operation}_{equipment_id}_value=' in data 
    # to '{equipment_name}_{operation}_{equipment_id}_value='
    for name in folder_name_list:
        if re.search(f'{equipment_name}_{operation}_{equipment_id}_value=', name):
            value = name.split('=')[1]
            new_name = f'{equipment_name}_{operation}{equipment_id}_value={value}'
            os.rename(os.path.join('data', name), os.path.join('data', new_name))

# change the folder name of HEAT of "PRES" and "TEMP", stream 10 and 14
change_folder_name('HEAT', 1, 'PRES')
change_folder_name('HEAT', 1, 'TEMP')
change_folder_name('HEAT', 2, 'PRES')
change_folder_name('HEAT', 2, 'TEMP')
change_folder_name('HEAT', 3, 'PRES')
change_folder_name('HEAT', 3, 'TEMP')
change_folder_name('HEAT', 4, 'PRES')
change_folder_name('HEAT', 4, 'TEMP')
