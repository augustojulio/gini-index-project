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
            print(f"Processing file: {filepath}")
            
            # Carrega a planilha usando pyexcel
            sheet = p.get_sheet(file_name=filepath)
            data = sheet.to_array()

            # Extrai o ano da primeira linha, segunda coluna (índice 1)
            year = data[0][1]

            # Percorre as linhas a partir da segunda (índice 1)
            for row in data[1:]:
                city_state = row[0].split(" - ")
                state = city_state[-1] if len(city_state) > 1 else None
                city = city_state[0]
                gini_value = row[1]

                if gini_value is not None and gini_value != '':
                    self.save_to_db(state, city, year, gini_value)

        except FileNotFoundError:
            print(f"Error: The file {filepath} does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred while processing the file {filepath}: {e}")
                    
        
    def save_to_db(self, state, city, year, gini_value):
        gini_record = GiniIndex(state=state, city=city, year=year, gini_value=gini_value)
        db.session.add(gini_record)
        db.session.commit()
