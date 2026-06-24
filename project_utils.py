
import sheet_utils as sheet_ut


class Project:
    def __init__(self, name):
        self.name = name
        self.project_sheets = [ ]
        self.sheet_count = 0
        self.selected_sheet = None

        self.create_sheet("Sheet 1")

    def create_sheet(self, sheet_name):
        new_sheet = sheet_ut.Sheet(sheet_name)
        self.project_sheets.append(new_sheet)
        self.sheet_count += 1



