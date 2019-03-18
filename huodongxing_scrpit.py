import requests
from lxml import etree
import json
import time

url = 'https://www.huodongxing.com/ranklist'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'uid=c3f4fb27-3bd6-4e9e-9d3f-783a47c72155;ASP.NET_SessionId=ddp1frw2zfbxomzd1t4afyvb;Appendhdmodalimg=Appendhdmodalimg;qdcode_2479875859200=628363131252;qdcode_8479347906400=6628363131252;route=1c148779685bf6c8f7fa768a9676bc01;HDX_REGION=%e5%8c%97%e4%ba%ac%2c%e5%8c%97%e4%ba%ac;Hm_lpvt_d89d7d47b4b1b8ff993b37eafb0b49bd=' + str(
        time.time())[:11] + ';_ga=GA1.2.928356410.1552526521;_gid=GA1.2.352944577.1552887423',
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
    activity_link = 'https://www.huodongxing.com/' + item.xpath('.//a[@class="flex popularity-son-item-right"]/@href')[
        0]
    # 活动内容暂时不获取
    # content_response = requests.get(url=activity_link, headers=headers).content.decode()
    # content_response_html = etree.HTML(content_response)
    # article = content_response_html.xpath('.//div[@class="article"]')[0].xpath('string(.)')
    # print(article)
    print('活动标题：　', title)
    print('活动地点：　', location)
    print('活动时间：　', activity_time)
    print('活动报名链接：　', activity_link)
    print('活动封面图片：　', img_url)
