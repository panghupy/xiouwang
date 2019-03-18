'''希鸥网添加文章'''
import requests
import json

'''
<li><label>信息标题<b>*</b></label><input name="info[title]" type="text" class="dfinput" value=""  style="width:518px;"/> <input type="checkbox" name="info[isgood]" value="1" > 推荐 </li>
					<li><label>内容关键字<b>*</b></label><input name="info[seokeywords]" type="text" id="seokeywords" value="" class="dfinput" style="width:518px;"></li>
					<li><label>内容简介<b>*</b></label><textarea name="info[seodescription]" id="seodescription" style="width:520px;height:100px;" class="dfinput"></textarea></li>
                    <li><label>发布人<b>*</b></label><input name="info[ftitle]" type="text" class="dfinput" value="" style="width:518px;"/></li>
					<li><label>阅读量<b>*</b></label><input name="info[hits]" type="text" id="hits" value="" class="dfinput" style="width:518px;"></li>
					<li><label>信息内容<b>*</b></label><textarea class="editor_id" name="info[content]" style="width:520px;height:350px;"></textarea></li>
					<li><label>封面图片<b>*</b></label><input name="img1" type="file" id="img1"> <font color="#FF0000">图片大小:20480K内,图片尺寸：317*217px</font></li>
					<li><label>创建时间<b>*</b></label><input name="info[sendtime]" type="text" class="dfinput" value="2019-03-18 10:42:04" style="width:150px;"/></li>
					<li><label>信息排序<b>*</b></label><input name="info[disorder]" type="text" class="dfinput" value="0" style="width:100px;"/> 注：数字越大越排在前 参考数值1- 4840 </li>			
'''
url = 'http://xiouhui.com/web_manage/news_add.php?pid=1&ty=45&tty=0&ttty=0'
headers = {
    'User-Agent': 'Mozilla/5.0(X11;Linux x86_64)AppleWebKit/537.36(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarynMKrhYz4DWGjdCsY',
    'Cookie': 'sys_guestid=1552825744; UM_distinctid=1698ba0ffb77a-085c7f08339b19-18211c0a-1fa400-1698ba0ffb8192; PHPSESSID=fpc2plrtr2ellkmbek4p918t93; CNZZDATA1273247885=1735094777-1552825778-%7C1552871506',
    'Referer': 'http://xiouhui.com/web_manage/news_add.php?pid=1&ty=45&tty=0&ttty=0', }

