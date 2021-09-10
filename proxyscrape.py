import aiohttp, asyncio
from fake_useragent import UserAgent

# Scrape & Check Proxies

pinglink = "http://httpbin.org/ip" # HTTP Protocol (No ssl)
proxylink = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http"
ranua = {'User-Agent': UserAgent()['google chrome']}
tm = 1 # Timeout per proxie (Measured in seconds)
logproxies = True # Option to log Good and bad Proxies on Terminal

async def checkproxy(session, proxie):
    try:
        async with session.get(pinglink, proxy=f"http://{proxie.split(':')[0]}:{proxie.split(':')[1]}", timeout=tm) as r:
            if logproxies == True:
                print(f'[Good] | {proxie}')
            return f'ok|{proxie}'
    except:
        if logproxies == True:
            print(f'[Bad] | {proxie}')
        return f'failed|{proxie}'

async def handleproxies(session, proxy_list):
    goodproxies = []
    for proxie in proxy_list:
        task = asyncio.create_task(checkproxy(session, proxie))
        goodproxies.append(task)
    results = await asyncio.gather(*goodproxies)
    return results

async def main(proxy_list):
    async with aiohttp.ClientSession() as session:
        data = await handleproxies(session, proxy_list)
        return data

async def getproxies():
    async with aiohttp.ClientSession(headers=ranua) as session:
        async with session.get(proxylink) as r:
            proxies = await r.text()
            return proxies

def proxielist():
    proxies = asyncio.get_event_loop().run_until_complete(getproxies()).replace("\r", "").split("\n")[:-1]
    workingprox = asyncio.get_event_loop().run_until_complete(main(proxies))
    proxwork = []
    for prox in workingprox:
        if "ok" in prox:
            proxwork.append(prox.split("|")[1])
    return proxwork