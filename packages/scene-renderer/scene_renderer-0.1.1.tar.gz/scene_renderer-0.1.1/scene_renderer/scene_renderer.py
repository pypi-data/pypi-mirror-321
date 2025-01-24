'''
The following helps in rendering a scene. 
It can be operated in following formats:
1. Rendering a scene from the front
2. Rendering a scene from the four corners
3. Rendering a scene from the top
4. A 360 degree view of the scene
5. Rendering from an arbitrary location and looking at an arbitrary target
'''
import os
import numpy as np

BLENDER_FUNCTIONS = """
import bpy
import sys
import numpy as np
from mathutils import Vector

def set_clamp_factor_to_zero():
    for material in bpy.data.materials:
        if material.use_nodes:  # Check if the material uses nodes
            for node in material.node_tree.nodes:
                # print(node.type)
                if node.type == 'MIX':
                    
                    # Set the numeric Factor (first one usually)
                    factor_input = node.inputs[0]  # Accessing the first "Factor" input
                    if factor_input.name == "Factor" and isinstance(factor_input.default_value, (int, float)):
                        factor_input.default_value = 0.0
                        print(f"Numeric Factor value set to: {factor_input.default_value}")
                    else:
                        print("Numeric Factor input not found or is not editable.")


# Set up the environment texture
def add_environment_texture(image_path):
    
    # Ensure the scene has a world
    world = bpy.context.scene.world
    if not world:
        world = bpy.data.worlds.new(name="World")
        bpy.context.scene.world = world
    
    # Enable nodes for the world
    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links

    # Clear existing nodes
    for node in nodes:
        nodes.remove(node)

    # Add a Background node
    bg_node = nodes.new(type='ShaderNodeBackground')
    bg_node.location = (0, 0)
    
    # Add an Environment Texture node
    env_texture_node = nodes.new(type='ShaderNodeTexEnvironment')
    env_texture_node.location = (-300, 0)
    env_texture_node.image = bpy.data.images.load(image_path)

    # Add a World Output node
    world_output_node = nodes.new(type='ShaderNodeOutputWorld')
    world_output_node.location = (200, 0)

    # Link nodes
    links.new(env_texture_node.outputs['Color'], bg_node.inputs['Color'])
    links.new(bg_node.outputs['Background'], world_output_node.inputs['Surface'])

def clear_scene():
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()
    bpy.ops.object.select_by_type(type='CAMERA')
    bpy.ops.object.delete()
    bpy.ops.object.select_by_type(type='LIGHT')
    bpy.ops.object.delete()

def load_scene(scene_path):
    bpy.ops.wm.open_mainfile(filepath=scene_path)

def apply_smooth_shading():
    # Apply smooth shading to all meshes
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.shade_smooth()

def save_current_scene(filepath):
    bpy.ops.wm.save_as_mainfile(filepath=filepath)

def setup_renderer_video(output_path, resolution_x=1920, resolution_y=1080, frame_rate=30, samples=100):
    render = bpy.context.scene.render
    render.engine = 'BLENDER_EEVEE_NEXT'
    render.image_settings.file_format = 'FFMPEG'
    render.ffmpeg.format = 'MPEG4'
    render.ffmpeg.codec = 'H264'
    render.ffmpeg.constant_rate_factor = 'HIGH'
    render.ffmpeg.ffmpeg_preset = 'GOOD'
    render.ffmpeg.video_bitrate = 5000
    render.resolution_x = resolution_x 
    render.resolution_y = resolution_y 
    render.resolution_percentage = 100
    render.fps = frame_rate
    render.filepath = output_path
    bpy.context.scene.cycles.samples = samples 

def setup_renderer(output_path, resolution_x=1920, resolution_y=1080, samples=100):
    render = bpy.context.scene.render
    render.engine = 'BLENDER_EEVEE_NEXT'
    render.resolution_x = resolution_x
    render.resolution_y = resolution_y
    render.filepath = output_path  # Output path
    render.image_settings.file_format = 'PNG'  # Set output format to PNG
    render.image_settings.color_mode = 'RGBA'  # Use RGBA to support transparency
    render.film_transparent = True  # Enable transparency in the render output
    bpy.context.scene.cycles.samples = samples 

def initialize_camera():
    cam_data = bpy.data.cameras.new('Camera')
    cam_ob = bpy.data.objects.new('Camera', cam_data)
    bpy.context.scene.collection.objects.link(cam_ob)
    bpy.context.scene.camera = cam_ob  # Set the camera as active
    return cam_ob

def place_camera(cam_ob, loc, looking_at):
    cx, cy, cz = loc
    point = looking_at

    cam_ob.location = Vector((cx, cy, cz))
    direction = Vector(point) - cam_ob.location
    rot_quat = direction.to_track_quat('-Z', 'Y')
    cam_ob.rotation_euler = rot_quat.to_euler()

def render_image():
    bpy.ops.render.render(write_still=True)

def animate_camera(cam_ob, cam_radius, scene_center, num_frames=360):
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = num_frames

    for frame, theta in enumerate(range(0, num_frames), start=1):
        theta_rad = np.deg2rad(theta)
        cam_ob.location = Vector((
            scene_center[0] + cam_radius * np.cos(theta_rad),
            -scene_center[1] + cam_radius * np.sin(theta_rad),
            2*scene_center[2]/3
        ))
        
        cam_ob.keyframe_insert(data_path="location", frame=frame)

    # Make the camera always face the target
    for frame in range(1, num_frames + 1):
        bpy.context.scene.frame_set(frame)
        direction = Vector(scene_center) - cam_ob.location
        rot_quat = direction.to_track_quat('-Z', 'Y')
        cam_ob.rotation_euler = rot_quat.to_euler()
        cam_ob.keyframe_insert(data_path="rotation_euler", frame=frame)
    
    
def render_video():
    bpy.ops.render.render(animation=True)
"""

