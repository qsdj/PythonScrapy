# coding=utf-8

import urllib
import urllib2
import json
import connect
import sys

send_headers = {
    "Host": "m.api.youpu.cn",
    "ypimg": "%7B%0A%20%20%22sPic%22%20:%20%7B%0A%20%20%20%20%22w%22%20:%20%22193%22,%0A%20%20%20%20%22h%22%20:%20%22193%22%0A%20%20%7D,%0A%20%20%22screen%22%20:%20%7B%0A%20%20%20%20%22w%22%20:%20%22640%22,%0A%20%20%20%20%22h%22%20:%20%221136%22%0A%20%20%7D,%0A%20%20%22bPic%22%20:%20%7B%0A%20%20%20%20%22w%22%20:%20%22640%22,%0A%20%20%20%20%22h%22%20:%20%22360%22%0A%20%20%7D%0A%7D",
    "identity": "72F00FDF-94BD-4B86-8D22-9C922A068486",
    "ypmtype": "iPhone 5S",
    "Accept": "*/*",
    "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Version": "3.2.6",
    "User-Agent": "YoupuTrip/3.2.6 (iPhone; iOS 9.0.2; Scale/2.00)"
}

youpulvxing = "http://m.api.youpu.cn/country/getDestList?package=i2&paramType=get&showType=letter&sign=1fa9190e3c354c88ae2947296fb5a08d&timestamp=1475027072"


# youpu_city = "http://m.api.youpu.cn/Customline/getCustomCityListByCountryId?countryid=161&package=i2&paramType=get&sign=32528dc430ca91b2d6f5dd6253509189&timestamp=1475027780"

def GET(url):
    opener = urllib2.Request(url, headers=send_headers)
    res = urllib2.urlopen(opener)
    return res.read()


def Do():
    try:
        html = GET(youpulvxing)
        jsonInfo = json.loads(html)
        targeList = jsonInfo['data']['countryList']
        for i in range(len(targeList)):
            countryLists = targeList[i]['list']
            for j in range(len(countryLists)):
                cnNames = countryLists[j]
                lists = {
                    "id": (" ", cnNames["id"])[cnNames["id"] <> ""],
                    "cnName": (" ", cnNames["cnName"])[cnNames["cnName"] <> ""],
                    "type": (" ", cnNames["type"])[cnNames["type"] <> ""],
                    "pic": (" ", cnNames["pic"])[cnNames["pic"] <> ""],
                    "jsonData":json.dumps(cnNames, ensure_ascii=False)
                }
                print lists["id"], lists["cnName"], lists["type"], lists["pic"]
                connect.InsertCountry(lists)

    except Exception, e:
        print "没有这个数据", e


Do()
