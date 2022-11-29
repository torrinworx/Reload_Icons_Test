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

# Blender Modules
import bpy

# Python Modules
import os
import importlib

# Local Modules
import main_panel

# Refresh Local Modules For Development
if "bpy" in locals():
    modules = {
        "main_panel": main_panel,
    }

    for i in modules:
        if i in locals():
            importlib.reload(modules[i])

# Local Imports
from .main_panel import MainPanel


classes = (
    MainPanel,
)

custom_icons = None


def register():
    # Custom Icons
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), '../icons')

    for icon in os.listdir(icons_dir):
        name, extension = os.path.splitext(os.path.basename(icon))
        if extension == ".png":
            custom_icons.load(name, icon, 'IMAGE')

    # Classes
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    # Custom Icons
    global custom_icons
    bpy.utils.previews.remove(custom_icons)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
