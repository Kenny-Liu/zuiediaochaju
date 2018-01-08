#!/usr/bin/env python
# coding=utf-8
# 用于从猎文网上查找罪恶调查局各个章节的链接地址


from urllib import request
import re

based_url = r"https://www.liewen.cc/b/0/449"


def get_chapter_html(based_url):
    # get the web content
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'referer': r'https://www.liewen.cc/b/0/449/',
        'connection': 'keep-alive',
    }
    req = request.Request(based_url, headers=headers)
    page = request.urlopen(req).read()
    page = page.decode("gbk")
    return page

def get_chapter_link(page):
    # analyse the web page to get the chapter link
    links = []
    result = re.findall(r"<dd>.*</a>", page)
    result = result[0].split("</dd>")
    for row_link in result:
        link = re.findall(r'/.*html', row_link)
        link = based_url + str(link[0])
        name = re.findall(r'<a .+>(.*?)</a>', row_link)
        links.append((link, name[0]))
    return links

if __name__=="__main__":
    page = get_chapter_html(based_url)
    links = get_chapter_link(page)
    page = get_chapter_html(r"https://www.liewen.cc/b/0/449/b/0/449/409570.html")
    print(page)
#    for link,name in links:
 #       print(link,name)