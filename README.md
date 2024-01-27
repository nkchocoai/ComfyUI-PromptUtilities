# ComfyUI-PromptUtilities
![PromptUtilities Preview](preview.png "PromptUtilities Preview")  
日本語版READMEは[こちら](README.jp.md)。

- Custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
- Add useful nodes related to prompt.

## Installation
```
cd <ComfyUI directory>/custom_nodes
git clone https://github.com/nkchocoai/ComfyUI-PromptUtilities.git
```

## Nodes
### Join String List (Experimental)
- Outputs string which are the input `argN` strings concatenated with `separator`.
- There may be some bugs as we have not been able to check the operation very well.

![Example Join String List](img/ex_join.png "Example Join String List")  

### Format String (Experimental)
- Output string containing the input `argN` embedded in a `prompt`.
- In the `prompt`, `[N]` is replaced by the value of `argN`.
- There may be some bugs as we have not been able to check the operation very well.

![Example Format String](img/ex_format.png "Example Format String")  

### Load Preset
- Outputs the prompt for the selected preset.
- The presets are listed in a CSV file located in the [presets](presets) directory.

![Example Load Preset](img/ex_preset.png "Example Load Preset")

### Load Preset (Advanced)
- Outputs the following values for the selected preset.
  - Positive prompt
  - Negative prompt
  - LoRA and its intensity
  - LoRA Stack (for [Efficiency Nodes](https://github.com/jags111/efficiency-nodes-comfyui))
- The presets are listed in a JSON file located in the [advanced_presets](advanced_presets) directory.

![Example Load Preset Advanced 01](img/ex_preset_adv_01.png "Example Load Preset Advanced 01")
![Example Load Preset Advanced 02](img/ex_preset_adv_02.png "Example Load Preset Advanced 02")

### Const String
- Outputs the input string.

### Const String(multi line)
- Outputs the input string.
- You can input the string in multiple lines.
