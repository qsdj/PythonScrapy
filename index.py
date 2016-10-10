import urllib2
import os
import requests
import sys
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        html = urllib2.urlopen(url).read()
        return html
    except urllib2.URLError,e:
        return ""

def getTargetImg(html):
    soup = BeautifulSoup(html)
    position = '/Users/likeli/Desktop/BeautifulImage/'
    if not os.path.isdir(position):
        os.makedirs(position)
    targetdiv = soup.find('div', class_='content-pic')
    nextUrl = targetdiv.find('a').get('href')
    targetImg = targetdiv.find('img')
    pic = requests.get(targetImg.get('src'))
    # print(targetImg)

    fp = open(position + targetImg.get('alt') + '.jpg', 'wb')
    fp.write(pic.content)
    fp.close()

    print("the next targetUrl => " + nextUrl + " ; the len : " + str(len(nextUrl)))
    if len(nextUrl) < 20:
        htmlInfo = getHtml("http://www.mm131.com/xinggan/" + nextUrl)
        getTargetImg(htmlInfo)


def doinio(beginindex,endindex):
    i = beginindex
    while i>endindex:
        i-=1
        htmlInfo = getHtml("http://www.mm131.com/xinggan/"+str(i)+".html")
        if htmlInfo=="":
            continue
        getTargetImg(htmlInfo)



# beginindex= int(sys.argv[1])
# endindex=sys.argv[2] if None else 1000
# print beginindex,endindex
doinio(2110,1000)
