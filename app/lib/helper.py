# -*- coding: utf-8 -*-
import platform
import requests


class HttpHelper(object):

    @staticmethod
    def get(q=None, isbn=None, return_json=True, proxies=True):
        if 'mac' in platform.platform():
            proxies = False
        if proxies:
            proxies = {"http": "http://10.158.100.9:8080", "https": "https://10.158.100.9:8080"}
        else:
            proxies = {}
        data = {
            'isbn': q or isbn,
            'key': '6Ffb9ZNmRVvi7YowQ2eRARLfB'
        }
        response = requests.get('https://binstd.apistd.com/isbn/query', params=data, proxies=proxies)
        if response.status_code != 200:
            return {} if return_json else ''
        return response.json() if return_json else response.text

        # with open(r'C:\D\myworkspace\mygitpro\new_fisher\{}.txt'.format(isbn), 'w', encoding='utf8') as f:
        #     f.write(str(resp.json()))
        # return json.loads(outcome)

        # return content


if __name__ == '__main__':
    url = 'https://book.feelyou.top/isbn/9787201094014'  # 'http://t.yushu.im/v2/web/isbn/9787501524044'
    isbn_list = [
        # '9787108012586',
        # '9787546206134',
        # '9787108012555',
        # '9787108012548',
        # '9787108012692'
        '9787546206134'
    ]
    for isbn in isbn_list:
        outcome = HttpHelper.get(isbn=isbn, proxies=True)
    # html = requests.get(url)
    # html1 = html.json()
    print(outcome)
