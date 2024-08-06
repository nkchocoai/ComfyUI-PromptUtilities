import re

from .base import BaseNode


class PromptUtilitiesPromptWeight(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt1": ("STRING", {"default": "", "multiline": False}),
                "weight1": (
                    "FLOAT",
                    {"default": 1.0, "min": -100, "max": 100, "step": 0.1},
                ),
            },
            "optional": {
                "prompt2": ("STRING", {"default": "", "multiline": False}),
                "weight2": (
                    "FLOAT",
                    {"default": 1.0, "min": -100, "max": 100, "step": 0.1},
                ),
                "prompt3": ("STRING", {"default": "", "multiline": False}),
                "weight3": (
                    "FLOAT",
                    {"default": 1.0, "min": -100, "max": 100, "step": 0.1},
                ),
                "prompt4": ("STRING", {"default": "", "multiline": False}),
                "weight4": (
                    "FLOAT",
                    {"default": 1.0, "min": -100, "max": 100, "step": 0.1},
                ),
                "prompt_weight": (
                    "STRING",
                    {"default": "", "multiline": False},
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "gen_prompt_weight"

    def gen_prompt_weight(self, **kwargs):
        prompts = []
        for i in range(4):
            prompt = kwargs[f"prompt{i+1}"]
            weight = kwargs[f"weight{i+1}"]
            if prompt == "" or weight == 0.0:
                continue
            if weight == 1.0:
                prompts.append(prompt)
            else:
                prompts.append(f"({prompt}:{weight})")

        if kwargs.get("prompt_weight", ""):
            prompts.append(kwargs["prompt_weight"])
        return (", ".join(prompts),)


class PromptUtilitiesRoundPromptWeight(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": False}),
                "n": ("INT", {"default": 3, "min": 0, "max": 100}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)

    FUNCTION = "round_prompt_weight"

    def round_prompt_weight(self, prompt, n):
        def round_match(match):
            number = float(match.group(1))
            rounded = round(number, n)
            return f"{rounded:.10f}".rstrip("0").rstrip(".")

        pattern = r"([-+]?\d*\.\d+)"
        return (re.sub(pattern, round_match, prompt),)
