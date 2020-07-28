#!/usr/bin/python3
import sys,os,requests

print ("获取当前目录中……")
filepath = os.getcwd()
print ("当前文件路径为",filepath)
fileurl = input("下载链接：")
r = requests.get(fileurl)
with open("python_logo.png",'wb') as f:
    f.write(r.content)