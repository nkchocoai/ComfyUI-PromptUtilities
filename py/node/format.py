from .base import BaseNode


class PromptUtilitiesFormatString(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "prompt": ("STRING", {"default": "[1], [2]", "display": "prompt"}),
            },
            "optional": {
                "arg1": ("STRING", {"forceInput": True}),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format"

    def format(self, prompt, **kwargs):
        result = prompt
        for i in range(1, len(kwargs) + 1):
            result = result.replace(f"[{i}]", kwargs[f"arg{i}"])
        return (result,)


class PromptUtilitiesJoinStringList(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "separator": ("STRING", {"default": ", ", "display": "separator"}),
            },
            "optional": {
                "arg1": ("STRING", {"forceInput": True}),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "join"

    def join(self, separator, **kwargs):
        # join without empty strings.
        result = separator.join([s for s in kwargs.values() if s])
        return (result,)
