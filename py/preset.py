import csv
import os

import folder_paths

class PresetManager:
    _presets = None

    custom_nodes_dir = folder_paths.get_folder_paths("custom_nodes")[0]
    presets_dir = os.path.join(custom_nodes_dir, "ComfyUI-PromptUtilities", "presets")

    @classmethod
    def get_presets(cls):
        if cls._presets is None:
            cls.load_presets()
        return cls._presets

    @classmethod
    def get_prompt(cls, key):
        presets = cls.get_presets()
        print(key, presets, presets[key])
        return presets[key]

    @classmethod
    def load_presets(cls):
        cls._presets = dict()
        preset_filename_list = cls.get_preset_filename_list()
        for preset_filename in preset_filename_list:
            with open(os.path.join(cls.presets_dir, preset_filename),"r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cls._presets[f"{preset_filename[:-4]} : {row['name']}"] = row['prompt']

    @classmethod
    def get_preset_filename_list(cls):
        files, _ = folder_paths.recursive_search(cls.presets_dir, excluded_dir_names=[".git"])

        return folder_paths.filter_files_extensions(files, ['.csv'])
