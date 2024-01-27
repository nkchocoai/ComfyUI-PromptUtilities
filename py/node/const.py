from .base import BaseNode

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