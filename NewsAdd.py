'''希鸥网添加文章'''
import requests
import json
import time
import requests
import json
import random


def add(title, content):
    url = 'http://xiouhui.com/web_manage/news_add.php?pid=1&ty=45&tty=0&ttty=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15',
        'Cookie': 'UM_distinctid=1697a0b538f2d0-0e0dfe104b5295-49183405-232800-1697a0b5390506; CNZZDATA1273247885=71788213-1552871280-http%253A%252F%252Fxiouhui.com%252F%7C1552871280; PHPSESSID=dj80rqmko351eu5j34fra9qqu2; sys_guestid=1552871275',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySQqMKpHHXTzK0LMb',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    boundary = '----WebKitFormBoundarySQqMKpHHXTzK0LMb'
    form_data_list = [boundary+'\r\nContent-Disposition: form-data;name="info[pid]"\r\n\r\n1\r\n',
                      'Content-Disposition: form-data;name="info[pid]"\r\n\r\n1\r\n',
                      'Content-Disposition: form-data;name="info[ty]"\r\n\r\n45\r\n',
                      'Content-Disposition: form-data;name="info[tty]"\r\n\r\n0\r\n',
                      'Content-Disposition: form-data;name="info[ttty]"\r\n\r\n0\r\n',
                      'Content-Disposition: form-data;name="info[title]"\r\n\r\n' + title + '\r\n',
                      'Content-Disposition: form-data;name="info[seokeywords]"\r\n\r\n' + title + '\r\n',
                      'Content-Disposition: form-data;name="info[ftitle]"\r\n\r\n转载\r\n',
                      'Content-Disposition: form-data;name="info[hits]"\r\n\r\n' + str(
                          random.randint(1500, 2500)) + '\r\n',
                      'Content-Disposition: form-data;name="info[content]"\r\n\r\n' + content + '\r\n',
                      'Content-Disposition: form-data;name="img1";filename="cover.png"\r\nContent-Type:image/jpeg\r\n\r\n'+str(open('cover.png', 'rb').read())+'\r\n',
                      'Content-Disposition: form-data;name="info[sendtime]"\r\n\r\n'+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+'\r\n',
                      'Content-Disposition: form-data;name="info[disorder]"\r\n\r\n0\r\n',
                      'Content-Disposition: form-data;name="dosubmit"\r\n\r\n马上发布\r\n'+boundary]

    all_data = (boundary+'\r\n').join(form_data_list)
    print(all_data)
    result = requests.post(url=url, headers=headers, data=all_data.encode()).content.decode()
    return result

print(add(title='不是标题', content='没啥东西'))
