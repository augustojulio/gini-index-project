import os
import pandas as pd
from app.models import db, GiniIndex

class GiniService:
    def __init__(self, data_dir='data/'):
        self.data_dir = data_dir

    def process_files(self):
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.xls'):
                self.process_file(os.path.join(self.data_dir, filename))

    def process_file(self, filepath):
        df = pd.read_excel(filepath, engine='openpyxl')
        year = df.columns[0]  # assuming the first column header is the year
        for _, row in df.iterrows():
            city_state = row[0].split(" - ")
            state = city_state[-1] if len(city_state) > 1 else None
            city = city_state[0]
            gini_value = row[1]
            if pd.notna(gini_value):
                self.save_to_db(state, city, year, gini_value)

    def save_to_db(self, state, city, year, gini_value):
        gini_record = GiniIndex(state=state, city=city, year=year, gini_value=gini_value)
        db.session.add(gini_record)
        db.session.commit()
