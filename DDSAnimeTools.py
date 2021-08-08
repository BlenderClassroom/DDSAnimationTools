bl_info = {
    "name": "DDS Annimation Tools",
    "author": "Dwayne Savage",
    "version": (1, 5),
    "blender": (2, 83, 0),
    "location": "3D View->sidebar->Item tab.",
    "description": "General settings for animating.",
    "warning": "",
    "wiki_url": "http://blenderclassroom.com",
    "category": "3D View",
    }

import bpy
from bpy.types import Panel
#Tab name setting.
tab = "Item"

#Adds motion path panel to the User Input panel
class MyPath(bpy.types.Panel):
    bl_idname = "DDS_PT_mypath"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = tab
    bl_label = "Motion Paths"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        mpath = context.object.motion_path
        bs = context.active_pose_bone
        if bs:
            bones = context.active_pose_bone.motion_path
            mps = context.object.pose.animation_visualization.motion_path
        else:
            bones=False
            mps = context.object.animation_visualization.motion_path
        col = self.layout.column(align=True)
        col.prop(mps, "type", expand=True)
        col.label(text="Display Range:")
        sub = col.column(align=True)
        if mps.type == 'CURRENT_FRAME':
            sub.prop(mps, "frame_before", text="Before")
            sub.prop(mps, "frame_after", text="After")
        elif mps.type == 'RANGE':
            sub.prop(mps, "frame_start", text="Start")
            sub.prop(mps, "frame_end", text="End")
        sub.prop(mps, "frame_step", text="Step")
        if bs:
            col.label(text="Cache for Bone:")
        else:
            col.label(text="Cache:")
        if bones:
            sub = col.column(align=True)
            sub.enabled = False
            sub.prop(bones, "frame_start", text="From")
            sub.prop(bones, "frame_end", text="To")
            sub = col.row(align=True)
            sub.operator("pose.paths_update", text="Update Paths", icon='BONE_DATA')
            sub.operator("pose.paths_clear", text="", icon='X')
        elif mpath:
            sub = col.column(align=True)
            sub.enabled = False
            sub.prop(mpath, "frame_start", text="From")
            sub.prop(mpath, "frame_end", text="To")
            sub = col.row(align=True)
            sub.operator("object.paths_update", text="Update Paths", icon='OBJECT_DATA')
            sub.operator("object.paths_clear", text="", icon='X')
        else:
            sub = col.column(align=True)
            sub.label(text="Nothing to show yet...", icon='ERROR')
            if bs:
                sub.operator("pose.paths_calculate", text="Calculate...", icon='BONE_DATA')
            else:
                sub.operator("object.paths_calculate", text="Calculate...", icon='OBJECT_DATA')
        col.label(text="Show:")
        col.prop(mps, "show_frame_numbers", text="Frame Numbers")
        col.prop(mps, "show_keyframe_highlight", text="Keyframes")
        sub = col.column()
        sub.enabled = mps.show_keyframe_highlight
        if bs:
            sub.prop(mps, "show_keyframe_action_all", text="+ Non-Grouped Keyframes")
        sub.prop(mps, "show_keyframe_numbers", text="Keyframe Numbers")
        if bones:
            col.prop(bones, "lines", text="Lines")
            col.prop(bones, "line_thickness", text="Thickness")
            split = col.split(factor=0.6)
            split.prop(bones, "use_custom_color", text="Color")
            sub = split.column()
            sub.enabled = bones.use_custom_color
            sub.prop(bones, "color", text="")
        elif mpath:
            col.prop(mpath, "lines", text="Lines")
            col.prop(mpath, "line_thickness", text="Thickness")
            split = col.split(factor=0.6)
            split.prop(mpath, "use_custom_color", text="Color")
            sub = split.column()
            sub.enabled = mpath.use_custom_color
            sub.prop(mpath, "color", text="")
            
