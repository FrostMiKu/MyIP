# MyIP

手里闲置一台腾讯云学生机，家里又有动态公网
于是就写了个脚本，让家里的电子垃圾定时像服务器报告自己的IP

server.py 运行在云服务器上，可以通过11085端口的简易web页面查看当前的公网IP
client.py 运行在电子垃圾上，每30秒报告一次自己的IP给云服务器

支持 Python 2.7 - Python 3.9