from aiohttp import web
import server

from .preset import PresetManager, PresetManagerAdvanced

@server.PromptServer.instance.routes.post("/prompt_utilities/refresh")
async def refresh_preset_manager(request):
    PresetManager.load_presets()
    PresetManagerAdvanced.load_presets()
    return web.Response(status=200)