# # print("let me see see you watch!")
# # name = "罗翔"
# # age = 43
# # weight = 74.3
# # %d：是替换整数，%s：替换字符串，%f：替换小数，print（）是输出打印的意思。
# # print("我的名字叫：" + name)
# # print("我的年龄：%i" % age)
# # print("体重：%.2f" % weight)
# # print("\n")
#
#
# # 一行输出,\n代表换行，想要显示出\n出来就:print("\\n")
# #print("我的名字叫：%s,我的年龄：%i岁,体重：%.2fKG" % (name, age, weight))
# # input()里输出的都自带""，都属于字符串；type()输入你想查看的数据查看数据类型。
# # int()把括号里的值强制转换成int的数据类型。
# # str()把括号里的值强制转换成string的数据类型。
# # CJ = input("请输入你的成绩：")
# # if int(CJ) > 88:
# #     print("奖励鸡腿")
# # else:
# #     print("奖励大嘴巴子")
# # and：并且；or：或者；not：不是。
# # user = input("请输入你的用户名：")
# # passwd = input("请输入你的密码：")
# # if user == "张三" and passwd == "123456":
# #     print("恭喜登陆成功！")
# # else:
# #     print("用户名或密码有误。")
#
#
# nu=int(input("输入数字:"))  #   true=1 false=0
# if nu%2:
#     print('nu是偶数')
# else:
#     print('nu是奇数')
# # a="88888888"
# # # print(a[1:4])
# # #print(len(a))
# # print(a.count("8"))
# #b=[1,2,3,4,5,6,7,8,9,10]
# # s=0
# # for i in b:
# #     s=s+i
# # print(s)
# # b.append(0) #末尾插入数据
# # del b[3] #按照下标来删除
# # b.remove(2) #按照写入的数字删除
# #b[6]=99 #按照下标来改数据
# # b.pop()
# # print(b)
# # print(b[8])
#
# array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# #print (list(range(1,len(array))))
# #i 表示第几轮“冒泡”(对比的轮数是实际的长度-1)
# # for i in range(1, len(array)):  #17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21
# #     #range()函数：左边为开始，右边为结束，但不能大于等于结束值，直接写数字range就会给他切片（10就会分成0，1，2...9）
# #     #j 表示“走访”到的元素索引，每一轮“冒泡”中，j 需要从列表开头“走访”到 len(array) - i 的位置
# #         for j in range(0, len(array) - i): #10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36
# #             #列表中第j个元素大于第j+1个元素
# #             if array[j] > array[j + 1]:
# #                 #升序
# #                 array[j], array[j + 1] = array[j + 1], array[j]
# # print(array)

# i=[5,2,6,9,12,54,22,0]
# # i.sort()
# # print(i)

# dict = {}
# dict['one']= "This is one"
# dict[2]="This is two"


#tinydict = {'name': 'john','code':6734,'dept': 'sales'}


#print (dict['one'])          # 输出键为'one' 的值
# print (dict[2])              # 输出键为 2 的值
# print (tinydict)             # 输出完整的字典
# print (tinydict.keys())      # 输出所有键
# print (tinydict.values())    # 输出所有值

# a = { '1':'1', '2':'23' }
# b = { '3':123, '4':'1234' }
#
# c = dict ( a, **b)
#
# print(c)

# dict = {
#     'one':"This is one",
#     2 : "This is two",
#     3:"This is three",
# }
#
# print (dict['one'])          # 输出键为'one' 的值

# s=0
# for i in range(100):
#     if i%2==0:
#         s=s+i
#     else:
#         continue
# print(s) #0-99的偶数相加

# s=0
# for i in range(100): #range（100）切片成0-99
#     if i%2:
#         s=s+i
#         if s > 1024:
#             break
#     else:
#         continue
# print(s) #当s奇数相加到大于1024时就跳出循环打印出s的数
#

# s=0
# i = 1
# while i <= 100 :
#     if i>0:
#         s=s+i
#         if s > 5000:
#             break
#     i=i+1
# print(s)

# s=0
# i = 1
# while i <= 10 :
#     if i>0:
#         s=s+i
#     # else:
#     #     pass
#     i=i+1
#     print(s)


# c = int(input("请输入一个整数："))
# if not c>100:
#     print(c+100)

# import random
# a = 1
# b = 99
# key = random.randint(1, 100)
# #函数功能：
# #random.randint(参数1，参数2)；参数1、参数2必须是整数；函数返回参数1和参数2之间的任意整数
#
# while 1:
#     guess = int(input("请输入一个整数%d" % a + "到%d:" % b))
#     if guess<key and guess > a:
#         a = guess
#         print('请输入%d到' % a+"到%d:" % b)
#     elif guess>key and guess<b:
#         b = guess
#         print('请输入%d' % a+"到%d:" % b)
#     elif guess <= 1 or guess >= 100:
#         print("小伙子，别调皮，请重新输入")
#     elif guess == key:
#         print('真聪明，猜对了！')
#         break

# class lei():
#     def nu1(self,a,b):
#         return a*b
#     def nu2(self,a,b):
#         return a+b
#     def jieguo(self,a,b):
#         return self.nu1(a,b)+self.nu2(a,b)
#t = lei()
#from class1 import Test_case
# import class1
# a= int(input("第一个正整数："))
# b = int(input("第一个正整数："))
# print(class1.Test_case().jieguo(a,b)) #答案 = (a*b)+(a+b)

# import requests
# import unittest
# import json
#
# class Easybuy(unittest.TestCase):
#     # 易买网登录
#     def test_01(self):
#         #获取url地址
#         dz = "http://localhost:8080/EasyBuy/Login"
#         #获取参数
#         sj = "loginName=admin&password=123456&action=login"
#         #
#         res = requests.request("get",url=dz,params=sj)
#         print(res.json())
#         #获取状态码
#         ztm = res.json()['message']
#         print(ztm)
#         #断言
#         self.assertTrue("操作成功"in res.text)
#
# if __name__ == '__main__':
#     unittest.main()

# from appium import webdriver
# import time
#
# desired_caps={}
#
# #启动参数
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.2'
# desired_caps['deviceName'] = '127.0.0.1:62001'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = '.Settings'
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wb/hub",desired_caps)
# time.sleep(3)
# driver.tap([(87,505),(141,542)],500)
# time.sleep(1)
# driver.find_element_by_id("android:id/up").click()
# # driver.tap([(0,56),(24,80)],500)
# time.sleep(2)
# driver.quit()

from appium import webdriver
import time

# 启动参数
desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'e0eadcb5'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# desired_caps={
#     'platformName':'Android',
#     'platformVersion':'4.4.2',
#     'deviceName':'127.0.0.1:62001',
#     'appPackage':'com.android.settings',
#     'appActivity':'.Settings'
# }

#time.sleep(3)
# 生成一个driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
#查看WLAN
# driver.tap([(210,1393),(480,1454)],500)
# # driver.tap([(87,164),(164,201)],500)
# time.sleep(2)
# #回退到设置页面
# driver.find_element_by_id("smartisanos:id/btn_back").click()
# time.sleep(2)
#打开显示页面（当各菜单元素相同时用模拟手指点击（tap），取bounds的值,后面的500是持续时间，单位毫秒）
# driver.tap([(87,505),(141,542)],500)
# time.sleep(3)
# #返回到设置页面
# driver.find_element_by_id("android:id/up").click()
# time.sleep(3)
#关闭驱动
driver.quit()
