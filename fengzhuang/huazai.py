

from appium import webdriver
import unittest
import time

# 启动参数
desired_caps={
    'platformName':'Android',
    'platformVersion':'4.4.2',
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.android.settings',
    'appActivity':'.Settings'
}

class Settest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_seting(self):
        #查看WLAN
        self.driver.find_element_by_id("android:id/title").click()
        time.sleep(3)
        #回退到设置页面
        self.driver.find_element_by_id("android:id/up").click()
        time.sleep(3)
        #打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
        element_info=self.driver.tap([(87,505),(141,542)],500)
        time.sleep(3)
        #返回到设置页面
        self.driver.find_element_by_id("android:id/up").click()
        time.sleep(3)

    def tearDown(self):
        #关闭驱动
        self.driver.quit()


print("*************************************************************")


from appium import webdriver
import time

# 启动参数
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#time.sleep(3)
# 生成一个driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
#查看WLAN
driver.find_element_by_id("android:id/title").click()
time.sleep(3)
#回退到设置页面
driver.find_element_by_id("android:id/up").click()
time.sleep(3)
#打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
driver.tap([(87,505),(141,542)],500)
time.sleep(3)
#返回到设置页面
driver.find_element_by_id("android:id/up").click()
time.sleep(3)
#关闭驱动
driver.quit()


print("*************************************************************")

import requests
import unittest
import json
from api_test import HTMLTestRunnerCN

class interfacetest01(unittest.TestCase):
    #实时天气查询接口
    def test01(self):
        url = 'https://tianqiapi.com/api'
        data = 'version=v6&appid=73691227&appsecret=123456'
        response = requests.request('GET',url,params=data)
        print(response.json())

