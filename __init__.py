from .py.node import *

NODE_CLASS_MAPPINGS = {
    "PromptUtilitiesFormatString": PromptUtilitiesFormatString,
    "PromptUtilitiesJoinStringList": PromptUtilitiesJoinStringList,
    "PromptUtilitiesLoadPreset": PromptUtilitiesLoadPreset,
    "PromptUtilitiesConstString": PromptUtilitiesConstString,
    "PromptUtilitiesConstStringMultiLine": PromptUtilitiesConstStringMultiLine,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptUtilitiesFormatString": "Format String",
    "PromptUtilitiesJoinStringList": "Join String List",
    "PromptUtilitiesLoadPreset": "Load Preset",
    "PromptUtilitiesConstString": "Const String",
    "PromptUtilitiesConstStringMultiLine": "Const String(multi line)",
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]