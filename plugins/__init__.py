# Zeno Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Anime_Factory_Official
# Developer @Grand_Zeno_Omni_KingBot





from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app





# Zeno Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Anime_Factory_Official
# Developer @Grand_Zeno_Omni_KingBot
