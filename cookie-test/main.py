# coding=utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup

# 百词斩, 拿这个网站的登录做个样例, 这个网站的登录模式很像你现在的市发改委网站
# 这里引用的包都是用的上的,你看过我之前写的代码,应该都比较熟悉了.
# 百词斩的登录入口 : http://www.baicizhan.com/login
# 这个网站的登录方式同样是form表单提交验证,里面有防伪码,还有一些其他的附加内容,同样
# 没有验证码,这家网站通过cookie来保持登录状态
# 这些代码我调试了,已经通过,你可以自己阅读以下,很简单.
# 请注意变量的作用域,那些是全局的.
# 你最终拿到的应该是json数据那么就导入json包来解析吧,这里我就略过了.

# cookielib 官方文档:https://docs.python.org/2/library/cookielib.html


email = "1603411701@qq.com"   # 账号
raw_pwd = ""                  # 密码

data = {
    'utf8' : '✓',
    'authenticity_token' : '',  # 网站的防伪标签
    'email' : email,
    'raw_pwd' : raw_pwd,
    'remember_me' : 0
}


def POST(url, data):
    post_data = urllib.urlencode(data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

    try: response = opener.open(url, post_data)
    except urllib2.URLError, e:
        # 网络请求的包一定要自己封装一个,而且要做错误处理,不然...
        print '网络请求发生一个错误:', e.reason

    return response.read()

# 获取网站的form表单内容,并开始自动管理cookie
soup = BeautifulSoup(POST("http://www.baicizhan.com/login",{}), 'lxml')

# 提取防伪标签
data['authenticity_token'] = soup.select('input[name=authenticity_token]')[0]['value']

# 开始获取登录后的首页内容
indexSoup = BeautifulSoup(POST("http://www.baicizhan.com/login", data), 'lxml')

# 提取目标内容
target = indexSoup.select('div[class*=index_left_topbar]')[0]

print target.get_text()


