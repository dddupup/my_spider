# coding:utf-8
# HTML下载器
import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko)"
                                " Chrome/58.0.3029.110 Safari/537.36"}
        resp = requests.get(url, headers=header)
        resp.encoding = 'utf-8'
        if resp.status_code != 200:
            return None
        return resp.text