class MyPath2(bpy.types.Panel):
    bl_idname = "DDS_PT_mypath2"
    bl_space_type = "GRAPH_EDITOR"
    bl_region_type = "UI"
    bl_category = "DDS"
    bl_label = "Motion Paths"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        mpath = context.object.motion_path
        bs = context.active_pose_bone
        if bs:
            bones = context.active_pose_bone.motion_path
            mps = context.object.pose.animation_visualization.motion_path
        else:
            bones=False
            mps = context.object.animation_visualization.motion_path
        col = self.layout.column(align=True)
        col.prop(mps, "type", expand=True)
        col.label(text="Display Range:")
        sub = col.column(align=True)
        if mps.type == 'CURRENT_FRAME':
            sub.prop(mps, "frame_before", text="Before")
            sub.prop(mps, "frame_after", text="After")
        elif mps.type == 'RANGE':
            sub.prop(mps, "frame_start", text="Start")
            sub.prop(mps, "frame_end", text="End")
        sub.prop(mps, "frame_step", text="Step")
        if bs:
            col.label(text="Cache for Bone:")
        else:
            col.label(text="Cache:")
        if bones:
            sub = col.column(align=True)
            sub.enabled = False
            sub.prop(bones, "frame_start", text="From")
            sub.prop(bones, "frame_end", text="To")
            sub = col.row(align=True)
            sub.operator("pose.paths_update", text="Update Paths", icon='BONE_DATA')
            sub.operator("pose.paths_clear", text="", icon='X')
        elif mpath:
            sub = col.column(align=True)
            sub.enabled = False
            sub.prop(mpath, "frame_start", text="From")
            sub.prop(mpath, "frame_end", text="To")
            sub = col.row(align=True)
            sub.operator("object.paths_update", text="Update Paths", icon='OBJECT_DATA')
            sub.operator("object.paths_clear", text="", icon='X')
        else:
            sub = col.column(align=True)
            sub.label(text="Nothing to show yet...", icon='ERROR')
            if bs:
                sub.operator("pose.paths_calculate", text="Calculate...", icon='BONE_DATA')
            else:
                sub.operator("object.paths_calculate", text="Calculate...", icon='OBJECT_DATA')
        col.label(text="Show:")
        col.prop(mps, "show_frame_numbers", text="Frame Numbers")
        col.prop(mps, "show_keyframe_highlight", text="Keyframes")
        sub = col.column()
        sub.enabled = mps.show_keyframe_highlight
        if bs:
            sub.prop(mps, "show_keyframe_action_all", text="+ Non-Grouped Keyframes")
        sub.prop(mps, "show_keyframe_numbers", text="Keyframe Numbers")
        if bones:
            col.prop(bones, "lines", text="Lines")
            col.prop(bones, "line_thickness", text="Thickness")
            split = col.split(factor=0.6)
            split.prop(bones, "use_custom_color", text="Color")
            sub = split.column()
            sub.enabled = bones.use_custom_color
            sub.prop(bones, "color", text="")
        elif mpath:
            col.prop(mpath, "lines", text="Lines")
            col.prop(mpath, "line_thickness", text="Thickness")
            split = col.split(factor=0.6)
            split.prop(mpath, "use_custom_color", text="Color")
            sub = split.column()
            sub.enabled = mpath.use_custom_color
            sub.prop(mpath, "color", text="")

#sets up the animation panel
class DDSAnime:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = tab
    bl_label = "Animation Tools"

#populates animation panel with main buttons and options    
class DDSTools(DDSAnime, Panel):

    @classmethod
    def poll(self, context):
        try:
            return (True)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        scene = context.scene
        col = self.layout.column(align=True)
        row = col.row(align=True)
        row.operator("screen.frame_jump", text="", icon='REW').end = False
        row.operator("screen.keyframe_jump", text="", icon='PREV_KEYFRAME').next = False
        if not context.screen.is_animation_playing:
            if scene.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
                sub = row.row(align=True)
                #sub.scale_x = 2.0
                sub.operator("screen.animation_play", text="", icon='PLAY')
            else:
                row.operator("screen.animation_play", text="", icon='PLAY_REVERSE').reverse = True
                row.operator("screen.animation_play", text="", icon='PLAY')
        else:
            sub = row.row(align=True)
            sub.scale_x = 1.4
            sub.operator("screen.animation_play", text="", icon='PAUSE')
        row.operator("screen.keyframe_jump", text="", icon='NEXT_KEYFRAME').next = True
        row.operator("screen.frame_jump", text="", icon='FF').end = True
        col.prop(context.tool_settings, 'keyframe_type', text='')
        row = col.row(align=True)
        row.prop(context.tool_settings, "use_keyframe_insert_auto", text="", toggle=True)
        if context.tool_settings.use_keyframe_insert_auto:
            row.prop(context.tool_settings, "use_keyframe_insert_keyingset", text="", toggle=True)
            if context.screen.is_animation_playing and not context.user_preferenes.edit.use_keyframe_insert_available:
                subsub = row.row(align=True)
                subsub.prop(toolsettings, "use_record_with_nla", toggle=True)
        row.prop(scene, "use_preview_range", text="")
        row = col.row(align=True)
        row.prop_search(scene.keying_sets_all, "active", scene, "keying_sets_all", text="")
        row.operator("anim.keyframe_insert", text="", icon='KEY_HLT')
        row.operator("anim.keyframe_delete", text="", icon='KEY_DEHLT')
        col.prop(scene, "frame_current", text="Current")
        if context.scene.use_preview_range == True:
            col.prop(scene, "frame_preview_start", text="Start")
            col.prop(scene, "frame_preview_end", text="End")
        else:
            col.prop(scene, "frame_start", text="Start")
            col.prop(scene, "frame_end", text="End")
        col = self.layout.column(align=True)
        col.prop(context.preferences.edit, "use_mouse_depth_cursor", toggle=True, text="Cursor Surface Project")
        col.prop(context.preferences.edit, "use_visual_keying", toggle=True, text="Visual Keying")
        col.prop(context.preferences.edit, "use_keyframe_insert_needed", toggle=True, text="Only insert needed")
        col.prop(context.preferences.edit, "use_keyframe_insert_available", toggle=True, text="Only insert Available")
        col.prop(context.preferences.edit, "keyframe_new_interpolation_type", text="")
        col.prop(context.preferences.edit, "keyframe_new_handle_type", text="")
        col.prop(context.preferences.inputs.walk_navigation, "view_height")

