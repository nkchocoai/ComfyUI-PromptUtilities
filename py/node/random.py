from .base import BaseNode

import numpy as np


class PromptUtilitiesSampleTags(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "tags": ("STRING", {"default": "", "multiline": True}),
                "tags_delimiter": (("new line", ","),),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "max_k": ("INT", {"default": 1, "min": 1, "max": 0xFFFFFFFFFFFFFFFF}),
                "min_k": ("INT", {"default": 1, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "sample_tags"

    def sample_tags(self, tags, tags_delimiter, seed, max_k, min_k):
        sampled_tags = self._sample_tags(tags, tags_delimiter, seed, max_k, min_k)
        return (", ".join(sampled_tags),)

    def _sample_tags(self, tags_s, tags_delimiter, seed, max_k, min_k):
        assert max_k >= min_k, "max_k must be greater than or equal to min_k."

        if tags_delimiter == "new line":
            tags = [tag.strip() for tag in tags_s.split("\n")]
        elif tags_delimiter == ",":
            tags = [tag.strip() for tag in tags_s.split(",")]

        random_gen = np.random.default_rng(seed)
        k = random_gen.integers(min_k, max_k + 1)
        random_gen.shuffle(tags)
        return tags[:k]


class PromptUtilitiesSampleTagsWithWeight(PromptUtilitiesSampleTags):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "tags": ("STRING", {"default": "", "multiline": True}),
                "tags_delimiter": (("new line", ","),),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "max_k": ("INT", {"default": 1, "min": 1, "max": 0xFFFFFFFFFFFFFFFF}),
                "min_k": ("INT", {"default": 1, "min": 0, "max": 0xFFFFFFFFFFFFFFFF}),
                "max_w": (
                    "FLOAT",
                    {"default": 1.0, "min": -100, "max": 100, "step": 0.01},
                ),
                "min_w": (
                    "FLOAT",
                    {"default": 0.8, "min": -100, "max": 100, "step": 0.01},
                ),
                "step_w": (
                    "FLOAT",
                    {"default": 0.1, "min": -100, "max": 100, "step": 0.01},
                ),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "sample_tags"

    def sample_tags(
        self, tags, tags_delimiter, seed, max_k, min_k, max_w, min_w, step_w
    ):
        sampled_tags = self._sample_tags(tags, tags_delimiter, seed, max_k, min_k)
        random_gen = np.random.default_rng(seed)
        weights = random_gen.choice(
            np.arange(min_w, max_w, step_w),
            size=len(sampled_tags),
        )
        sampled_tags = [f"({t}:{round(w, 2)})" for t, w in zip(sampled_tags, weights)]
        return (", ".join(sampled_tags),)
