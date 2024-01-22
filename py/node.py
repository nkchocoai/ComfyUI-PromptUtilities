import folder_paths

from .preset import PresetManager

class BaseNode:
    CATEGORY = "PromptUtilities"


class PromptUtilitiesConstStringBase(BaseNode):
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_string"

    def get_string(self, string):
        return (string,)


class PromptUtilitiesConstString(PromptUtilitiesConstStringBase):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"default": "", "multiline": False})
            }
        }


class PromptUtilitiesConstStringMultiLine(PromptUtilitiesConstStringBase):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"default": "", "multiline": True})
            }
        }


class PromptUtilitiesFormatString(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "prompt": ("STRING", {"default": "[1], [2]", "display": "prompt"}),
            },
            "optional": {
                "arg1": ("STRING",{"forceInput": True}),
            },
        }
        # for i in range(1, MAX_NUM_ARGS + 1):
        #     arg_name = f"arg{i}"
        #     input_types["optional"][arg_name] = ("STRING", {"default": "", "display": arg_name})

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format"

    def format(self, prompt, **kwargs):
        print(kwargs)
        result = prompt
        for i in range(1, len(kwargs) + 1):
            result = result.replace(f'[{i}]',kwargs[f"arg{i}"]) 
        return (result,)


class PromptUtilitiesJoinStringList(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "separator": ("STRING", {"default": ", ", "display": "separator"}),
            },
            "optional": {
                "arg1": ("STRING",{"forceInput": True}),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "join"

    def join(self, separator, **kwargs):
        PresetManager.load_presets()
        print(kwargs)
        print(kwargs.values())
        result = separator.join(kwargs.values())
        return (result,)


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