#Adds Simplify subpanel to Anime Tools        
class DDSSimple(DDSAnime, Panel):
    bl_label = "Simplify"
    bl_parent_id = "DDSTools"
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw_header(self, context):
        self.layout.prop(context.scene.render, "use_simplify", text="")
        
    def draw(self, context):
        rd = context.scene.render
        cscene = context.scene.cycles
        eg = context.engine
        layout = self.layout
        col = layout.column(align=True)
        col.active = rd.use_simplify
        col.label(text="View Port")
        row = col.row(align=True)
        row.prop(rd, "simplify_subdivision", text="")
        row.prop(rd, "simplify_child_particles", text="")
        if hasattr(rd, "simplify_volumes"):
            row = col.row(align=True)
            row.prop(rd, "simplify_volumes", text="Volume Resolution")
                
        if eg == "CYCLES":
            row = col.row(align=True)
            row.label(text="Texture Limit")
            row = col.row(align=True)
            row.prop(cscene, "texture_limit", text="")
            row = col.row(align=True)
            row.prop(cscene, "ao_bounces", text="AO Bounces")
        row = col.row(align=True)
        row.prop(rd, "use_simplify_smoke_highres", text="High-Res Smoke")
        col.label(text="Render")
        row = col.row(align=True)
        row.prop(rd, "simplify_subdivision_render", text="")
        row.prop(rd, "simplify_child_particles_render", text="")
        if eg == "CYCLES":
            row = col.row(align=True)
            row.label(text="Texture Limit")
            row = col.row(align=True)
            row.prop(cscene, "texture_limit_render", text="")
            row = col.row(align=True)
            row.prop(cscene, "ao_bounces_render", text="AO Bounces")
        if eg == "CYCLES":
            box = layout.box()
            col.label(text="Culling")
            col = box.column(align=True)
            col.active = rd.use_simplify
            col.prop(cscene, "use_camera_cull")
            row = col.row()
            row.active = cscene.use_camera_cull
            row.prop(cscene, "camera_cull_margin", text="Cam Margin")
            col.prop(cscene, "use_distance_cull")
            row = col.row()
            row.active = cscene.use_distance_cull
            row.prop(cscene, "distance_cull_margin", text="Dist Margin")
            
        col = layout.column()
        col.active = rd.use_simplify
        col.prop(rd, "simplify_gpencil", text="Grease Pencil")
        box = layout.box()
        if rd.use_simplify and rd.simplify_gpencil:
            box.active = True
        else:
            box.active = False
        col = box.column(align=True)
        col.prop(rd, "simplify_gpencil_onplay", text="Playback Only") 
        col.prop(rd, "simplify_gpencil_view_fill", text="Fill")
        col.prop(rd, "simplify_gpencil_modifier", text="Modifiers") 
        col.prop(rd, "simplify_gpencil_shader_fx", text="ShaderFX") 
        col.prop(rd, "simplify_gpencil_tint", text="Layers Tinting") 
        col.prop(rd, "simplify_gpencil_antialiasing", text="Antialiasing")

classes = (
    DDSTools,
    DDSSimple,
    MyPath,
    MyPath2,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__": 
    register()    