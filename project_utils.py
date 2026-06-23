
class Project():
    def __init__(self):
        self.project_sheets = [None]

    def create_sheet(self, sheet_name):
        new_sheet = Sheet(sheet_name)
        self.project_sheets.append(new_sheet)



class Sheet():
    def __init__(self, sheet_name):
        self.sheet_name = "Test"