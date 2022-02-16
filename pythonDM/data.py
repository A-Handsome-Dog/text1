from selenium import webdriver
import time
import xlrd

#获取驱动，窗口最大化。
driver = webdriver.Chrome()
driver.maximize_window()
#读取xls文件。
xls = xlrd.open_workbook("C:\\Users\\EDZ\\Desktop\\bilibili.xls")
#选择文件的第一张表
biao = xls.sheet_by_name("Sheet1")

#创建空列表
list=[]
for i in range(0,biao.nrows):
    list = biao.row_values(i)
    break
print(list)
#打开网址
driver.get(list[0])
time.sleep(3)
#搜索框输入：xxx
driver.find_element_by_class_name(list[2]).send_keys(list[3])
time.sleep(1)
#点击搜索
driver.find_element_by_class_name(list[5]).click()
time.sleep(3)
#获取所有标签页
all = driver.window_handles
driver.switch_to.window(all[-1])
#点击最多播放
driver.find_element_by_xpath(list[7]).click()
time.sleep(3)

list2=[]
#选择表的第二行
for a in range(1,biao.nrows):
    list2 = biao.row_values(a)
    break
# print(list2)
#点击哔哩哔哩首页
driver.find_element_by_class_name(list2[0]).click()

