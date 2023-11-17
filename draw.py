import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import re
import numpy as np

# read the folder name in data
folder_name_list = []
for i in os.listdir('data'):
    if os.path.isdir(os.path.join('data', i)):
        folder_name_list.append(i)

def plot_figure(equipment_name, equipment_id, stream_id, operation):
    # operation is 'PRES' or 'TEMP'
    # equipment_name is 'SEC' or 'HEAT'
    # equipment_id is 1, 2, 3, 4
    # stream_id is 10 or 14
    # read the folder's Result.csv of equipment_name with same id to a pandas dataframe
    result = pd.DataFrame()
    dfs = []
    for name in folder_name_list:
        if re.match(f'{equipment_name}_{operation}{equipment_id}_value=', name):
            value = name.split('=')[1]
            path = os.path.join('data', name, 'Result.csv')
            df = pd.read_csv(path)
            df['value'] = value
            dfs.append(df)
    result = pd.concat(dfs, ignore_index=True)
    # plot figure for the result of stream_id by matplotlib. The value is the x-axis and the mass flow rate is the y-axis.
    if isinstance(stream_id, str):
        stream_id = int(stream_id)
    df_stream = result.loc[result['Stream_ID'] == stream_id].copy()
    df_stream['value'] = df_stream['value'].astype(float)
    df_stream['Mass_flow_rate_kg/hr'] = df_stream['Mass_flow_rate_kg/hr'].astype(float)
    plt.figure()
    # every component draw a line in the figure and draw the value point in the figure
    for component in df_stream['Component'].unique():
        df_component = df_stream.loc[df_stream['Component'] == component].copy()
        plt.plot(df_component['value'], df_component['Mass_flow_rate_kg/hr'], label=component)
        plt.scatter(df_component['value'], df_component['Mass_flow_rate_kg/hr'])
    plt.legend()
    plt.xlabel(f'{equipment_name}{equipment_id}_{operation}')
    plt.ylabel('Mass_flow_rate_kg/hr')
    plt.title(f'{equipment_name}{equipment_id}_{operation}_stream_{stream_id}')
    # save the figure
    path = os.path.join('figure', f'{equipment_name}{equipment_id}_{operation}_stream_{stream_id}.png')
    plt.savefig(path)
    plt.close()
    
# # draw the figure of SEC
# for i in range(1, 5):
#     plot_figure('SEC', i, 10, 'PRES')
#     plot_figure('SEC', i, 14, 'PRES')

# # draw the figure of HEAT
# for i in range(1, 5):
#     plot_figure('HEAT', i, 10, 'TEMP')
#     plot_figure('HEAT', i, 14, 'TEMP')
    
#     plot_figure('HEAT', i, 10, 'PRES')
#     plot_figure('HEAT', i, 14, 'PRES')
     
# match the figure of eruipment with same operatioin
def match_figure(equipment_name, operation):
    for stream_id in [10, 14]:
        fix, ax = plt.subplots(2, 2, figsize=(10, 10))
        plot_figure(equipment_name, 1, stream_id, operation)
        plot_figure(equipment_name, 2, stream_id, operation)
        plot_figure(equipment_name, 3, stream_id, operation)
        plot_figure(equipment_name, 4, stream_id, operation)
        # save the figure
        path = os.path.join('figure', f'{equipment_name}_{operation}_stream_{stream_id}_summary.png')
        plt.savefig(path)

