bl_info = {
    "name": "Reload_Icons_Test",
    "author": "Torrin Leonard, This Cozy Studio Inc.",
    "version": (0, 0, 1),
    "blender": (3, 3, 1),
    "location": "View3D",
    "description": "",
    "support": "COMMUNITY",
    "category": "Development",
}

# #cbcbcb

# Blender Modules
import bpy

# Python Modules
import os
import sys
import importlib

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Local Imports
import icon_manager

# Refresh Locals for development:
if "bpy" in locals():
    modules = {
        "icon_manager": icon_manager,
    }

    for i in modules:
        if i in locals():
            importlib.reload(modules[i])

from .icon_manager import IconManager

icon_manager = IconManager()


class MainPanel(bpy.types.Panel):
    bl_idname = "reload_icons_test.main_panel"
    bl_label = "Main Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Reload Icons Test'

    def draw_header(self, context):
        layout = self.layout
        layout.template_icon(icon_value=icon_manager.get_icon_id('BAR_CHART_CDG'))

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row()
        row.label(text="Hello World!", icon="INFO")

        row = layout.row()
        row.label(text="Hello World!", icon_value=icon_manager.get_icon('PIE_CHART_CDG').icon_id)

        # ^^ How do I get 'custom_icons' in this file?


classes = (
    MainPanel,
)


def register():
    # icons_dir = bpy.path.abspath(os.path.join(os.path.dirname(__file__), 'icons'))

    # Custom Icons
    icon_manager.load_icons()

    # Classes
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    # Custom Icons
    icon_manager.remove_icons()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
