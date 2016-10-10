# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth
from qiniu import BucketManager

access_key = 'dR_jD1jSeI02UQvyvyCn50nD8xHICg-rRtjY9C-1'
secret_key = 'gjFmDy7tPB5oXpm7ZlGkL8ZXEVUZk5I_9c9Urs6e'

#初始化Auth状态
q = Auth(access_key, secret_key)

#初始化BucketManager
bucket = BucketManager(q)

#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'likeli-img'
key = 'python-logo.png'

#获取文件的状态信息
ret, info = bucket.stat(bucket_name, key)
print(info)
assert 'hash' in ret
