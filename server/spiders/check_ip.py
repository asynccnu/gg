import aiohttp
import concurrent.futures

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

async def _check_ip(ip):
    _ip = ip.get('ip')
    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            resp = await session.get('http://www.baidu.com', proxy=_ip, timeout=3)
            await resp.text() # release
            return ip
        except Exception: # 😂
            return None

async def check_ip(ip, ip_use):
    _ip = await _check_ip(ip)
    if _ip:
        ip_use.append(_ip)
