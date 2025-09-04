import requests
from lxml import html
import random

userAgents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.141 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Mozilla/5.0 (Windows NT 10.0; ARM64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
]

def makeReq(url):

    cookies = {
        'xla': 's4t',
        '_gid': 'GA1.2.1750497856.1756817011',
        '_ga_QFVL8KLXT6': 'GS2.1.s1756817011$o1$g1$t1756817016$j55$l0$h1840389665',
        '_ga': 'GA1.1.672934238.1756817011',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://hdhub4u.menu/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{random.choice(userAgents)}',
        # 'cookie': 'xla=s4t; _gid=GA1.2.1750497856.1756817011; _ga_QFVL8KLXT6=GS2.1.s1756817011$o1$g1$t1756817016$j55$l0$h1840389665; _ga=GA1.1.672934238.1756817011',
    }

    response = requests.get(
        url,
        # cookies=cookies,
        headers=headers,
    )

    return response

def processResponse(response):
    try:
        tree = html.fromstring(response.text)
        downloadLink = tree.xpath('//a[contains(@href,"https://hubdrive.space/file")]/@href')
        downloadName = tree.xpath('//a[contains(@href,"https://hubdrive.space/file")]//text()')

        downloads = list(zip([n.strip() for n in downloadName], downloadLink))
        data = []
        for dwn in downloads:
            dwnType = {
                'typeName':dwn[0],
                'link':dwn[1]
            }
            data.append(dwnType)
        return data
    except Exception as E:
        print(f"[ERROR]: {E}")

def main(url):
    # url = "https://hdhub4u.menu/avatar-2009-brrip-in-hindi-english-full-movie/"
    response = makeReq(url)
    if response:
        results = processResponse(response)
        if results:
            # print(results)
            return results
        else:
            # print(f'[NOT]: {url}')
            return None
    else:
        # print(f'[ERROR]: {response.status_code}')
        return None

# if __name__ == '__main__':
#     main()