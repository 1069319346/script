#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 扇贝清空词库脚本
import requests
import sys
import time
import json

def main():
    payload = {'pass': '1', 'force': '1'}
    header = {
        # 用户cookie，使用时需要设置
        'cookie': '1',
        'referer' : 'https://www.shanbay.com/bdc/learnings/library/',
        'user-agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    # 页数，使用时需要设置
    for i in range(1,2):
        url = "https://www.shanbay.com/api/v1/bdc/library/master/?page=%s&_=%s" % (str(1), str(int(time.time())))
        r = requests.get(url, headers = header)
        data = json.loads(r.text)
        print(data['data']['objects'])
        for i in data['data']['objects']:
            learning_id = i['learning_id']
            print(learning_id)
            learning_url = "https://www.shanbay.com/api/v1/bdc/learning/%s/" % (str(learning_id))
            print(learning_url)
            lr = requests.put(learning_url, headers = header, data = payload)
            print(lr.text)


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    main()