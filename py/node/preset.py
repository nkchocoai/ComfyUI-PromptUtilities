import json

import numpy as np

from .base import BaseNode
from ..preset import PresetManager, PresetManagerAdvanced

import folder_paths

class PromptUtilitiesLoadPreset(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "preset": (list(PresetManager.get_presets().keys()), ),
            }
        }
            
    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_preset"

    def load_preset(self, preset):
        prompt = PresetManager.get_preset(preset)
        return (prompt,)


class PromptUtilitiesLoadPresetAdvanced(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "preset": (list(PresetManagerAdvanced.get_presets().keys()), ),
            }
        }
            
    RETURN_TYPES = ("STRING","STRING",folder_paths.get_filename_list("loras"),"FLOAT","FLOAT","LORA_STACK",)
    RETURN_NAMES = ("positive prompt","negative prompt","lora name","strength model","strength clip","lora stack",)
    FUNCTION = "load_preset"

    def load_preset(self, preset):
        preset_ = PresetManagerAdvanced.get_preset(preset)
        positive_prompt, negative_prompt, lora_name, strength_model, sterngth_clip, lora_stack = \
            PresetManagerAdvanced.parse_preset(preset_)
            
        return (positive_prompt, negative_prompt, lora_name, strength_model, sterngth_clip, lora_stack)


class PromptUtilitiesRandomPreset(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "filename": (list(PresetManager.get_preset_filename_list()), ),
                "choice_preset": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }
            
    RETURN_TYPES = ("STRING",)
    FUNCTION = "random_preset"

    def random_preset(self, **kwargs):
        choice_preset = kwargs['choice_preset']
        return (choice_preset,)


class PromptUtilitiesRandomPresetAdvanced(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "filename": (list(PresetManagerAdvanced.get_preset_filename_list()), ),
                "choice_preset": ("STRING", {"multiline": True, "dynamicPrompts": False}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            }
        }
            
    RETURN_TYPES = ("STRING","STRING",folder_paths.get_filename_list("loras"),"FLOAT","FLOAT","LORA_STACK",)
    RETURN_NAMES = ("positive prompt","negative prompt","lora name","strength model","strength clip","lora stack",)
    FUNCTION = "random_preset"

    def random_preset(self, **kwargs):
        choice_preset = kwargs['choice_preset']
        positive_prompt, negative_prompt, lora_name, strength_model, sterngth_clip, lora_stack = \
            PresetManagerAdvanced.parse_preset(json.loads(choice_preset))
        return (positive_prompt, negative_prompt, lora_name, strength_model, sterngth_clip, lora_stack)