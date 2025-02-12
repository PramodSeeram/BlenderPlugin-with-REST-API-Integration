import bpy
import requests

class SimplePanel(bpy.types.Panel):
    bl_label = "Custom UI Panel"
    bl_idname = "OBJECT_PT_simple_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        if obj:
            layout.label(text=f"Selected Object: {obj.name}")
            col = layout.column()
            col.prop(obj, "location")
            col.prop(obj, "rotation_euler")
            col.prop(obj, "scale")
            layout.prop(context.scene, "selected_endpoint")
            layout.operator("object.send_transform")

class SendTransformOperator(bpy.types.Operator):
    bl_idname = "object.send_transform"
    bl_label = "Send Data to Server"

    def execute(self, context):
        obj = context.object
        endpoint = context.scene.selected_endpoint

        if obj:
            data = {
                "name": obj.name,
                "location": list(obj.location),
                "rotation": list(obj.rotation_euler),
                "scale": list(obj.scale)
            }
            try:
                url = f"http://127.0.0.1:8000{endpoint}"
                response = requests.post(url, json=data)
                self.report({'INFO'}, f"Server Response: {response.text}")
            except Exception as e:
                self.report({'ERROR'}, f"Failed to send data: {e}")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimplePanel)
    bpy.utils.register_class(SendTransformOperator)

    bpy.types.Scene.selected_endpoint = bpy.props.EnumProperty(
        name="Endpoint",
        description="Select API endpoint",
        items=[
            ("/transform", "Transform", ""),
            ("/translation", "Translation", ""),
            ("/rotation", "Rotation", ""),
            ("/scale", "Scale", ""),
        ]
    )

def unregister():
    bpy.utils.unregister_class(SimplePanel)
    bpy.utils.unregister_class(SendTransformOperator)
    del bpy.types.Scene.selected_endpoint

if __name__ == "__main__":
    register()
