from .py.node import *

NODE_CLASS_MAPPINGS = {
    "PromptUtilitiesFormatString": PromptUtilitiesFormatString,
    "PromptUtilitiesJoinStringList": PromptUtilitiesJoinStringList,
    "PromptUtilitiesLoadPreset": PromptUtilitiesLoadPreset,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptUtilitiesFormatString": "Format String",
    "PromptUtilitiesJoinStringList": "Join String List",
    "PromptUtilitiesLoadPreset": "Load Preset",
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]