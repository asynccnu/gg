import asyncio
from .cn_proxy import cn_proxy_spider
from .kuaidaili import kuaidaili_spider
from .xicidaili import xici_spider
from .mimvp import mimvp_spider
from .check_ip import check_ip

def _start_spiders(ip_all):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(

        # shadowsocks proxy, crawl 100 ip
        cn_proxy_spider(ip_all, 70, {'127.0.0.1': 1080}),
        # kuaidaili_spider(ip_all, 100),
        # mimvp_spider(ip_all, 20)
        # xici_spider(ip_all, 200)
    ))

def _check_ips(ip_all, ip_use):
    loop = asyncio.get_event_loop()
    tasks = []
    for ip in ip_all:
        tasks.append(check_ip(ip, ip_use))
    loop.run_until_complete(asyncio.gather(*tuple(tasks)))
