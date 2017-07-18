#实现原因:
**因为[http://ss.ishadowx.com/](http://ss.ishadowx.com/)上的密码每6小时会更换(0点, 6点, 12点, 18点)并重启服务器,导致每次都要重新打开网页去找密码,所以做了以下程序,每次只需启动程序就会重新获取密码,并打开shadowsocks,方便了使用**

    
#使用及注意:

 - 仅适用windows环境
 - 代码适用需要配置python3.0以上的版本, [python下载地址](https://www.python.org/downloads/windows/)
 - python需要用到requests模块
     - 下载requests模块的方法如下:
         - 在cmd输入即可:
         
            > pip install requests
        

 - **需要下载shadowsocks客户端, github中给出, download项目即可获得**
 - **使用时, 记得设置好代码的ssPath, ssConfigPath的路径(见shadowsocks.py)**


#实现代码:

 - 代码分两部分: 
     - 第一部分api_shadowsocks.py为设计的api接口类
     - 第二部分shadowsocks.py是使用举例
     
 - api_shadowsocks
     - 主要函数 setShadowSocks(self, pattern):
     
         - 用于爬取 [http://ss.ishadowx.com/](http://ss.ishadowx.com/) 上的服务器,密码,端口,加密方式,并将其设置到shadowsocks.exe的配置文件中
         
     - 函数getHtml(self), 用于获取页面的内容
     
     - 函数printItem(self, pattern), 显示爬取的服务器,密码,端口,加密方式
         
 - 实现思想
     - 爬取页面上的密码,服务器,端口,加密方式
         - 将爬取的信息设置到shadowsocks可执行程序的配置文件gui-config.json中
     - 判断shadowsocks.exe进程是否存在(因为一个目录下的shadowsocks.exe只能打开一个), 若存在, 则关闭.
     - 打开可执行程序shadowsocks.exe即可(记得启动系统代理)

![启动系统代理](1.png)

#使用批处理:

**本次提供了两种使用shadowsocks.py的方式:**

* Auto.bat:直接运行shadowsocks.py，注意Auto.bat路径更改后要修改相应的路径位置(见代码注释)
        （当网站密码可能在使用期间更改，当访问失效时，重新运行bat程序即可）  

* Auto_update.bat：增加加入计划任务的功能，令其在0,6,12,18,24点重新启动程序来重新获取密码   
    
*注意，Auto.bat以及Auto_update.bat是为了方便打开程序才提供的，如果不想修改其中路径问题，直接创建快捷方式放到桌面即可*

O(∩_∩)O妈妈再也不怕我掉线了    (路径问题见代码)



#不使用该项目的科学上网方法:
*   直接download项目中的shadowsocks
*   然后打开ishadow的网址: [http://ss.ishadowx.com/](http://ss.ishadowx.com/)
*   找到密码和服务器，更改到shadowsocks中，并启用服务代理即可