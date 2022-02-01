# aiohttpdemo_polls/main.py


import sys
import asyncio

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from aiohttp import web

from settings import config
from routes import setup_routes
from db import pg_context

app = web.Application()
app['config'] = config
setup_routes(app)
app.cleanup_ctx.append(pg_context)
web.run_app(app)