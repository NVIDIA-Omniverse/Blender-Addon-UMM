# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.

import typing
import traceback

import bpy

from ..core.converter import util


"""
import omni.universalmaterialmap.blender.material

omni.universalmaterialmap.blender.material.apply_data_to_instance(
instance_name='Material',
source_class='OmniPBR.mdl|OmniPBR',
render_context='Blender',
source_data=[
            ('albedo_add', 0.02),
            ('albedo_desaturation', 0.19999999),
            ('ao_texture', ('', 'raw')),
            ('ao_to_diffuse', 1),
            ('bump_factor', 10),
            ('diffuse_color_constant', (0.800000011920929, 0.800000011920929, 0.800000011920929)),
            ('diffuse_texture', ('D:/Blender_GTC_2021/Marbles/assets/standalone/A_bumper/textures/play_bumper/blue/play_bumperw_albedo.png', 'sRGB')),
            ('diffuse_tint', (0.96202534, 0.8118357, 0.8118357)),
            ('enable_emission', 0),
            ('enable_ORM_texture', 1),
            ('metallic_constant', 1),
            ('metallic_texture', ('', 'raw')),
            ('metallic_texture_influence', 1),
            ('normalmap_texture', ('D:/Blender_GTC_2021/Marbles/assets/standalone/A_bumper/textures/play_bumper/blue/play_bumperw_normal.png', 'raw')),
            ('ORM_texture', ('D:/Blender_GTC_2021/Marbles/assets/standalone/A_bumper/textures/play_bumper/blue/play_bumperw_orm.png', 'raw')),
            ('reflection_roughness_constant', 1),
            ('reflection_roughness_texture_influence', 1),
            ('reflectionroughness_texture', ('', 'raw')),
            ('texture_rotate', 45),
            ('texture_scale', (2, 2)),
            ('texture_translate', (0.1, 0.9)),
        ]
)
"""
"""
import omni.universalmaterialmap.blender.material

omni.universalmaterialmap.blender.material.convert_instance_to_data(
instance_name='Material',
render_context='MDL',
)

import omni.universalmaterialmap.blender.material

omni.universalmaterialmap.blender.material.convert_instance_to_data(
instance_name='M_play_bumper_wood',
render_context='MDL',
)
"""


def apply_data_to_instance(instance_name: str,  source_class: str, render_context: str, source_data: typing.List[typing.Tuple[str, typing.Any]]) -> None:
    try:
        for material in bpy.data.materials:
            if not isinstance(material, bpy.types.Material):
                continue
            if material.name == instance_name:
                if util.can_apply_data_to_instance(source_class_name=source_class, render_context=render_context, source_data=source_data, instance=material):
                    util.apply_data_to_instance(source_class_name=source_class, render_context=render_context, source_data=source_data, instance=material)
                else:
                    print(f'Omniverse UMM: Unable to apply data at import for material "{instance_name}". This is not an error - just means that conversion data does not support the material.')
                return
    except Exception as error:
        print('Warning: Universal Material Map: function "apply_data_to_instance": Unexpected error:')
        print('\targument "instance_name" = "{0}"'.format(instance_name))
        print('\targument "source_class" = "{0}"'.format(source_class))
        print('\targument "render_context" = "{0}"'.format(render_context))
        print('\targument "source_data" = "{0}"'.format(source_data))
        print('\terror: {0}'.format(error))
        print('\tcallstack: {0}'.format(traceback.format_exc()))


def convert_instance_to_data(instance_name: str,  render_context: str) -> typing.List[typing.Tuple[str, typing.Any]]:
    try:
        for material in bpy.data.materials:
            if not isinstance(material, bpy.types.Material):
                continue
            if material.name == instance_name:
                if util.can_convert_instance_to_data(instance=material, render_context=render_context):
                    return util.convert_instance_to_data(instance=material, render_context=render_context)
                return []
    except Exception as error:
        print('Warning: Universal Material Map: function "convert_instance_to_data": Unexpected error:')
        print('\targument "instance_name" = "{0}"'.format(instance_name))
        print('\targument "render_context" = "{0}"'.format(render_context))
        print('\terror: {0}'.format(error))
        print('\tcallstack: {0}'.format(traceback.format_exc()))
    return []
