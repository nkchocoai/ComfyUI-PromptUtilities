from .base import BaseNode

import re
from comfy.sd1_clip import token_weights


class PromptUtilitiesReplaceOrInsertTag(BaseNode):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": (
                    "STRING",
                    {"multiline": True, "default": "", "forceInput": True},
                ),
                "pattern": ("STRING", {"default": "", "multiline": False}),
                "value": ("STRING", {"default": "", "multiline": False}),
                "mode": (["replace", "insert"],),
                "inherit_weight": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "replace_tag"

    def replace_tag(self, text, pattern, value, mode, inherit_weight):
        text = text.replace("\(", "{[{[")
        text = text.replace("\)", "}]}]")
        weights = token_weights(text, 1.0)
        tags = []
        for t, weight in weights:
            for tag in t.split(","):
                tag = tag.strip()
                if tag:
                    tags.append((tag, weight))
        tags2 = []
        for i, v in enumerate(tags):
            if re.match(pattern, v[0]):
                w = 1.0
                if inherit_weight:
                    w = v[1]
                if mode == "insert":
                    tags2.append(v)
                tags2.append((value, w))
            else:
                tags2.append(v)
        result = []
        for tag, weight in tags2:
            if weight == 1.0:
                result.append(tag)
            else:
                result.append(f"({tag}:{weight})")
        s = ", ".join(result)
        s = s.replace("{[{[", "\(")
        s = s.replace("}]}]", "\)")
        return (s,)
