'''希鸥网添加文章'''
import requests
import json

import requests
import json
import random


def add(title, content, cover_img_name):
    url = 'http://xiouhui.com/web_manage/news_add.php?pid=1&ty=45&tty=0&ttty=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15',
        'Cookie': 'UM_distinctid=1697a0b538f2d0-0e0dfe104b5295-49183405-232800-1697a0b5390506; CNZZDATA1273247885=71788213-1552871280-http%253A%252F%252Fxiouhui.com%252F%7C1552871280; PHPSESSID=dj80rqmko351eu5j34fra9qqu2; sys_guestid=1552871275',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarySQqMKpHHXTzK0LMb',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }

    form_data = '''
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[pid]"
    
    1
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[ty]"
    
    45
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[tty]"
    
    0
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[ttty]"
    
    0
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[title]"
    
    标题
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[seokeywords]"
    
    内容关键字
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[seodescription]"
    
    内容简介
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[ftitle]"
    
    发布人
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[hits]"
    
    阅读量
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[content]"
    
    <p>
        信息内容&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    </p>
    <p>
        <br />
    </p>
    <p>
        <br />
    </p>
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="img1"; filename="WechatIMG179.jpeg"
    Content-Type: image/jpeg''' + open('WechatIMG179.jpeg', 'rb') + '''
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[sendtime]"
    
    2019-03-18 12:05:46
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="info[disorder]"
    
    0
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb
    Content-Disposition: form-data; name="dosubmit"
    
    马上发布
    ------WebKitFormBoundarySQqMKpHHXTzK0LMb--
    '''
    result = requests.post(url=url, headers=headers, data=form_data).content.decode()
    return result


print(add(title='不是标题', content='没啥东西', cover_img_name=''))
