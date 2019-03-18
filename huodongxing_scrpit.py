import requests
from lxml import etree
import json

url = 'https://www.huodongxing.com/ranklist'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
response = requests.get(url, headers=headers).content.decode()
html = etree.HTML(response)
with open('test.html', 'w')as f:
    f.write(response)
popularity_list = html.xpath('.//div[@class="popularity-son-item flex"]')
for item in popularity_list:
    # 活动标题
    title = item.xpath('.//img[@class="item-logo"]/@alt')[0]
    # 活动封面图片
    img_url = item.xpath('.//img/@src')
    # 活动地点
    location = item.xpath('.//p[@class="item-dress-pp"]/text()')[0]
    # 活动时间
    activity_time = item.xpath('.//p[@class="item-data flex"]')[0].xpath('string(.)')
    # 活动报名链接
    activity_link = 'https://www.huodongxing.com/'+item.xpath('.//a[@class="flex popularity-son-item-right"]/@href')[0]
    # 活动内容
    content_response = requests.get(url=activity_link, headers=headers).content.decode()
    content_response_html = etree.HTML(content_response)
    article = content_response_html.xpath('.//div[@class="article"]')[0].xpath('string(.)')
    print(article)
    break
