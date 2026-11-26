"""Presentation render of the winch drum (PHO-21).

Run after cad/winch_drum.py:
    blender -b --python cad/render_winch_drum.py
Writes out/winch_drum_render.png (kept small: 960 x 720, few samples).
"""

import math
from pathlib import Path

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parent.parent
STL = ROOT / "out" / "winch_drum.stl"
PNG = ROOT / "out" / "winch_drum_render.png"
RES_X, RES_Y = 960, 720
SAMPLES = 32

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

bpy.ops.wm.stl_import(filepath=str(STL))
drum = bpy.context.selected_objects[0]
drum.scale = (0.001, 0.001, 0.001)  # mm -> m
bpy.ops.object.select_all(action="DESELECT")
drum.select_set(True)
bpy.context.view_layer.objects.active = drum
bpy.ops.object.shade_auto_smooth(angle=math.radians(30))
# drum axis is Z in the CAD; lay it horizontally along X, centred, resting on the floor
drum.rotation_euler = (0, math.radians(90), 0)
drum.location = (-0.034, 0, 0.032)

mat = bpy.data.materials.new("aluminium")
mat.use_nodes = True
bsdf = mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Base Color"].default_value = (0.80, 0.81, 0.83, 1)
bsdf.inputs["Metallic"].default_value = 1.0
bsdf.inputs["Roughness"].default_value = 0.35
drum.data.materials.append(mat)

bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 0, 0))
floor = bpy.context.active_object
fmat = bpy.data.materials.new("floor")
fmat.use_nodes = True
fmat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.12, 0.13, 0.15, 1)
fmat.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.6
floor.data.materials.append(fmat)

world = bpy.data.worlds.new("w")
world.use_nodes = True
world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.18, 0.20, 0.24, 1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.5
scene.world = world

for loc, energy in (((0.25, -0.25, 0.35), 8), ((-0.3, -0.1, 0.25), 3), ((0, 0.3, 0.3), 4)):
    bpy.ops.object.light_add(type="AREA", location=loc)
    light = bpy.context.active_object
    light.data.energy = energy
    light.data.size = 0.2
    light.rotation_euler = (Vector((0, 0, 0.03)) - Vector(loc)).to_track_quat("-Z", "Y").to_euler()

bpy.ops.object.camera_add(location=(0.13, -0.17, 0.12))
cam = bpy.context.active_object
cam.data.lens = 60
cam.rotation_euler = (Vector((0, 0, 0.03)) - cam.location).to_track_quat("-Z", "Y").to_euler()
scene.camera = cam

scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = SAMPLES
scene.cycles.use_denoising = True
scene.render.resolution_x = RES_X
scene.render.resolution_y = RES_Y
scene.render.filepath = str(PNG)
scene.view_settings.view_transform = "AgX"
bpy.ops.render.render(write_still=True)
print(f"wrote {PNG}")
