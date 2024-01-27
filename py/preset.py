import csv
import json
import os

import folder_paths

class PresetManagerBase:
    _presets = None

    custom_nodes_dir = folder_paths.get_folder_paths("custom_nodes")[0]

    file_extensions = []

    @classmethod
    def get_presets_dir(cls):
        return os.path.join(cls.custom_nodes_dir, "ComfyUI-PromptUtilities", cls.presets_dir)

    @classmethod
    def get_presets(cls):
        if cls._presets is None:
            cls.load_presets()
        return cls._presets

    @classmethod
    def get_preset(cls, key):
        presets = cls.get_presets()
        print(key, presets, presets[key])
        return presets[key]

    @classmethod
    def get_preset_filename_list(cls):
        files, _ = folder_paths.recursive_search(cls.get_presets_dir(), excluded_dir_names=[".git"])

        return folder_paths.filter_files_extensions(files, cls.file_extensions)

    @classmethod
    def load_presets(cls):
        cls._presets = dict()
        preset_filename_list = cls.get_preset_filename_list()
        for preset_filename in preset_filename_list:
            with open(os.path.join(cls.get_presets_dir(), preset_filename),"r", encoding='utf-8') as f:
                cls.load_file(f, preset_filename)


class PresetManager(PresetManagerBase):
    presets_dir = "presets"
    file_extensions = ['.csv']

    @classmethod
    def load_file(cls, f, preset_filename):
        reader = csv.DictReader(f)
        for row in reader:
            cls._presets[f"{preset_filename[:-4]} : {row['name']}"] = row['prompt']


class PresetManagerAdvanced(PresetManagerBase):
    presets_dir = "advanced_presets"
    file_extensions = ['.json']

    @classmethod
    def load_file(cls, f, preset_filename):
        data = json.load(f)
        for k,v in data.items():
            cls._presets[f"{preset_filename[:-5]} : {k}"] = v
