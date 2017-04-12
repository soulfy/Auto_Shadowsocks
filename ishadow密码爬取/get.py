import requests
import datetime as time
import tkinter as tk
import re

#get请求
response = requests.get(url='http://free.ishadow.online/')

#判断返回状态
if response.status_code:
	response.encoding = 'utf-8'

	t_dict = dict()					
	content = response.text

#########################################
	#爬取Japan第一个服务器的密码
#########################################
	pattern = re.compile('<h4>Password:<span id="pwjpa">(.*)</span>  <span class="copybtn" data-clipboard-target="#pwjpa"><i class="fa fa-copy"></i></span></h4>', re.S)
	item = re.findall(pattern, content)
	t_dict['服务器ip']='a.jpip.pro'
	t_dict['服务器端口']='443'
	t_dict['加密']='aes-256-cfb'
	t_dict['密码']=item[0]


	# 保存到文件中，便于查看记录
	file_name = 'save.txt'
	with open(file_name, 'a') as f:
		f.write("------------------------------------------------\n")
		f.write('写入时间: ' + time.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
		try:
			#弹出窗口，便于当前复制
			root = tk.Tk()
			root.geometry('400x400+600+200')
			listb = tk.Listbox(root, width=50, height=20, font=('黑体', 14))

			for key in t_dict:
				f.write(key+':\n'+t_dict[key]+'\n\n')
				listb.insert(0, '\n')
				listb.insert(0, t_dict[key])
				listb.insert(0, key+':')

			listb.pack()
			root.mainloop()
		except:
			f.write('写入失败!!\n')
        	
else:
	print('打开失败，请查看网络或稍后重试.....')
