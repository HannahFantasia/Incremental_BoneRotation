bl_info = {
    "name": "Incremental bone rotation",
    "author": "Hannah Ümit <twitter.com/HannahUmit>",
    "version": (1,0),
    "blender": (2, 80, 0),
    "category": "Edit",
    "location": "3D Viewport",
    "description": "Incremental bone rotation EAT SHIT PUSSIES, formula by Sas van Gulik, implemented by yours truly",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

import bpy

from rna_prop_ui import rna_idprop_ui_create 

bpy.types.PoseBone.Zrotationincrement = bpy.props.FloatProperty(
    name="Degrees",
    description='Amount of degrees that you want to incrementally rotate in the X axis',
    default=10,
    min=0,
    soft_max=360,
    )

class IncrementalBoneRotation(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "select.incrementalbonerotation_operator"
    bl_label = "Incremental Bone Rotation"
    bl_options = {'REGISTER', 'UNDO'}
    
    x_rotincui: bpy.props.BoolProperty(
        name="X",
        description='Amount of degrees that you want to incrementally rotate in the X axis',
        default=False,
        )

    # y_rotincui: bpy.props.BoolProperty(
        # name="Y",
        # description='Amount of degrees that you want to incrementally rotate in the Y axis',
        # default=True,
        # )

    z_rotincui: bpy.props.BoolProperty(
        name="Z",
        description='Amount of degrees that you want to incrementally rotate in the Z axis',
        default=False,
        )
        
    def execute(self, context):
        
        obj = context.active_pose_bone
        
        if self.x_rotincui:
            
            obj.rotation_mode = 'XYZ'
            rna_idprop_ui_create(
                obj,
                "increments", 
                default = 10,
                min=0, max=360,
                soft_min=None, soft_max=None,
                description="Amount of degrees that you want to incrementally rotate in the X axis",
                overridable=False,
                subtype=None,
                )
            Xpath = obj.path_from_id() + "[\"increments\"]"
            
            
            #create driver
            
            Xdriver = obj.driver_add("rotation_euler", 0)
            
            Xdriver.driver.type = 'SCRIPTED'
            Xdriver.driver.use_self = True
            Xdriver.driver.expression = "floor( self.rotation_euler.x /  float (radians(increment_rot))  ) * (radians(increment_rot))"
            
            #change driver variable properties
            Xvar = Xdriver.driver.variables.new()
            
            Xvar.name = 'increment_rot'
            Xvar.type = 'SINGLE_PROP'
            
            Xvar.targets[0].id = bpy.context.active_object
            Xvar.targets[0].data_path = Xpath
            
            
        # if self.y_rotincui:
            
            # #bpy.context.active_pose_bone.Yrotationincrement = 10
            # #Ypath = bpy.context.active_pose_bone.path_from_id("Yrotationincrement")
            
            
            # #create driver
            # bpy.context.active_pose_bone.rotation_mode = 'XYZ'
            
            # Ydriver = bpy.context.active_pose_bone.driver_add("rotation_euler", 1)
            
            # Ydriver.driver.type = 'SCRIPTED'
            # Ydriver.driver.use_self = True
            # Ydriver.driver.expression = "floor( self.rotation_euler.y /  float (radians(increment_rot))  ) * (radians(increment_rot))"
            
            # #change driver variable properties
            # Yvar = Ydriver.driver.variables.new()
            
            # Yvar.name = 'increment_rot'
            # Yvar.type = 'SINGLE_PROP'
            
            # Yvar.targets[0].id = bpy.context.active_object
            # #Yvar.targets[0].data_path = Ypath
            
            
        if self.z_rotincui:
            
            bpy.context.active_pose_bone.Zrotationincrement = 10
            Zpath = bpy.context.active_pose_bone.path_from_id("Zrotationincrement")
            
            
            #create driver
            bpy.context.active_pose_bone.rotation_mode = 'XYZ'
            
            Zdriver = bpy.context.active_pose_bone.driver_add("rotation_euler", 2)
            
            Zdriver.driver.type = 'SCRIPTED'
            Zdriver.driver.use_self = True
            Zdriver.driver.expression = "floor( self.rotation_euler.z /  float (radians(increment_rot))  ) * (radians(increment_rot))"
            
            #change driver variable properties
            Zvar = Zdriver.driver.variables.new()
            
            Zvar.name = 'increment_rot'
            Zvar.type = 'SINGLE_PROP'
            
            Zvar.targets[0].id = bpy.context.active_object
            Zvar.targets[0].data_path = Zpath
            
        return {'FINISHED'}

blender_classes = [
    IncrementalBoneRotation,
]


def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)
        
        
def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)
        
        
if __name__ == "__main__":
    register()
    
    