# 适用于 windows
# 当程序不能用时，请访问:https://github.com/VonSdite/Auto_ishadow
# 如不能解决，联系本人， 122691411@qq.com
import urllib.request
import urllib.parse
import re
import subprocess
import json
import requests

url='http://ishadowsocks.info'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
res = requests.get(url=url, headers=headers)

if res.status_code:
    res.encoding = 'utf-8'

    content = res.text

#########################################
    # 爬取Japan第一个服务器的密码
#########################################
    pattern = re.compile(
        '<h4>Password:<span id="pwjpa">(.*)</span>  <span class="copybtn" data-clipboard-target="#pwjpa"><i class="fa fa-copy"></i></span></h4>', re.S)
    item = re.findall(pattern, content)

    password = item[0]
    # print(password)

    subprocess.call('taskkill /f /im shadowsocks.exe', stdout=subprocess.PIPE)
    # 更换为你的ss配置文件路径
    ssconfigpath = "E:\Shadowsocks\gui-config.json"
    with open(ssconfigpath, "r+") as f:
        data = json.load(f)
        data[u"configs"][0][u"password"] = password
        f.seek(0)
        json.dump(data, f, indent=4)

    # 更改为你的ss程序路径
    sspath = "E:\Shadowsocks\Shadowsocks.exe"
    subprocess.Popen(sspath)

    print("ok!")

else:
    print("error!")
