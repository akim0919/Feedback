from openpyxl import load_workbook

load_wb = load_workbook("/Users/seinkim/Documents/Eyetracking/Eyetracking Metrics_이호석_set1357.xlsx", data_only=True)

load_ws = load_wb['Sheet1']

print(load_ws['F15'].value)