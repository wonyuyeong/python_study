# urllib : url을 읽고 분석할 때 사용하는 모듈

import urllib.request,webbrowser

def getwikidocs(page):
    resource = 'https://wikidocs.net/{}' .format(page)
    with urllib.request.urlopen(resource) as s :
        with open("day07/wikidocs_%s.html" %page, "wb") as f :
            f.write(s.read())

getwikidocs(12)

# open_new 새창에 브러우저 열기
# open: 기존 창에 열기
webbrowser.open_new("http://python.org")