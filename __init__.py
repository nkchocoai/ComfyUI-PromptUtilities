import configparser
import os

from .py.node.const import *
from .py.node.format import *
from .py.node.preset import *
from .py.node.weight import *
from .py.server import *
from .py.preset import PresetManager

NODE_CLASS_MAPPINGS = {
    "PromptUtilitiesFormatString": PromptUtilitiesFormatString,
    "PromptUtilitiesJoinStringList": PromptUtilitiesJoinStringList,
    "PromptUtilitiesLoadPreset": PromptUtilitiesLoadPreset,
    "PromptUtilitiesLoadPresetAdvanced": PromptUtilitiesLoadPresetAdvanced,
    "PromptUtilitiesRandomPreset": PromptUtilitiesRandomPreset,
    "PromptUtilitiesRandomPresetAdvanced": PromptUtilitiesRandomPresetAdvanced,
    "PromptUtilitiesConstString": PromptUtilitiesConstString,
    "PromptUtilitiesConstStringMultiLine": PromptUtilitiesConstStringMultiLine,
    "PromptUtilitiesPromptWeight": PromptUtilitiesPromptWeight,
    "PromptUtilitiesRoundPromptWeight": PromptUtilitiesRoundPromptWeight,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptUtilitiesFormatString": "Format String",
    "PromptUtilitiesJoinStringList": "Join String List",
    "PromptUtilitiesLoadPreset": "Load Preset",
    "PromptUtilitiesLoadPresetAdvanced": "Load Preset (Advanced)",
    "PromptUtilitiesRandomPreset": "Random Preset",
    "PromptUtilitiesRandomPresetAdvanced": "Random Preset (Advanced)",
    "PromptUtilitiesConstString": "Const String",
    "PromptUtilitiesConstStringMultiLine": "Const String (multi line)",
    "PromptUtilitiesPromptWeight": "Prompt Weight",
    "PromptUtilitiesRoundPromptWeight": "Round Prompt Weight",
}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]


# output csv presets as wildcards.
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
if config.has_section("default"):
    default_config = config["default"]
    output_dir = default_config.get("output_csv_presets_as_wildcards")
    if output_dir:
        output_dir = os.path.abspath(output_dir)
        print("output presets as wildcard.", output_dir)
        PresetManager.output_as_wildcard(output_dir)
