# gg client example
import redis
import aiohttp
from aiohttp import web

db = redis.StrictRedis(host='localhost', port=6379)
db.slaveof(host='192.168.99.100', port=7389)

async def handle(request):
    _ip = eval(db.srandmember('ips'))
    ip = 'http://' + _ip.get('ip')
    async with aiohttp.ClientSession() as session:
        async with session.get('http://muxistudio.com', proxy=ip) as resp:
            print(resp.status)
    return web.Response(text="done")


app = web.Application()
app.router.add_get('/', handle)
web.run_app(app)
