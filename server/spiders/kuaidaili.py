import aiohttp
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    
async def kuaidaili_spider(ip_all, ip_num, proxy=None):
    kuaidaili_url = "http://www.kuaidaili.com/free/inha/1/"
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(kuaidaili_url) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, 'lxml')
            tbody = soup.find('tbody')
            print(soup)
