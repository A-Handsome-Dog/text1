import time
from fengzhuang.main import Fengzhuang

if __name__ == '__main__':
    #打开百度首页
    wy = Fengzhuang()
    wy.open("https://www.baidu.com/")
    #在搜索框输入：QQ邮箱
    wy.ss("name","wd").send_keys("QQ邮箱")
    #点击百度一下
    wy.ss("id","su").click()
    time.sleep(4)
    #点击QQ邮箱
    wy.ss("xpath",'//*[@id="1"]/h3/a[1]').click()
    #选择最新的标签页
    wy.dww()
    #定位补丁框架
    wy.dwf('login_frame')
    #点击请求头像
    wy.ss("id","img_out_1505328345").click()
    #选择最新标签页
    wy.dww()
    time.sleep(3)
    #点击写信
    wy.ss("id","composebtn").click()
    time.sleep(4)
    #定位大框架
    wy.dwf('mainFrame')
    time.sleep(1)
    #在收件人输入：2292110190@qq.com
    wy.ss("xpath",'//*[@id="toAreaCtrl"]/div[2]/input').send_keys("2292110190@qq.com")
    #在主题输入：嗯嗯饿呢嗯嗯嗯嗯啊
    wy.ss("xpath",'//*[@id="subject"]').send_keys("嗯嗯饿呢嗯嗯嗯嗯啊")
    time.sleep(3)
    #上传附件：1.txt
    wy.ss("name","UploadFile").send_keys("C:\Ms\\1.txt")
    time.sleep(2)
    #定位正文框架
    wy.dwf(wy.ss("xpath",'//*[@class="qmEditorIfrmEditArea"]'))
    #正文输入：厄内阿斯顿ask多久啊我看等哈我的
    wy.ss("xpath",'/html/body/div').send_keys("厄内阿斯顿ask多久啊我看等哈我的")
    time.sleep(4)
    #回退到上一个框架
    wy.dwpf()
    time.sleep(1)
    #点击发送
    wy.ss("xpath",'//*[@id="toolbar"]/div/a[1]').click()
    time.sleep(3)


