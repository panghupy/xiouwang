import requests
import time
import json

# 获取活动内容
url = 'https://www.huodongxing.com/event/7475570758200?utm_source=%e6%b4%bb%e5%8a%a8%e4%ba%ba%e6%b0%94%e6%8e%92%e8%a1%8c%e6%a6%9c&utm_medium=%e6%b4%bb%e5%8a%a8%e4%ba%ba%e6%b0%94%e6%8e%92%e8%a1%8c%e6%a6%9c&utm_campaign=ranklistpage&qd=6628363131252'

headers = {
    'uid': 'c3f4fb27-3bd6-4e9e-9d3f-783a47c72155',
    'ASP.NET_SessionId': 'ddp1frw2zfbxomzd1t4afyvb',
    'Appendhdmodalimg': 'Appendhdmodalimg',
    'qdcode_2479875859200': '628363131252',
    'qdcode_8479347906400': '6628363131252',
    'route': '1c148779685bf6c8f7fa768a9676bc01',
    'HDX_REGION': '%e5%8c%97%e4%ba%ac%2c%e5%8c%97%e4%ba%ac',
    'Hm_lpvt_d89d7d47b4b1b8ff993b37eafb0b49bd': str(time.time())[:11],
    '_ga': 'GA1.2.928356410.1552526521',
    '_gid': 'GA1.2.352944577.1552887423',
}

result = requests.get(url=url, headers=headers,verify=False).content.decode()

print(result)