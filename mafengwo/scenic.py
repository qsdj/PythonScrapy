# coding=utf-8
import urllib
import urllib2
import cookielib
import json
import sys
from bs4 import BeautifulSoup

send_headers = {
    "Host": "mapi.mafengwo.cn",
    "Connection": "keep-alive",
    "Proxy-Connection": "keep-alive",
    "Accept-Webp": 1,
    "Accept": "*/*",
    "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "TravelGuideMdd/7.6.1 (iPhone; iOS 9.0.2; Scale/2.00),Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13A452 mfwappcode/cn.mafengwo.www mfwappver/7.6.1 mfwjssdk/0.1"
}

mafengwo = "https://mapi.mafengwo.cn/travelguide/poi/pois/mdds/10030?app_code=cn.mafengwo.www&app_ver=7.6.1&channel_id=App%20Store&device_token=ae0c62f4a8b9acae331d5f2a9d29a5493782adf253f2ecb0eba00d6d9cbc0cfd&device_type=ios&hardware_model=iPhone6%2C1&idfa=A81C8C50-3D09-4FCF-A585-387E47636C75&idfv=F05A0796-76D7-4349-9C0A-33B0F1BCBC1F&mfwsdk_ver=20160401&o_lat=39.780783&o_lng=116.545751&oauth_consumer_key=4&oauth_nonce=74f54454-c1ce-4291-ba10-4ab427b85be5&oauth_signature=rvEoXpbV2deYKoc4S5F/hD1px4M%3D&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1475988936&oauth_token=0_d5af5e71fbcea723b6af2ddae8ab084a&oauth_version=1.0&open_udid=F05A0796-76D7-4349-9C0A-33B0F1BCBC1F&screen_scale=2&start=0&sys_ver=9.0.2&time_offset=480&type_id=3&x_auth_mode=client_auth"


def GET(url):
    opener = urllib2.Request(url, headers=send_headers)
    res = urllib2.urlopen(opener)
    return res.read()


def Do():
    html = GET(mafengwo)
    jsonInfo = json.loads(html)
    print jsonInfo["data"]["list"][0]["name"]


Do()
