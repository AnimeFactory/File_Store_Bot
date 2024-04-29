# Zeno Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Anime_Factory_Official
# Developer @Grand_Zeno_Omni_KingBot




from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Anime_Factory_Official")




# Zeno Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Anime_Factory_Official
# Developer @Grand_Zeno_Omni_KingBot
