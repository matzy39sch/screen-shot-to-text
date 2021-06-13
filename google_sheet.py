import pygsheets
import pandas as pd

def write_to_sheet(service_file, data, sheet_name, sheet_index, start_x_y):
    work_sheet = auth_and_open_sheet(service_file, sheet_name)
    work_sheet[sheet_index].set_dataframe(create_data_frame(data), start_x_y)

def create_data_frame(text):
    data = text.split("\n")
    return pd.DataFrame(data=data)

def auth_and_open_sheet(service_file, spread_sheet_name):
    gc = pygsheets.authorize(service_file=service_file)
    return gc.open(spread_sheet_name)
