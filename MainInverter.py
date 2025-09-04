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

def makeReq1(url):
    cookies = {
        '_ga': 'GA1.1.946365115.1756829554',
        '_ga_8QTNRD0R4M': 'GS2.1.s1756829553$o1$g0$t1756829553$j60$l0$h0',
        'test_variant': '0.2306068649457903',
        'dom3ic8zudi28v8lr6fgphwffqoz0j6c': 'e9c382f4-f7d5-4bdf-9b37-856ee1013304%3A3%3A1',
        'pp_main_c41c0c721055e3861572ac22acdad541': '1',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{random.choice(userAgents)}',
        # 'cookie': '_ga=GA1.1.946365115.1756829554; _ga_8QTNRD0R4M=GS2.1.s1756829553$o1$g0$t1756829553$j60$l0$h0; test_variant=0.2306068649457903; dom3ic8zudi28v8lr6fgphwffqoz0j6c=e9c382f4-f7d5-4bdf-9b37-856ee1013304%3A3%3A1; pp_main_c41c0c721055e3861572ac22acdad541=1',
    }

    try:
        response = requests.get(
            url,
            # cookies=cookies,
            headers=headers
        )

        tree = html.fromstring(response.text)
        downloadLink = tree.xpath('//a[@class="btn btn-primary btn-user btn-success1 m-1"]/@href')
        if downloadLink:
            return downloadLink[0]
        else:
            print(f"[{response.status_code}]: {response.text}")
            return None
    except Exception as E:
        print(f"[ERROR]: {E}")


def makeReq2(url):
    cookies = {
        '_ga': 'GA1.1.367741597.1756722180',
        '_ga_VPX61DM9S8': 'GS2.1.s1756993299$o7$g1$t1756993384$j60$l0$h0',
    }
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{random.choice(userAgents)}',
        # 'cookie': '_ga=GA1.1.367741597.1756722180; _ga_VPX61DM9S8=GS2.1.s1756993299$o7$g1$t1756993384$j60$l0$h0',
    }

    try:
       response = requests.get(
            url,
            cookies=cookies,
            headers=headers
        )

       tree = html.fromstring(response.text)
       downloadLink = tree.xpath('//a[@id="download"]/@href')
       if downloadLink:
           return downloadLink[0]
       else:
           print(f"[{response.status_code}]: {response.text}")
           return None
    except Exception as E:
        print(f"[ERROR]: {E}")


def makeReq3(url):
    cookies = {
        'clever-counter-94679': '0-1',
        'xyt': '2',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'priority': 'u=0, i',
        # 'referer': 'https://stockbhoomi.com/5-profitable-business-ideas-for-2025/',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{random.choice(userAgents)}',
        # 'cookie': 'clever-counter-94679=0-1; xyt=2',
    }

    try:
        response = requests.get(
            url,
            # cookies=cookies,
            headers=headers,
        )

        tree = html.fromstring(response.text)
        downloadLink = tree.xpath('//a[@id="s3"]/@href') or tree.xpath('//a[@id="fsl"]/@href')
        if downloadLink:
            return downloadLink[0]
        else:
            downloadLink = tree.xpath('//a[@class="btn btn-danger btn-lg h6"]/@href')
            if downloadLink:
                if len(downloadLink) > 1:
                    return downloadLink[1]
                else:
                    return downloadLink[0]
            else:
                print(f"[{response.status_code}]: {response.text}")
                return None
    except Exception as E:
        print(f"[ERROR]: {E}")


def mainReq(url):
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

    try:
        response = requests.get(
            url,
            # cookies=cookies,
            headers=headers,
        )

        tree = html.fromstring(response.text)
        downloadLink = tree.xpath('//a[contains(@href,"https://hubdrive.space/file")]/@href')
        downloadName = tree.xpath('//a[contains(@href,"https://hubdrive.space/file")]//text()')

        downloads = list(zip([n.strip() for n in downloadName], downloadLink))

        data = []
        if downloads:
            for dwn in downloads:
                res1 = makeReq1(dwn[1])
                if res1:
                    res2 = makeReq2(res1)
                    if res2:
                        res3 = makeReq3(res2)
                        if res3:
                            dwnType = {
                                'typeName': dwn[0],
                                'link': res3,
                                'status': True
                            }
                            data.append(dwnType)
                        else:
                            print(f"[NOT/3]: {res3}")
                    else:
                        print(f"[LINK]: {res1}")
                        print(f"[NOT/2]: {res2}")
                else:
                    print(f"[NOT/1]: {url}")
            return data
        else:
            downloadLink = tree.xpath('//h3/a[contains(@href,"https://taazabull24.com")]/span/em[not(contains(text(),"Watch"))]/parent::span/parent::a/@href')
            downloadName = tree.xpath('//h3/a[contains(@href,"https://taazabull24.com")]/span/em[not(contains(text(),"Watch"))]/parent::span/parent::a//text()')

            downloads = list(zip([n.strip() for n in downloadName if n != ']'], downloadLink))

            for dwn in downloads:
                dwnType = {
                    'typeName': dwn[0],
                    'link': dwn[1],
                    'status': False
                }
                data.append(dwnType)
            return data
    except Exception as E:
        print(f"[ERROR]: {E}")

def main(url):
    # url = "https://hdhub4u.menu/gangnam-blues-2015-uncut-hindi-bluray-full-movie/"
    results = mainReq(url)
    if results:
        # print(results)
        return results
    else:
        # print(f'[NOT]: {url}')
        return None

# if __name__ == '__main__':
#     main()
