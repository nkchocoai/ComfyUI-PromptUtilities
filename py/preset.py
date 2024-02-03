import csv
import json
import os

import numpy as np

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
        return presets[key]

    @classmethod
    def get_presets_by_filename(cls, filename):
        presets = cls.get_presets()
        presets_by_name = [v for k,v in presets.items() if k.split(' : ')[0] == filename]
        return presets_by_name

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
    
    @classmethod
    def random_preset(cls, filename, seed):
        random_gen = np.random.default_rng(seed)
        presets = cls.get_presets_by_filename(filename[:-4])
        preset = random_gen.choice(presets)
        return preset



class PresetManagerAdvanced(PresetManagerBase):
    presets_dir = "advanced_presets"
    file_extensions = ['.json']

    @classmethod
    def load_file(cls, f, preset_filename):
        data = json.load(f)
        for k,v in data.items():
            cls._presets[f"{preset_filename[:-5]} : {k}"] = v

    @classmethod
    def parse_preset(cls, preset):
        positive_prompt = preset.get("positive_prompt","")
        negative_prompt = preset.get("negative_prompt","")
        
        lora = preset.get("lora", None)
        lora_name, strength_model, sterngth_clip = cls.load_lora(lora)
        
        loras = preset.get("loras", None)
        if loras is None and lora is not None:
            lora_stack = [(lora_name, strength_model, sterngth_clip)]
        else:
            lora_stack = cls.load_loras(loras)

        return positive_prompt, negative_prompt, lora_name, strength_model, sterngth_clip, lora_stack
    
    @classmethod
    def load_lora(cls, lora):
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

    @classmethod
    def load_loras(cls, loras):
        lora_stack = []
        if loras is None:
            return lora_stack
        
        for lora in loras:
            lora_name, strength_model, sterngth_clip = cls.load_lora(lora)
            lora_stack.append((lora_name, strength_model, sterngth_clip))

        return lora_stack

    @classmethod
    def random_preset(cls, filename, seed):
        random_gen = np.random.default_rng(seed)
        presets = cls.get_presets_by_filename(filename[:-5])
        preset = random_gen.choice(presets)
        return preset