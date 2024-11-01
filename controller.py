import pandas as pd
import pyexcel as px

def extractCSV(file):
    if not file.endswith(".csv"):
        return {
            'status': False,
            'message': "Please provide a CSV file only."
        }
    
    try:
        df = pd.read_csv(file)
        return {
            'status': True,
            'data': df
        }
    except Exception as e:
        return {
            'status': False,
            'message': f"There was an error extracting data from the CSV file:\n{e}"
        }

def intoExcel(data, dest):
    try:
        data_dict = data.to_dict(orient='records')
        px.save_as(records=data_dict, dest_file_name=dest)
        return f"Your file has been successfully saved to: {dest}"
    except Exception as e:
        return f"There is an issue saving to Excel:\n{e}"
