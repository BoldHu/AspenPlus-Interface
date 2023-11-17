import os
import csv

class export():
    def __init__(self, aspen, result_material_list=[], stream_ids=['10']) -> None:
        self.result_folder_path = r'D:\python_workspace\continuous_process\data'
        self.result_file_name = "Result.csv"
        self.setting_parameter_file_name = "Setting_parameter.csv"
        self.aspen = aspen
        self.result_material_list = result_material_list
        self.setting_parameter = []
        self.stream_result = []
        self.stream_ids = stream_ids
        self.total_result = 0 # total mass flow rate of result_material_list
        
    def save_result(self, folder_name):
        self.result_folder_path = r'D:\python_workspace\continuous_process\data'
        # Save the results to a CSV file
        
        # initial the setting parameter list and stream result list
        self.initial_all_result_list()
        
        # Read the material list from the text file
        self.read_result_material_list()
        
        # Get the input setting parameters
        self.getting_parameters()
        
        # Read the stream results
        self.read_stream_result()
        
        # Check if folder exists; if not, create it
        self.result_folder_path = os.path.join(self.result_folder_path, folder_name)
        if not os.path.exists(self.result_folder_path):
            os.makedirs(self.result_folder_path)

        # Save the result to the data folder
        result_path = os.path.join(self.result_folder_path, self.result_file_name)

        with open(result_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stream_ID", "Component", "Mass_flow_rate_kg/hr"])  # Writing headers
            writer.writerows(self.stream_result)  # Writing data
            
        # save the setting parameter to the data folder
        setting_parameter_file_name = "Setting_parameter.csv"
        setting_parameter_path = os.path.join(self.result_folder_path, setting_parameter_file_name)
        with open(setting_parameter_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Setting_parameter", "Value"])  # Writing headers
            writer.writerows(self.setting_parameter)  # Writing data
        return self.stream_result, self.setting_parameter

    def read_result_material_list(self):
        # read the .txt file of properties_material_list to the list
        with open('result_material_list.txt', 'r') as f:
            for line in f:
                self.result_material_list.append(line.strip())
        return self.result_material_list

    def getting_parameters(self):
        # get the input settiing parameters
        for i in range(1, 5):
            path_SEC = f"Data\Blocks\SEC{str(i)}\Input"
            path_HEAT = f"Data\Blocks\HEAT{str(i)}\Input"
            
            node_SEC_PRES = self.aspen.Tree.FindNode(path_SEC + "\PRES")
            node_HEAT_PRES = self.aspen.Tree.FindNode(path_HEAT + "\PRES")
            node_HEAT_TEMP = self.aspen.Tree.FindNode(path_HEAT + "\TEMP")
            
            # append to list with the name of SEC and HEAT and value of PRES and TEMP
            self.setting_parameter.append([f"SEC{i}_Pressure", node_SEC_PRES.Value])
            self.setting_parameter.append([f"HEAT{i}_Temperature", node_HEAT_PRES.Value])
            self.setting_parameter.append([f"HEAT{i}_Temperature", node_HEAT_TEMP.Value])
        self.setting_parameter.append(["FLOW", self.aspen.Tree.FindNode("\Data\Streams\FEED-101\Input\TOTFLOW\MIXED").Value])
        self.setting_parameter.append(['Split_fraction', self.aspen.Tree.FindNode(r"\Data\Blocks\B3\Input\FRAC\14").Value])
        # get the oil-hydrogen ratio
        mass_hydrogen = self.aspen.Tree.FindNode(r"\Data\Streams\15\Output\MASSFLOW\MIXED\HYDROGEN").Value
        mass_all_flow = self.aspen.Tree.FindNode(r"\Data\Streams\30\Output\MASSFLMX\MIXED").Value
        hydrogen_ratio = mass_hydrogen / mass_all_flow
        self.setting_parameter.append(['Oil_hydrogen_ratio', hydrogen_ratio])
        return self.setting_parameter

    def read_stream_result(self):
        self.total_result = 0
        for stream_id in self.stream_ids:
            for material in self.result_material_list:
                try:
                    path = f"Data\Streams\{stream_id}\Output\MASSFLOW3\{material}"
                    node = self.aspen.Tree.FindNode(path)
                    if node is None:
                        raise ValueError(f"Could not find node at path {path}")
                    mass_flow_rate = node.Value
                    self.total_result += mass_flow_rate
                    self.stream_result.append([stream_id, material, mass_flow_rate])
                except Exception as e:
                    print(f"Could not retrieve data for stream {stream_id}. Error: {e}")
        self.stream_result.append(['Total', 'Total', self.total_result])
        # save the result of feed_flow_rate / total_result
        all_flow = self.aspen.Tree.FindNode(r"\Data\Streams\30\Output\MASSFLMX\MIXED").Value
        self.stream_result.append(['Aromatic Yield', 'Aromatic Yield',  self.total_result / all_flow])
    
    def initial_all_result_list(self):
        # initial the setting parameter list and stream result list
        self.setting_parameter = []
        self.stream_result = []
        self.result_material_list = []
    
    def save_stream_temp(self, strem_temp):
        # save the stream temperature to the data folder
        stream_temp_file_name = "Stream_temp.csv"
        stream_temp_path = os.path.join(self.result_folder_path, stream_temp_file_name)
        with open(stream_temp_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stream_ID", "Temperature"])
            writer.writerows(strem_temp)
        return strem_temp
    
    def save_SEC_temp(self, SEC_react_temp):
        # save the SEC temperature to the data folder by format [SEC1, 0.0, 10.0]
        SEC_temp_file_name = "SEC_temp.csv"
        SEC_temp_path = os.path.join(self.result_folder_path, SEC_temp_file_name)
        with open(SEC_temp_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["SEC", "TMIN", "TMAX"])
            writer.writerows(SEC_react_temp)
        return SEC_react_temp

    def save_hydrogen_ratio(self, ratio_list):
        # save the hydrogen ratio to the data folder by format [SEC1, 0.0, 10.0]
        hydrogen_ratio_file_name = "Hydrogen_ratio.csv"
        hydrogen_ratio_path = os.path.join(self.result_folder_path, hydrogen_ratio_file_name)
        print(hydrogen_ratio_path)
        with open(hydrogen_ratio_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Split_fraction', 'mass_hydrogen', 'mass_all_flow', 'ratio'])
            writer.writerows(ratio_list)
        print('save hydrogen ratio successfully')
        return ratio_list
    
    def save_old_result(self, folder_name):
        self.result_folder_path = r'D:\python_workspace\continuous_process\data'
        # Save the results to a CSV file
        
        # initial the setting parameter list and stream result list
        self.initial_all_result_list()
        
        # Read the material list from the text file
        self.read_result_material_list()
        
        # Get the input setting parameters
        self.getting_parameters()
        
        # Read the stream results
        self.read_stream_result()
        
        # Check if folder exists; if not, create it
        self.result_folder_path = os.path.join(self.result_folder_path, folder_name)
        if not os.path.exists(self.result_folder_path):
            os.makedirs(self.result_folder_path)

        # Save the result to the data folder
        result_path = os.path.join(self.result_folder_path, self.result_file_name)

        with open(result_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stream_ID", "Component", "Mass_flow_rate_kg/hr"])  # Writing headers
            writer.writerows(self.stream_result)  # Writing data
            
        # save the setting parameter to the data folder
        setting_parameter_file_name = "Setting_parameter.csv"
        setting_parameter_path = os.path.join(self.result_folder_path, setting_parameter_file_name)
        with open(setting_parameter_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Setting_parameter", "Value"])  # Writing headers
            writer.writerows(self.setting_parameter)  # Writing data
        return self.stream_result, self.setting_parameter