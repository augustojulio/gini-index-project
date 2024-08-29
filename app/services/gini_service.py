import os
import pandas as pd
from app.models import db, GiniIndex
import pyexcel as p

class GiniService:
    def __init__(self, data_dir='data/'):
        self.data_dir = data_dir

    def process_files(self):
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.XLS'):
                filepath = os.path.join(self.data_dir, filename)
                print(filepath)
                if not os.path.exists(filepath):
                    raise FileNotFoundError(f"O arquivo {filepath} não foi encontrado.")
                self.process_file(filepath)
                
    def process_file(self, filepath):
        try:
            print(f"Processingg file: {filepath}")
            
            sheet = p.get_sheet(file_name=filepath)
            data = sheet.to_array()
            
            # Extrai o cabeçalho
            header = data[0]
            year = header[0]  # Assume que o ano é o primeiro cabeçalho
            
            for row in data[1:]:
                city_state = row[0].split(" - ")
                state = city_state[-1] if len(city_state) > 1 else None
                city = city_state[0]
                gini_value = row[1]

                if gini_value is not None:
                    self.save_to_db(state, city, year, gini_value)

        except FileNotFoundError:
            print(f"Error: The file {filepath} does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred while processing the file {filepath}: {e}")
                
    # def process_file(self, filepath):
        try:
            print(f"Processing file: {filepath}")
            df = pd.read_excel(filepath, engine='openpyxl')
            print(f"File loaded successfully: {filepath}")

            if df.empty:
                print(f"Warning: The file {filepath} is empty.")
                return

            # Assuming the first column header is the year
            year = df.columns[0]
            print(f"Year identified: {year}")

            for _, row in df.iterrows():
                city_state = row[0].split(" - ")
                state = city_state[-1] if len(city_state) > 1 else None
                city = city_state[0]
                gini_value = row[1]

                print(f"Processing city: {city}, state: {state}, gini_value: {gini_value}")

                if pd.notna(gini_value):
                    self.save_to_db(state, city, year, gini_value)
                else:
                    print(f"Skipping row with missing Gini value: {row}")

        except FileNotFoundError:
            print(f"Error: The file {filepath} does not exist.")
        except ValueError as ve:
            print(f"ValueError: {ve} - There might be an issue with the format or content of the file: {filepath}")
        except Exception as e:
            print(f"An unexpected error occurred while processing the file {filepath}: {e}")


    # def process_file(self, filepath):
    #     print('entrou aqui 2')
    #     df = pd.read_excel(filepath, engine='openpyxl')
    #     year = df.columns[0]  # assuming the first column header is the year
    #     for _, row in df.iterrows():
    #         city_state = row[0].split(" - ")
    #         state = city_state[-1] if len(city_state) > 1 else None
    #         city = city_state[0]
    #         gini_value = row[1]
    #         if pd.notna(gini_value):
    #             self.save_to_db(state, city, year, gini_value)
    
    
    def save_to_db(self, state, city, year, gini_value):
        gini_record = GiniIndex(state=state, city=city, year=year, gini_value=gini_value)
        db.session.add(gini_record)
        db.session.commit()
