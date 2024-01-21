from .nodes.node import *

NODE_CLASS_MAPPINGS = {
    "PromptUtilitiesFormatString": PromptUtilitiesFormatString,
    "PromptUtilitiesJoinStringList": PromptUtilitiesJoinStringList,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptUtilitiesFormatString": "Format String",
    "PromptUtilitiesJoinStringList": "Join String List",
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]