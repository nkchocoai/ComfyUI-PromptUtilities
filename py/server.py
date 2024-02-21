import json

from aiohttp import web
import server

from .preset import PresetManager, PresetManagerAdvanced


@server.PromptServer.instance.routes.post("/prompt_utilities/refresh")
async def refresh_preset_manager(request):
    PresetManager.load_presets()
    PresetManagerAdvanced.load_presets()
    return web.Response(status=200)


def on_prompt(json_data):
    prompt = json_data["prompt"]

    for k, v in prompt.items():
        if "class_type" in v and (
            v["class_type"]
            in ["PromptUtilitiesRandomPreset", "PromptUtilitiesRandomPresetAdvanced"]
        ):
            inputs = v["inputs"]
            input_seed = int(inputs["seed"])
            input_filename = inputs["filename"]
            if v["class_type"] == "PromptUtilitiesRandomPreset":
                inputs["choice_preset"] = PresetManager.random_preset(
                    input_filename, input_seed
                )
            elif v["class_type"] == "PromptUtilitiesRandomPresetAdvanced":
                preset = PresetManagerAdvanced.random_preset(input_filename, input_seed)
                inputs["choice_preset"] = json.dumps(preset)

            server.PromptServer.instance.send_sync(
                "prompt-utilities-feedback",
                {
                    "node_id": k,
                    "widget_name": "choice_preset",
                    "type": "STRING",
                    "value": inputs["choice_preset"],
                },
            )

    return json_data


server.PromptServer.instance.add_on_prompt_handler(on_prompt)
