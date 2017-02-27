import aiohttp
import aiosocks
from bs4 import BeautifulSoup
from aiosocks.connector import SocksConnector

async def cn_proxy_spider(ip_all, ip_num, proxy=None):
    cn_proxy_url = "http://cn-proxy.com/"
    proxy_addr, proxy_port = list(proxy.items())[0]
    conn = SocksConnector(proxy=aiosocks.Socks5Addr(proxy_addr, proxy_port),
                          proxy_auth=None, remote_resolve=True)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(cn_proxy_url) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, 'lxml')
            tbodys = soup.find_all('tbody')
            for tbody in tbodys:
                for _ in tbody.find_all('tr'):
                    td = _.find_all('td')
                    ip_all.append({
                        'ip'  : 'http://' + td[0].string+':'+td[1].string,
                        'addr': td[2].string.split(" ")[0],
                        'time': td[-1].string
                    })
