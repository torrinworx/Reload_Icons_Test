import bpy


class MainPanel(bpy.types.Panel):
    bl_idname = "reload_icons_test.main_panel"
    bl_label = "Main Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Reload Icons Test'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label("Hello World!", icon_value=custom_icons["BAR_CHART_CDG"].icon_id)
        # ^^ How do I get 'custom_icons' in this file?