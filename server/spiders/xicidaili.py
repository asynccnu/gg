import aiohttp
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

async def xici_page_spider(ip_all, page_num):
    xici_url = "http://www.xicidaili.com/nn/%s" % page_num
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(xici_url) as resp:
            content = await resp.text()
            soup = BeautifulSoup(content, 'lxml')
            print(soup)
            tr = soup.find_all('tr')
            for _ in tr[1:]:
                tds = _.find_all('td')
                ip = 'http://' + tds[1].string + ':' + tds[2].string
                print("ip", ip)
                if (tds[3].a): addr = tds[3].a.string 
                else: addr = None
                time = tds[-1].string
                ip_all.append({
                    'ip': ip,
                    'addr': addr,
                    'time': time
                })


async def xici_spider(ip_all, ip_num, proxy=None):
    page = int(ip_num / 100)

    for page_num in range(1, page+1):
        await xici_page_spider(ip_all, page_num)