#文件路径
Testcase_dir = 'C:\\Users\\EDY\PycharmProjects\\AutoTest\\api_test'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'Queryweatherreport.py')
filename = 'C:\\Users\\EDY\PycharmProjects\\AutoTest\\api_test\\Queryweatherreport.html'
fp = open(filename, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(
stream=fp,
title='接口测试报告',
description='用例执行情况：')
#runner.run(testunit)
runner.run(dis)
fp.close()


print("*************************************************************")

#coding:utf8
import requests
import unittest
class EasyBuyLogin(unittest.TestCase):
    #易买网登录接口
    def test01(self):
        url = 'http://localhost:8080/EasyBuy/Login'

        data = 'loginName=admin&password=123456&action=login'

        headers = {
            'Content-Type': 'application/x-www-from-urlencoded'
        }

        response = requests.request('POST', url, headers=headers, params=data)

        #print(response.text.encode('utf8'))
        #print(response.json())
        #获取返回的结果
        print(response.text)
        #获取状态码
        result = response.json()['status']
        print(result)
        #断言
        self.assertEqual(1,result)
        self.assertIn('登陆成功',response.text)
        self.assertTrue('操作成功'in response.text)
if __name__ == '__main__':
    unittest.main()

print("*************************************************************")

import requests
import json
import jsonpath

#生成token接口
url = "http://localhost:8000/login"
# python 字典 --》 json
data = {
    "username": "admin",
    "password": "admin"
}
res = requests.post(url=url, json=data)
#使用json包,打印json格式换行并且前面空四个空格，通过ascii防止乱码
print(json.dumps(res.json(), indent=4, ensure_ascii=False))
# 返回值是个列表 所以要加索引
# print(jsonpath.jsonpath(res.json(), "$..token")[0])

print("*************************************************************")

#登录jwt接口
urllogin = "http://localhost:8000/auth/hello"
#使用jsonpath来提取
token = "Bearer " + jsonpath.jsonpath(res.json(), "$..token")[0]
headers = {
    "Authorization":token
}
res1 = requests.get(url=urllogin,headers=headers)
print(json.dumps(res1.json(), indent=4, ensure_ascii=False))

print('************************************************************')

#上传文件接口
url = "http://httpbin.org/post"
# 准备一个文件
file = open("D:\学生消课.txt", "rb")
# 参数
files = {
    "file": file
}
res2 = requests.post(url=url, files=files)
#print(res.json())
print(json.dumps(res2.json(), indent=4, ensure_ascii=False))

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

import requests
import json

url='http://localhost:8080/EasyBuy/Login'
data='loginName=admin&password=123456&action=login'

#req=requests.request('POST',url=url,params=data)
req=requests.post(url=url,params=data)
print(req.text)
#print(json.dumps(req.json(),indent=4, ensure_ascii=False))

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

from selenium import webdriver
import time
import xlrd

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
#读取文件
data = xlrd.open_workbook("C:\\Users\\EDY\\PycharmProjects\\AutoTest\\data_driven\\data\\testcase01.xls")
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#使用for循环输出所有数据
list=[]
for i in range (0,table.nrows):
    # 只读取其中一行
    list = table.row_values(i)
    break
print(list)
#判断是否有网址需要打开
if(str(list[0])!=''):
    driver.get(list[0])
#判断执行关键字
if(str(list[2])==u'输入'):
    if(list[1]=='id'):
        driver.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
if(str(list[6])==u'点击'):
    if(list[5]=='id'):
        driver.find_element_by_id(list[7]).click()
time.sleep(3)
driver.close()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

from selenium import webdriver
import time
import xlrd

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
#读取文件
data = xlrd.open_workbook("C:\\Users\\EDY\\PycharmProjects\\AutoTest\\data_driven\\data\\testcase01.xls")
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#使用for循环输出所有数据
list=[]
for i in range (0,table.nrows):
    # 读取excel第一行
    list = table.row_values(i)
    break
print(list)
time.sleep(3)
#通过索引在excel表中获取百度URL
driver.get(list[0])
time.sleep(3)
#通过索引在excel表中获取百度输入框元素并输入要搜索的字段
driver.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
#通过索引在excel表中获取百度点击“百度一下”元素并点击
driver.find_element_by_id(list[7]).click()
time.sleep(3)
list=[]
for i in range (1,table.nrows):
    # 读取excel第二行
    list = table.row_values(i)
    break
print(list)
#跳转到“百度首页”
driver.find_element_by_css_selector(list[0]).click()
time.sleep(3)
driver.close()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

import os
import time

while 1 :
    now_time = time.strftime("%H:%M")
    if now_time == '16:28' or now_time == '17:21':
        os.chdir("C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test")
        os.system('python window.py')
        print (u'运行完成退出!')
        break
    else:
        time.sleep(3)
        print(now_time)

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#发送邮箱
sender = '443887994@qq.com'
port=465
#接收邮箱
receiver ='2217211022@qq.com'
#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/授权码
username = "443887994@qq.com"
password = "lyiydxwbexhfbhci"
# 邮件类型，获取各种附件需要用到
msgRoot = MIMEMultipart('related')
#邮件主题
msgRoot['Subject'] = '自动化测试报告'
#构造附件
att = MIMEText(open('C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test\\result.html', 'rb').read(), 'base64',
'utf-8')
#在响应类型为application/octet- stream情况下使用了这个头信息的话，那就意味着不直接显示内容，而是弹出一个”文件下载”的对话框
att["Content-Type"] = 'application/octet-stream'
#Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
att["Content-Disposition"] = 'attachment; filename="result.html"'
#读取附件
msgRoot.attach(att)
# 开启发信服务
smtp = smtplib.SMTP_SSL(smtpserver,port)
# 发件人邮箱账号、邮箱授权码
smtp.login(username, password)
# msg.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str
smtp.sendmail(sender, receiver,msgRoot.as_string())
#发件人邮箱中的SMTP服务器
smtp.connect('smtp.qq.com')
# 关闭服务器
smtp.quit()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

#发邮件
import smtplib
#用于构建内容文本
from email.mime.text import MIMEText
# 从email包引入Header()方法，Header()是用来构建邮件头的
from email.header import Header
#发送邮箱
sender = '443887994@qq.com'
#邮箱端口号
port=465
#接收邮箱
receiver = '2217211022@qq.com'
#发送邮件主题
subject = '测试执行结果'
#发送邮箱服务器
smtpserver = 'smtp.qq.com'
#发送邮箱用户/授权码
username = '443887994@qq.com'
password ='lyiydxwbexhfbhci'
#邮件信息对象（编写text类型的邮件正文）
msg = MIMEText('<html><h1>本次UI自动化通过率100%</h1></html>','html','utf-8')
#Subject来自哪里，指发件人的名称或地址
msg['Subject'] = Header(subject, 'utf-8')
# 开启发信服务
smtp = smtplib.SMTP_SSL(smtpserver,port)
# 发件人邮箱账号、邮箱授权码
smtp.login(username, password)
# msg.as_string()中as_string()是将msg(MIMEText或MIMEMultipart对象)变为str
smtp.sendmail(sender, receiver,msg.as_string())
#发件人邮箱中的SMTP服务器
smtp.connect('smtp.qq.com')
# 关闭服务器
smtp.quit()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

from ui_test import HTMLTestRunnerCN
import unittest
#文件路径
Testcase_dir = 'C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'danyuantest.py')
# 定义报告存放路径
filename = "C:\\Users\\EDY\\PycharmProjects\\AutoTest\\ui_test\\result.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
    # 运行测试用例
runner.run(dis)
#关闭报告文件
#fp.close()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

#coding:utf-8
from selenium import  webdriver
import unittest
import  time

class test(unittest.TestCase):
    def testduanyan(self):
        self.driver = webdriver.Chrome()
        #窗口最大化
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        #等待3秒
        time.sleep(3)
        #在搜索框输入china
        self.driver.find_element_by_id("kw").send_keys("china")
        time.sleep(3)
        #点击搜索按钮
        self.driver.find_element_by_id("su").click()
        time.sleep(10)
        #断言（断言是unittest自带的方法，必需与unittest一起用）
        #self.assertEqual(self.driver.find_element_by_xpath('//*[@id="su"]').get_attribute("value"),u'百度一下',"百度失败")

        #判断bool值为True或为False
        #self.assertTrue(self.driver.find_element_by_xpath('//*[@id="su"]').is_enabled())

        #检查某个元素是否存在,当元素存在则pass
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="su"]'))
        time.sleep(5)
        #退出浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

