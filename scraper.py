__author__ = 'pattersonday'


import argparse
import requests
import re


def create_parser():
    """Create a cmd line parser object with 1 argument definition"""

    parser = argparse.ArgumentParser(description='Process url')
    parser.add_argument('url', help='url to parse')
    return parser


def url_to_parse(url):
    response = requests.get(url)
    response.content


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    url = args.url
      

if __name__ == '__main__':
    main()
