import bpy
from icon_manager import IconManager


class MainPanel(bpy.types.Panel):
    bl_idname = "reload_icons_test.main_panel"
    bl_label = "Main Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Reload Icons Test'

    icon_manager = IconManager()

    def draw_header(self, context):
        layout = self.layout
        layout.template_icon(icon_value=self.icon_manager.get_icon_id('BAR_CHART_CDG'))

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Hello World!", icon="INFO")

        row = layout.row()
        row.label(text="Hello World!", icon_value=self.icon_manager.get_icon_id('PIE_CHART_CDG'))
