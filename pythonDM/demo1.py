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
# from class1 import Test_case
# a= int(input("第一个正整数："))
# b = int(input("第一个正整数："))
# print(Test_case().jieguo(a,b)) #答案 = (a*b)+(a+b)


# from class1 import People
# if __name__ == "__main__": # 创建一类的实例，初始化：girl/live
#     girlfriend = People() # 访问类的属性
#     print (girlfriend.girl)
#     print (girlfriend.live)

# from class1 import Lei
# if __name__ == '__main__':
#     dogcat = Lei()
#     print(dogcat.ahd)
#     print(dogcat.ahc)

# import random
# a=0
# b=100
# key = random.randint(a,b)
#
# while 1:
#     cai= int(input("请输入%d-%d其中一个整数："%(a,b)))
#     if cai < key and cai > a:
#         a=cai
#         print("请输入%d"%a+"到%d"%b)
#     elif cai > key and cai <b:
#         b=cai
#         print("请输入%d"%a+"到%d"%b)
#     elif cai < 0 or cai > 100:
#         print("兄弟别搞啊！！！")
#     elif cai==key:
#         print("终于猜对了！！！")
#         break

arr = [5,3,1,2,0,8,4]
index = [2,0,4,0,1,3,5,1,6,0]
QQ = ""
for i in index:
    QQ += str(arr[i]) #通过索引i查找对应arr列表中的数据，并拼接打印出来
print("联系方式QQ："+QQ)



