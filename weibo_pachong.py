import requests
import re
import json
from pyquery import PyQuery as pq
from dingtalkchatbot.chatbot import DingtalkChatbot
#模拟发送http请求
#网站站点
# url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%23%E6%81%8B%E4%B8%8E%E5%88%B6%E4%BD%9C%E4%BA%BA%23%26t%3D0&page_type=searchall&page=%s'%page
#防反爬
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}

def message(pages):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=67b81ffbcb0c8ddaa7d52aaeb1268cd9f74f83557c8475af7d66e4dcbfa10ba8'
    dbj = '近期疑似bug微博：'
    aaa = ['bug','补偿','道歉','只有我一个人','只有我一人','Bug','维护','问题','闪退','进不去','丑','红点','充值不了']
    for i in range(1,pages):
        page = i
        #恋与超话
        # url = 'https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D61%26q%3D%23%E6%81%8B%E4%B8%8E%E5%88%B6%E4%BD%9C%E4%BA%BA%26t%3D0&page_type=searchall&page='+str(page)
        #恋与所有话题
        url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%E6%81%8B%E4%B8%8E%E5%88%B6%E4%BD%9C%E4%BA%BA%26t%3D0&page_type=searchall&page='+str(page)
        #闪暖
        # url = 'https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D61%26q%3D%23%E9%97%AA%E8%80%80%E6%9A%96%E6%9A%96%23%26t%3D0&page_type=searchall&page='+str(page)
        #get发送请求
        response = requests.get(url,headers=headers)
        #网站编码转为utf-8
        response.encoding = 'utf-8'
        #网站源码
        html = response.json()
        items = html.get('data').get('cards')
        for item in items:
            address = {'scheme': item.get('scheme')}
            item = item.get('mblog')
            if item:
                data = {
                    'created_at': item.get('created_at'),
                    'text': pq(item.get('text')).text(),
                    # 'scheme': item.get('scheme')
                }
                for m in aaa:
                    if m in data['text']:
                        dbj = dbj + '\n\n('+ data['created_at'] + ')微博内容:'+ data['text'] +'\n链接:'+address['scheme']
                        # bbb.append(alili)
                        # print('内容:',data['text'],'\n链接:',address['scheme'],'\n时间:',data['created_at'])
    # 测试群
    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=67b81ffbcb0c8ddaa7d52aaeb1268cd9f74f83557c8475af7d66e4dcbfa10ba8'
    # 正式群
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=496bba9ad5a29cf969048c3966de4c1d976c95bc7909883a3b485c54c545c130'
    robot_excel = DingtalkChatbot(webhook)
    robot_excel.send_text(dbj)
if __name__ == '__main__':
    pages = 20
    message(pages)
    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=67b81ffbcb0c8ddaa7d52aaeb1268cd9f74f83557c8475af7d66e4dcbfa10ba8'
    # robot_excel = DingtalkChatbot(webhook)
    # robot_excel.send_text(dbj)