class SceneRenderer:
    def __init__(self, resolution_x=1920, resolution_y=1080, samples=100, frame_rate=30, num_frames=360):
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.samples = samples
        self.frame_rate = frame_rate
        self.num_frames = num_frames
        self.tmp_dir = 'tmp'
        self.scene = f"""
{BLENDER_FUNCTIONS}        
"""

    def set_clamp_factor_to_zero(self):
        self.scene += """
set_clamp_factor_to_zero()
"""

    def add_environment_texture(self):
        def get_image_path():
            # Calculate the absolute path dynamically
            package_dir = os.path.dirname(__file__)  # Directory of the current file
            image_path = os.path.join(package_dir, "assets", "env.exr")
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image not found at {image_path}")
            return image_path

        image_path = get_image_path()

        self.scene += f"""
add_environment_texture('{image_path}')
"""

    def apply_smooth_shading(self):
        self.scene += """
apply_smooth_shading()
"""

    def load_scene(self, scene_path):
        self.scene += f"""
load_scene("{scene_path}")
"""
        
    def setup_renderer_video(self, output_path):
        self.scene += f"""
setup_renderer_video("{output_path}", {self.resolution_x}, {self.resolution_y}, {self.frame_rate}, {self.samples})
"""
        
    def setup_renderer(self, output_path):
        self.scene += f"""
setup_renderer("{output_path}", {self.resolution_x}, {self.resolution_y}, {self.samples})
"""
    
    def initialize_camera(self):
        self.scene += """
cam_ob = initialize_camera()
"""

    def place_camera(self, loc, looking_at):
        self.scene += f"""
place_camera(cam_ob, {loc}, {looking_at})
"""
        
    def render_image(self):
        self.scene += """
render_image()
"""

    def animate_camera(self, cam_radius, scene_center):
        self.scene += f"""
animate_camera(cam_ob, {cam_radius}, {scene_center}, {self.num_frames})
"""

    def render_video(self):
        self.scene += """
render_video()
"""

    def clear(self):
        """
        Removes all mesh objects from the current Blender scene.
        """
        self.scene += """
clear_scene()
"""

    def save_current_scene(self, filepath):
        self.scene += f"""
save_current_scene("{filepath}")
"""

    def run(self):
        self.save_current_scene(f'{self.tmp_dir}/scene.blend')
        import os
        import subprocess
        os.makedirs(self.tmp_dir, exist_ok=True)
        with open(f'{self.tmp_dir}/scene.py', 'w') as f:
            f.write(self.scene)
        
        BLENDER_PATH = os.getenv('BLENDER_PATH')
        # BLENDER_PATH = '/Applications/Blender.app/Contents/MacOS/Blender'        
        # Path to the Blender executable
        # Update this path according to your Blender installation

        # Path to your custom script that you want Blender to run
        current_directory = os.getcwd()
        script_path = os.path.join(current_directory,f'{self.tmp_dir}/scene.py')

        # Constructing the command to run Blender, execute the script, and pass the assetID
        command = [
            BLENDER_PATH,
            '--python', script_path,  # The path to the script Blender will run
            '--background',  # Run Blender in background mode
        ]
        # Execute the command
        try:
            subprocess.run(command, timeout=300, stdout = subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            print("Blender process exceeded the time limit and was terminated.")

    def init(self, path):
        self.clear()
        self.load_scene(path)
        self.apply_smooth_shading()
        self.initialize_camera()
        self.add_environment_texture()

    def render(self, path, output_path, location, target):
        location[1] = -location[1]
        target[1] = -target[1]
        self.init(path)
        self.place_camera(location, target)
        self.setup_renderer(output_path)
        self.render_image()
        self.run()
    
    def render_from_front(self, path, output_path, scene_dims, scene_center):
        self.init(path)

        W,D,H = scene_dims
        cx, cz, cy = scene_center
        dist = np.max([W,D,H])
        cy_ = dist*3
        cz_ = cy_*0.5

        self.place_camera((cx, -cy_, cz_), (cx, -cz, cy))
        self.setup_renderer(output_path)
        
        self.render_image()
        self.run()

    def render_from_corners(self, path, output_paths, scene_dims, scene_center):
        self.init(path)

        W,D,H = scene_dims
        cx, cz, cy = scene_center
        cz = -cz

        corners = [
        ((cx+W/2, cz-D/2, H),  (cx, cz, 0)),  # Camera at (0, 0, h) looking at (w, d, 0)
        ((cx+W/2, cz+D/2, H), (cx, cz, 0)),  # Camera at (w, 0, h) looking at (0, d, 0)
        ((cx-W/2, cz+D/2, H), (cx, cz, 0)),  # Camera at (0, d, h) looking at (w, 0, 0)
        ((cx-W/2, cz-D/2, H),  (cx, cz, 0))   # Camera at (w, d, h) looking at (0, 0, 0)
        ]
        
        for i, (camera_location, target_location) in enumerate(corners):
            self.place_camera(camera_location, target_location)
            self.setup_renderer(output_paths[i])
            self.render_image()
        
        self.run()
          
    def render_from_top(self, path, output_path, scene_dims, scene_center):
        self.init(path)

        W,D,H = scene_dims
        cx, cz, cy = scene_center
        cz = -cz
        dist = np.max([W,D,H])
        cy_ = dist*3
        cz_ = cy_*0.5

        self.place_camera((cx, cz, cy_), (cx, cz, 0))
        self.setup_renderer(output_path)
        self.render_image()
        self.run()

    def render_360(self, path, output_path, scene_dims, scene_center):
        self.init(path)

        W,D,H = scene_dims
        cam_radius = 3 * np.sqrt((W / 2) ** 2 + (D / 2) ** 2)
        self.initialize_camera()
        self.animate_camera(cam_radius, scene_center)
        self.setup_renderer_video(output_path)
        self.render_video()
        self.run()

# renderer = SceneRenderer(resolution_x=512,resolution_y=512)
# renderer.render_from_front('/Users/kunalgupta/Documents/translator/tmp2/scene.blend', 'tmp/front.png', (1,1,1), (0,0,0))
# renderer.render_from_corners('/Users/kunalgupta/Documents/translator/tmp2/scene.blend', ['tmp/corner1.png', 'tmp/corner2.png', 'tmp/corner3.png', 'tmp/corner4.png'], (2,2,4), (2,2,2))
# renderer.render_from_top('/Users/kunalgupta/Documents/translator/tmp2/scene.blend', 'tmp/top.png', (2,1,1), (0.5,0.4,0.5))
# renderer.render_360('/Users/kunalgupta/Documents/translator/tmp2/scene.blend', 'tmp/360.mp4', (2,2,3), (2,2,1.5))
# renderer.render('/Users/kunalgupta/Documents/translator/tmp2/scene.blend', 'tmp/render.png', (1,1,1), (0,0,0))
