bl_info = {
    "name": "Nok Humanoid Addon",
    "author": "Nok Animation Studios",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Generates a humanoid stylized character with different properties that can be tuned.",
    "warning": "",
    "doc_url": "",
    "category": "",
}


import bpy
from random import randint
from bpy.types import (Panel, Operator)


class ButtonOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "generate.1"
    bl_label = "Simple Humanoid Generator"

    def execute(self, context):
        for i in range(50):
            random_scale = randint(0, 3)
            x = randint(-40, 40)
            y = randint(-40, 40)
            z = randint(-40, 40)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=random_scale, enter_editmode=False, align='WORLD', location=(x, y, z))
            bpy.ops.object.shade_smooth()
        
        return {'FINISHED'}
            
            
class GeneratePanel(bpy.types.Panel):
    bl_label = "Humanoid Generate Panel"
    bl_idname = "OBJECT_PT_generate"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Humanoid Generator"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.operator(ButtonOperator.bl_idname, text="Generate", icon='GHOST_ENABLED')


from bpy.utils import register_class, unregister_class

def register():
    register_class(ButtonOperator)
    register_class(GeneratePanel)
    

def unregister():
    unregister_class(ButtonOperator)
    unregister_class(GeneratePanel)


if __name__ == "__main__":
    register()
