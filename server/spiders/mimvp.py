import aiohttp
from bs4 import BeautifulSoup

async def mimvp_spider(ip_all, ip_num, proxy=None):
    mimvp_url = "http://proxy.mimvp.com/free.php?proxy=in_hp"
    async with aiohttp.ClientSession() as session:
        async with session.get(mimvp_url) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, 'lxml')
            tbody = soup.find('tbody')
            ip_td = []
            for index, td in enumerate(tbody.find_all('td')):
                # 端口居然是奇怪的加密图片....
                print(td)

            print('\n')
