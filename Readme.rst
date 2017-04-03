不使用本項目方法:[另附]_
	
***********************************************
ishadow的目前网址为:http://abc.ishadow.online/
***********************************************

``注：访问不到时，可能是ishadow网址变更了``


注意
====
*	仅提供windows方法
*	本程序需要电脑配置python3.0以上的版本并且需要用到requests模块
python下载地址:https://www.python.org/downloads/windows/

下载requests模块的方法:在cmd中输入
	``pip install requests``	
*	本次对自启动进行了修改，利用计划任务实现shadowsocks永不掉线的方法,即令其在0,6,12,18,24点重新启动程序来重新获取密码  
    
|

使用方法:
=========
  
|  
1.	**先下载shadowsocks客户端，**
  	链接：http://pan.baidu.com/s/1nvPVhgt 密码：drxv
2.	**Download本项目，使用时，先将net.py代码中的目录位置更改到你存放shadowsocks的目录（见代码注释）**   
3.	**本次提供了两种使用net.py的方式:**
    
	*	Auto.bat:直接运行net.py，注意Auto.bat路径更改后要修改相应的路径位置(见代码注释)
	 	（但网站密码可能在使用期间更改，当访问失效时，重新运行bat程序即可）   
	*	Auto_update.bat：增加加入计划任务的功能，令其在0,6,12,18,24点重新启动程序来重新获取密码   
	
	| 
	``注意，Auto.bat以及Auto_update.bat是为了方便打开程序才提供的，如果不想修改其中路径问题，直接创建快捷方式放到桌面即可``

O(∩_∩)O妈妈再也不怕我掉线了    (路径问题见代码)
:::::::::::::::::::::::::::::::::::::::::::::::


.. [另附] 
不使用该项目的方法:
-------------
*	直接download百度云内的shadowsocks
*	然后打开ishadow的网址，找到密码和服务器，更改到shadowsocks中，并启用服务代理