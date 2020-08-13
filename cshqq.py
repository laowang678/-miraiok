# -*- coding:utf-8 -*-
import os
import shutil
import time

cqhttp = "app"
exename = "miraiOK_windows_386.exe"

print u"机器人程序名为miraiOK_windows_386.exe，请不要更改"

##print u"请把文件夹拉进来"
##zh = raw_input()
print u"请输入帐号，按回车继续"
zh = raw_input()
print u"请输入密码，按回车继续"
mm = raw_input()
with open("config.txt","wb+") as a:
    a.write("""#DEBUG
#NOUPDATE
#
----------


login %s %s
""" % (zh,mm))
shutil.copy("%s.dll" % cqhttp, ".\plugins\MiraiNative\plugins")
shutil.copy("%s.json" % cqhttp, ".\plugins\MiraiNative\plugins")
startexe = ("start %s" % (exename)).encode('gbk')
os.system(startexe)
print u"登录成功后按回车继续"
raw_input()
print u"正在继续，请等待10秒"

time.sleep(10)
arg = 'taskkill /f /im "%s"' % exename
os.system(arg.encode('gbk'))
time.sleep(2)
arg = 'taskkill /f /im "%s"' % "java.exe"
os.system(arg.encode('gbk'))
time.sleep(2)
with open("oneqq.json","rb+") as a:
    with open(".\plugins\MiraiNative\data\io.github.richardchien.coolqhttpapi\config\%s.json" % zh,"wb+") as b:
        b.write(a.read())
print u"完成了，按回车结束"
raw_input()
