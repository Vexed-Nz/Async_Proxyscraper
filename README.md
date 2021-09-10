# Async_Proxyscraper
- Scrape and Check for Fast Proxies with

-- `ProxyScrape API || docs.proxyscrape.com`

### Installation:
> pip install aiohttp fake_useragent

> git clone `https://github.com/Vexed-Nz/Async_Proxyscraper.git`

### Usage:
```py
from proxyscrape import proxielist

print(proxielist())

# Response:
# [Proxy:port...]

# Config in Py File:
'''
pinglink : HTTP Protocol (No ssl)
proxylink : Query Parameter Modifications
ranua : Useragent
tm : Timeout per proxie (sec)
logproxies : Log Proxie Status onto Terminal
'''
```
<br/>
* Be free to submit issues, make pull requests, or suggest features. 
