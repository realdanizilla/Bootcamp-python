import json
import pandas as pd
import os
from .FilesSources import FilesSources

class JsonSource(FilesSources):
    def __init__(self):
        self.previous_files = []
        self.combined_data = pd.DataFrame()
        self.create_path()

    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data', 'json_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.json')]

        if new_files:
            print("New JSON files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
        else:
            print("No new JSON files detected.")
            self.get_data()

    def read_json_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Erro ao acessar o JSON {e}")
            return None
    
    def get_data(self):
        data_frames = []
        for file_name in self.previous_files:
            if file_name.endswith('.json'):
                file_path = os.path.join(self.folder_path, file_name)
                json_data = self.read_json_file(file_path)
                if json_data is not None:
                   # Check if the JSON is a dictionary (scalar) or a list
                    if isinstance(json_data, dict):
                        # Wrap dictionary in a list
                        df = pd.DataFrame([json_data])
                    elif isinstance(json_data, list):
                        # Directly convert to DataFrame if it's a list of dictionaries
                        df = pd.DataFrame(json_data)
                    else:
                        print(f"Unsupported JSON structure in file: {file_name}")
                        continue
                
                    data_frames.append(df)
        if data_frames:
            self.combined_data = pd.concat(data_frames, ignore_index=True)
            print(self.combined_data)
        else:
            print("no valid json data found to consolidate")
            
        return self.combined_data
        # print(data)
        # return data