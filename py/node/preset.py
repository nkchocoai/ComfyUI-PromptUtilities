from .base import BaseNode
from ..preset import PresetManager, PresetManagerAdvanced


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
            
    RETURN_TYPES = ("STRING","STRING","STRING","FLOAT","FLOAT","LORA_STACK",)
    RETURN_NAMES = ("positive prompt","negative prompt","lora name","strength model","strength clip","lora stack",)
    FUNCTION = "load_preset"

    def load_preset(self, preset):
        preset = PresetManagerAdvanced.get_preset(preset)
        positive_prompt = preset.get("positive_prompt","")
        negative_prompt = preset.get("negative_prompt","")
        
        lora = preset.get("lora", None)
        lora_name, strength_model, sterngth_clip = self.load_lora(lora)
        
        loras = preset.get("loras", None)
        lora_stack = self.load_loras(loras)
            
        return (positive_prompt, negative_prompt, lora_name, strength_model, sterngth_clip, lora_stack)
    
    def load_lora(self, lora):
        if lora is None:
            return "None", 0, 0
        
        lora_name = lora.get("lora_name", "None")
        if "weight" in lora:
            strength_model = lora.get("weight", 0)
            sterngth_clip = lora.get("weight", 0)
        else:
            strength_model = lora.get("strength_model", 0)
            sterngth_clip = lora.get("strength_clip", 0)

        return lora_name, strength_model, sterngth_clip

    
    def load_loras(self, loras):
        lora_stack = []
        if loras is None:
            return lora_stack
        
        for lora in loras:
            lora_name, strength_model, sterngth_clip = self.load_lora(lora)
            loras.append((lora_name, strength_model, sterngth_clip))

        return lora_stack