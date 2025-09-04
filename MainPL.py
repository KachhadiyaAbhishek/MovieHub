import requests
from lxml import html
from pymongo import MongoClient
from datetime import datetime
import random
import concurrent.futures

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

def fetchDate():
    return datetime.now().strftime("%Y_%m_%d")

client = MongoClient("mongodb://localhost:27017/")
db = client["hdhub4u"]
collection = db[f"movieList_{fetchDate()}"]

def makeReq(page):

    cookies = {
        'hidecta': 'no',
        'xla': 's4t',
        '_gid': 'GA1.2.1692397781.1756717430',
        'hidecta': 'no',
        '_gat_gtag_UA_89947843_1': '1',
        '_ga_QFVL8KLXT6': 'GS2.1.s1756717430$o1$g1$t1756718383$j22$l0$h1704189489',
        '_ga': 'GA1.1.1835875240.1756717430',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': f'{random.choice(userAgents)}',
        # 'cookie': 'hidecta=no; xla=s4t; _gid=GA1.2.1692397781.1756717430; hidecta=no; _gat_gtag_UA_89947843_1=1; _ga_QFVL8KLXT6=GS2.1.s1756717430$o1$g1$t1756718383$j22$l0$h1704189489; _ga=GA1.1.1835875240.1756717430',
    }

    response = requests.get(
        f'https://hdhub4u.menu/page/{page}/',
        # cookies=cookies,
        headers=headers
    )

    return response

def processResponse(response):
    try:
        tree = html.fromstring(response.text)

        movieLink = tree.xpath('//ul[@class="recent-movies"]/li/figcaption/a/@href')
        movieName = tree.xpath('//ul[@class="recent-movies"]/li/figcaption/a/p/text()')
        movieImg = tree.xpath('//ul[@class="recent-movies"]/li/figure/img/@src')
        movies = list(zip(movieLink, [m.strip() for m in movieName], movieImg))
        movieData = []
        for movie in movies:
            data = {
                'movieLink': movie[0],
                'movieName': movie[1],
                'movieImage': movie[2]
            }
            movieData.append(data)
        return movieData
    except Exception as e:
        print(f"[ERROR]: {e}")

def pagination(start, end):
    for page in range(start, end + 1):
        response = makeReq(page)
        if response:
            results = processResponse(response)
            if results:
                collection.insert_many(results)
                print(f'[{page}]: {len(results)} movies inserted.')
            else:
                print(f'[NOT]: page: {page} movie not found.')
        else:
            print(f'[ERROR]: {response.status_code}')

def main():
    total_pages = 892
    num_threads = 5
    chunk_size = total_pages // num_threads
    threads = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            start = i * chunk_size + 1
            end = (i + 1) * chunk_size if i < num_threads - 1 else total_pages
            threads.append(executor.submit(pagination, start, end))

        concurrent.futures.wait(threads)

    print("[DONE]: Scraping completed.")

# def main():
#     page = 646
#     while True:
#         response = makeReq(page)
#         if response:
#             results = processResponse(response)
#             if results:
#                 collection.insert_many(results)
#                 print(f'[{page}]: {len(results)} movies inserted.')
#                 page += 1
#             else:
#                 print(f'[NOT]: page: {page} movie not found.')
#                 break
#         else:
#             print(f'[ERROR]: {response.status_code}')
#             break

if __name__ == '__main__':
    main()