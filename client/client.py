# gg client example
import random
import asyncio
import aioredis
import aiohttp
from aiohttp import web

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:2.0b9pre) Gecko/20110105 Firefox/4.0b9pre'}

async def redis_conn():
    redis = await aioredis.create_redis(('localhost', 6379))
    redis.slaveof(host='192.168.99.100', port=7389)
    ips = await redis.smembers('ips')
    redis.close()
    await redis.wait_closed()
    return ips

async def handle(request):
    ips = await redis_conn()
    while True:
        ip = eval(random.choice(ips)).get('ip')
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get('http://muxistudio.com', proxy=ip, timeout=3) as resp:
                    print(ip)
                    print(resp.status)
                    break
            except Exception:
                pass
    return web.Response(text="done")

app = web.Application()
app.router.add_get('/', handle)
web.run_app(app)