def plot_merge_figure(equipment_name, stream_id, operation):
    # operation is 'PRES' or 'TEMP'
    # equipment_name is 'SEC' or 'HEAT'
    # stream_id is 10 or 14
    # read the folder's Result.csv of equipment_name with same id to a pandas dataframe
    
    # draw in subplots
    fig, ax = plt.subplots(2, 2, figsize=(10, 10))
    
    for equipment_id in range(1, 5):
        result = pd.DataFrame()
        dfs = []
        for name in folder_name_list:
            if re.match(f'{equipment_name}_{operation}{equipment_id}_value=', name):
                value = name.split('=')[1]
                path = os.path.join('data', name, 'Result.csv')
                df = pd.read_csv(path)
                df['value'] = value
                dfs.append(df)
        result = pd.concat(dfs, ignore_index=True)
        # plot figure for the result of stream_id by matplotlib. The value is the x-axis and the mass flow rate is the y-axis.
        if isinstance(stream_id, str):
            stream_id = int(stream_id)
        df_stream = result.loc[result['Stream_ID'] == stream_id].copy()
        df_stream['value'] = df_stream['value'].astype(float)
        df_stream['Mass_flow_rate_kg/hr'] = df_stream['Mass_flow_rate_kg/hr'].astype(float)
        
        # every component draw a line in the figure and draw the value point in the figure
        for component in df_stream['Component'].unique():
            df_component = df_stream.loc[df_stream['Component'] == component].copy()
            ax[(equipment_id - 1) // 2, (equipment_id - 1) % 2].plot(df_component['value'], df_component['Mass_flow_rate_kg/hr'], label=component)
            ax[(equipment_id - 1) // 2, (equipment_id - 1) % 2].scatter(df_component['value'], df_component['Mass_flow_rate_kg/hr'])
        ax[(equipment_id - 1) // 2, (equipment_id - 1) % 2].set_xlabel(f'{equipment_name}{equipment_id}_{operation}')
        ax[(equipment_id - 1) // 2, (equipment_id - 1) % 2].set_ylabel('Mass_flow_rate_kg/hr')
    
    # set the title of the figure
    fig.suptitle(f'{equipment_name}_{operation}_stream_{stream_id}')
    # set the legend of the figure in figure, the four subplots have the same legend
    legend = fig.legend(*ax[0, 0].get_legend_handles_labels(), loc='upper right')
    # save the figure
    path = os.path.join('figure', f'Summary_{equipment_name}{equipment_id}_{operation}_stream_{stream_id}.png')
    plt.savefig(path)

# draw the figure of SEC
plot_merge_figure('SEC', 10, 'PRES')
plot_merge_figure('SEC', 14, 'PRES')

# draw the figure of HEAT
plot_merge_figure('HEAT', 10, 'TEMP')
plot_merge_figure('HEAT', 14, 'TEMP')

plot_merge_figure('HEAT', 10, 'PRES')
plot_merge_figure('HEAT', 14, 'PRES')

# draw the Strem_temp.csv in data
def plot_strem_temp():
    # draw the histogram of stream temp, x-axis is the Stream-id and y-axis is the value of stream temp
    # read the stream temp in data
    stream_temp = pd.read_csv('./data/Stream_temp.csv')
    # draw the bar of stream temp
    category = stream_temp['Stream_ID'].copy()
    x = np.arange(len(category))
    y = stream_temp['Temperature'].copy()
    plt.figure()
    plt.bar(x, y, width=0.5, color='blue')
    plt.plot(x, y, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    plt.xticks(x, category)
    plt.xlabel('Stream_ID')
    plt.ylabel('Stream_temp')
    plt.title('Stream_temp_change_process')
    plt.savefig('figure/Stream_temp_change_process.png')
    plt.close()

# plot_strem_temp()

def plot_SEC_react_temp():
    # the data is like: SEC,TMIN,TMAX
    # read the SEC_react_temp in data
    SEC_react_temp = pd.read_csv('./data/SEC_temp.csv')
    
    # draw the bar of SEC_react_temp
    x = np.arange(len(SEC_react_temp['SEC']))
    y1 = SEC_react_temp['TMIN'].copy()
    y2 = SEC_react_temp['TMAX'].copy()
    
    plt.figure()
    plt.bar(x, y1, width=0.5, color='blue', label='TMIN')
    plt.plot(x, y1, color='red', marker='o', linestyle='dashed', linewidth=2, markersize=12)
    plt.plot(x, y2, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12, label='TMAX')
    
    plt.xticks(x, SEC_react_temp['SEC'])
    plt.xlabel('SEC')
    plt.ylabel('SEC_react_temp')
    
    # Adjust the legend's location, size, and position
    plt.legend(loc='upper left', fontsize='small', bbox_to_anchor=(1, 1))
    
    plt.title('SEC_react_temp_change_process')
    plt.tight_layout()
    plt.savefig('figure/SEC_react_temp_change_process.png', bbox_inches='tight')
    plt.close()

# plot_SEC_react_temp()


# draw the picture of FLOWRATE
def plot_single_paramter(parameter_name, stream_id):
    # the data is like Stream_ID,Component,Mass_flow_rate_kg/hr
    result = pd.DataFrame()
    dfs = []
    for name in folder_name_list:
        if re.match(f'{parameter_name}_value=', name):
            value = name.split('=')[1]
            path = os.path.join('data', name, 'Result.csv')
            df = pd.read_csv(path)
            df['value'] = value
            dfs.append(df)
    result = pd.concat(dfs, ignore_index=True)
    # plot figure for the result of by matplotlib. The value is the x-axis and the mass flow rate is the y-axis.
    df_stream = result.loc[result['Stream_ID'] == stream_id].copy()
    df_stream['value'] = df_stream['value'].astype(float)
    df_stream['Mass_flow_rate_kg/hr'] = df_stream['Mass_flow_rate_kg/hr'].astype(float)
    plt.figure()
    # every component draw a line in the figure and draw the value point in the figure
    for component in df_stream['Component'].unique():
        df_component = df_stream.loc[df_stream['Component'] == component].copy()
        plt.plot(df_component['value'], df_component['Mass_flow_rate_kg/hr'], label=component)
        plt.scatter(df_component['value'], df_component['Mass_flow_rate_kg/hr'])
    plt.legend()
    plt.xlabel(f'{parameter_name}_input')
    plt.ylabel('Mass_flow_rate_kg/hr')
    plt.title(f'{parameter_name}_input_stream_{stream_id}')
    # save the figure
    path = os.path.join('figure', f'{parameter_name}_input_stream_{stream_id}.png')
    plt.savefig(path)
    plt.close()

# plot_single_paramter('FLOWRATE', 10)
# plot_single_paramter('FLOWRATE', 14)

# draw the picture of FLOWRATE
def plot_single_paramter_name(parameter_name, stream_id, figure_name):
    # the data is like Stream_ID,Component,Mass_flow_rate_kg/hr
    result = pd.DataFrame()
    dfs = []
    for name in folder_name_list:
        if re.match(f'{parameter_name}_value=', name):
            value = name.split('=')[1]
            path = os.path.join('data', name, 'Result.csv')
            df = pd.read_csv(path)
            df['value'] = value
            dfs.append(df)
    result = pd.concat(dfs, ignore_index=True)
    # plot figure for the result of by matplotlib. The value is the x-axis and the mass flow rate is the y-axis.
    df_stream = result.loc[result['Stream_ID'] == stream_id].copy()
    df_stream['value'] = df_stream['value'].astype(float)
    df_stream['Mass_flow_rate_kg/hr'] = df_stream['Mass_flow_rate_kg/hr'].astype(float)
    plt.figure()
    # every component draw a line in the figure and draw the value point in the figure
    for component in df_stream['Component'].unique():
        df_component = df_stream.loc[df_stream['Component'] == component].copy()
        plt.plot(df_component['value'], df_component['Mass_flow_rate_kg/hr'], label=component)
        plt.scatter(df_component['value'], df_component['Mass_flow_rate_kg/hr'])
    plt.legend()
    plt.xlabel(f'{parameter_name}_input')
    plt.ylabel('Mass_flow_rate_kg/hr')
    plt.title(f'{parameter_name}_input_stream_{stream_id}')
    # save the figure
    path = os.path.join('figure', f'{figure_name}_input_stream_{stream_id}.png')
    plt.savefig(path)
    plt.close()

# plot_single_paramter_name("FLOWRATE", 10, "FLOWRATE_CHANGE_50%")
# plot_single_paramter_name("FLOWRATE", 14, "FLOWRATE_CHANGE_50%")
