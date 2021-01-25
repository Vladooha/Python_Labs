import requests
from multiprocessing.dummy import Pool
import sys
import re
import time

HOST_REGEXP = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'

def load_urls():
    print('LOADING URL LIST...')
    with open('links.txt', 'r') as links:
        urls = links.readlines()
        cutted_urls = []
        for url in urls:
            cutted_url = url.replace("\n", "")
            cutted_urls.append(cutted_url)
        return cutted_urls

def parse_url(url):
    match = re.search(HOST_REGEXP, url)
    address = match.group('host')
    print('Parsing [{}]...'.format(address))

    response = requests.get(url)
    html = response.text

    print('[{}]: {}'.format(address, html[:100].replace("\n", "")))

    return html

if __name__ == '__main__':
    PROCESS_COUNT = sys.argv[1] if len(sys.argv) > 1 else 1
    print('WEB PARSER STARTED ({} THREADS)'.format(PROCESS_COUNT))

    urls = load_urls()
    print('Url list:\n-----\n{}\n-----'.format('\n'.join(urls)))
    print('PARSING STARTED')
    start_time = time.time()
    with Pool(int(PROCESS_COUNT)) as pool:
        html_arr = pool.map(parse_url, urls)
    end_time = time.time()
    print('Parsing time: {} s'.format(end_time - start_time))
