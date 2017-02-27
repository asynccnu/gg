# gg client example
import random
import asyncio
import aioredis
import aiohttp
from aiohttp import web

# db = redis.StrictRedis(host='localhost', port=6379)
# db.slaveof(host='192.168.99.100', port=7389)
# loop = asyncio.get_event_loop()
async def redis_conn():
    conn = await aioredis.create_connection(('localhost', 6379))
    ips = await conn.execute('smembers', 'ips')
    conn.close()
    await conn.wait_closed()
    return ips

# ips = list(db.smembers('ips')) # blocking

async def handle(request):
    ips = await redis_conn()
    ip = "http://" + eval(random.choice(ips)).get('ip')
    # ip = None
    async with aiohttp.ClientSession() as session:
        async with session.get('http://muxistudio.com', proxy=ip) as resp:
            print(resp.status)
    return web.Response(text="done")


app = web.Application()
app.router.add_get('/', handle)
web.run_app(app)
