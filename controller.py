import pandas as pd
import pyexcel as px

def extractCSV(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        if not file.endswith(".csv"):
            return "Provide CSV file only"
        
        return f"There is error in extracted data from CSV file:\n{e}"
        
    

def intoExcel(data, dest):
    try:
        data_dict = data.to_dict(orient='records')
        px.save_as(records=data_dict, dest_file_name=dest)
        return True
    except Exception as e:
        return f"There is an issue saving to Excel:\n{e}"
    