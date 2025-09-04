import openpyxl

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)

    def get_data(self, sheet_name):
        sheet = self.workbook[sheet_name]
        data = []

        # Skip header row
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)

        return data
