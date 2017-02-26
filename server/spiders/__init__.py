import asyncio
from .cn_proxy import cn_proxy_spider
# from ..tasks import ip_all

def _start_spiders(ip_all):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(

        # shadowsocks proxy, crawl 100 ip
        cn_proxy_spider(ip_all, 100, {'127.0.0.1': 1080}),

    ))
