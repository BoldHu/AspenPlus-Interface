import win32com.client
from export import export
from aspen_model import aspen_model

# Step 1: Connect to Aspen Plus
aspen = win32com.client.Dispatch("Apwn.Document")

# Step 2: Open the Aspen Plus model file
model_path = r'D:\python_workspace\continuous_process\PD-P1-CNR-1.bkp'
aspen.InitFromArchive2(model_path)

# display the initial value of the setting parameter
result_stream_id = ['10']
exporter = export(aspen, stream_ids=result_stream_id)
aspen_operator = aspen_model(aspen, exporter)
aspen_operator.initial_parameter()
initial_setting_parameter = aspen_operator.setting_parameter
print(initial_setting_parameter)

# Step 3: Run the simulation
# aspen_operator.run_simulation()

# run to get stream temp
# aspen_operator.get_stream_temp()

# run to get temp of SEC
# aspen_operator.get_SEC_react_temp()

# Step 4: Change the setting parameter
aspen_operator.run_change_simulation(id_of_SEC=1)
aspen_operator.run_change_simulation(id_of_SEC=2)
aspen_operator.run_change_simulation(id_of_SEC=3)
aspen_operator.run_change_simulation(id_of_SEC=4)
aspen_operator.run_change_simulation(id_of_HEAT=1, change_operation='PRES')
aspen_operator.run_change_simulation(id_of_HEAT=1, change_operation='TEMP')
aspen_operator.run_change_simulation(id_of_HEAT=2, change_operation='PRES')
aspen_operator.run_change_simulation(id_of_HEAT=2, change_operation='TEMP')
aspen_operator.run_change_simulation(id_of_HEAT=3, change_operation='PRES')
aspen_operator.run_change_simulation(id_of_HEAT=3, change_operation='TEMP')
aspen_operator.run_change_simulation(id_of_HEAT=4, change_operation='PRES')
aspen_operator.run_change_simulation(id_of_HEAT=4, change_operation='TEMP')
# change FLOWRATE
aspen_operator.run_change_simulation(change_operation='FLOWRATE')

# change split fraction
aspen_operator.run_change_simulation(change_operation='split_fraction')

# Step 5: Close the Aspen Plus connection
aspen.Close()

# Release the COM object
del aspen
