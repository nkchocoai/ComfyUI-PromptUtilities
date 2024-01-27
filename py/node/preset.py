from .base import BaseNode
from ..preset import PresetManager


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
        prompt = PresetManager.get_prompt(preset)
        return (prompt,)