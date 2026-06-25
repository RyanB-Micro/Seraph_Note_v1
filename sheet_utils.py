
import project_style as proj_style

class Sheet:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.screen_width = proj_style.WIDTH
        self.screen_height = proj_style.HEIGHT
        self.node_list = []
        self.fact_list = []
        self.source_list = []
        self.quote_list = []
        self.bond_list = []
        self.tools_list = []
        self.tool_choices = [("New_Node", proj_style.SERAPH), ("New_Fact", proj_style.VISION_AZURE),
                             ("New_Quote", proj_style.BLUE_82), ("New_Source", proj_style.MINT_2x128)]