import pymysql

class Mysql(object):
    def mysql(sql):
        #连接数据库
        hostvalue='localhost'
        uservalue='root'
        passwordvalue='root'
        dbvalue='easybuy'
        portvalue=3306
        connection=pymysql.connect(host=hostvalue,user=uservalue,password=passwordvalue,db=dbvalue,
                                   port=portvalue,charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

        #通过cursors创建游标
        cursor=connection.cursor()
        #创建sql语句并执行
        sqlvalue=sql #'select * from easybuy_user'
        cursor.execute(sqlvalue)
        #查询数据库单条数据
        result=cursor.fetchone()
        #查询数据库多条数据
        #result=cursor.fetchall()
        #提交sql
        connection.commit()
        return result

    if __name__ == '__main__':
        # a=mysql(sql='select * from easybuy_user')
        # print(a)
        b=mysql(sql='select userName from easybuy_user where id=2')
        print(b)

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

from selenium import webdriver
import unittest
import time

class Test(unittest.TestCase):
    #在一个类中只会在所有测试用例运行前调用一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.baidu.com")
        cls.driver.maximize_window()

    #@unittest.skip('不执行此用例')
    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('china')
        #self.driver.find_element_by_name('wd').send_keys('中国')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        #回退到上一步
        self.driver.back()
        time.sleep(3)

    def test2(self):
        # 获取‘新闻’的元素并打新闻页面
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
        #暂停3秒
        time.sleep(3)
        #获取所有窗口
        self.handles =self.driver.window_handles
        #切换到新窗口
        self.driver.switch_to.window(self.handles[1])
        #暂停3秒
        time.sleep(3)
        #在新闻页面搜索‘国内新闻’
        self.driver.find_element_by_id('ww').send_keys('国内新闻')
        self.driver.find_element_by_id('s_btn_wr').click()
    #在所有测试用例运行后调用一次
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class Test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://localhost:8080/EasyBuy")

    def test1(self):
        self.driver.find_element_by_xpath('//html/body/div[5]/div/ul/li[2]/a').click()
        time.sleep(3)
        # el=self.driver.find_element_by_xpath('//html/body/div[6]/div[1]/div[2]/div[2]/ul/li[1]/div[4]/a[1]')
        # self.assertTrue(el.is_enabled(),"收藏失败")

    #@unittest.skip('不执行此用例')
    def test2(self):
        self.driver.find_element_by_xpath('//html/body/div[4]/div[2]/form/input[1]').send_keys('香水',Keys.ENTER)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

#方法一：
if __name__ == '__main__':
     unittest.main()

#测试套可以放在if __name__ == '__main__'下执行也可以直接执行

#方法二：
#创建一个测试套件，并向其中加载测试用例
#suite=unittest.TestLoader().loadTestsFromTestCase(Test)
#显式运行测试没并且通过设置verbosity设定对每一个测试方法产生测试结果；run中传入要执行的测试套件
#unittest.TextTestRunner(verbosity=2).run(suite)

#方法三：
# testunit = unittest.TestSuite()
# testunit.addTest(Test("test2"))
# unittest.TextTestRunner().run(testunit)

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

from selenium import webdriver
import time

class Mylib():

    def __init__(self):
        #初始化浏览器对象
        self.driver = webdriver.Chrome()

    def delay(self):
        #延迟等待
        self.driver.implicitly_wait(5)

    def open_url(self, url):
        #访问网站
        self.driver.get(url)
        self.delay()
        print('访问:%s成功'%url)

    def locate_element(self, locate_type, value):

        return self.driver.find_element(locate_type,value)
        #return self.driver.locate_element(locate_type,value)

    def __del__(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    web = Mylib()
    web.open_url('https://www.baidu.com')
    el = web.locate_element('id','kw')
    el.send_keys('itcast')
    el_sub = web.locate_element('id','su')
    el_sub.click()

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

class People():
    def hand(self):
        print('这是我朋友的手')
    def foot(self):
        print('这是我朋友的脚')
if __name__ == '__main__':
    goodfriend = People()
    print(goodfriend.hand())
    print(goodfriend.foot())

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
#i 表示第几轮“冒泡”(对比的轮数是实际的长度-1)
for i in range(1, len(array)):
    #j 表示“走访”到的元素索引，每一轮“冒泡”中，j 需要从列表开头“走访”到 len(array) - i 的位置
        for j in range(0, len(array) - i):
            #列表中第j个元素大于第j+1个元素
            if array[j] > array[j + 1]:
                #升序
                array[j], array[j + 1] = array[j + 1], array[j]
print(array)

#1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

