__author__ = 'pattersonday'


import argparse
from bs4 import BeautifulSoup
import requests
import re
import sys
from urlparse import urljoin


def create_parser():
    """Create a cmd line parser object with 1 argument definition"""

    parser = argparse.ArgumentParser(description='Process url')
    parser.add_argument('url', help='url to parse')
    return parser


def url_to_parse(url):
    response = requests.get(url)
    url_content = response.content

    url_list = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|
        (?:%[0-9a-fA-F][0-9a-fA-F]))+', url_content)
    # email_list = re.findall(r'
    # (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', url_content)
    # phone_list = re.findall(r'
    # 1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?',
    # url_content)

    soup = BeautifulSoup(url_content, features='html.parser')

    href = soup.find_all('a')
    href_list = []

    for link in href:
        full_url = urljoin(url, str(link.get('href')))
        if full_url not in href_list:
            href_list.append(full_url)

    src = soup.find_all('img')
    src_list = []

    for img in src:
        full_img = urljoin(url, str(img.get('src')))
        if full_img not in src_list:
            src_list.append(full_img)

    print('Urls {} and img {}'.format('\n'.join(href_list + url_list),
          '\n'.join(src_list)))


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    url = args.url

    url_to_parse(url)


if __name__ == '__main__':
    main()
