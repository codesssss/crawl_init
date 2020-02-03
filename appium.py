from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pymongo#数据库
platform= 'Android'
deviceName='SM_G9650'#改成自己手机型号
app_package='com.tencent.mm'
app_activity='.ui.LauncherUI'
driver_server='http://127.0.0.1:4723/wd/hub'

class WeChatCrawl():
    def __init__(self):
        self.desired_caps={
        'platformName':platform,
        'deviceName':deviceName,
        'appPackage':app_package,
        'appActivity':app_activity}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)
        self.client=pymongo.MongoClient()
        self.db=self.client.weixin
        #创建叫weixin的数据库
        self.collection=self.db.weixin
        #定义集合

    def login(self):
        #登录过程
        print('点击登陆按钮——————')
        login=self.wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/d75')))
        login.click()
        #输入手机号
        phone=self.wait.until(EC.presence_of_element_located((By.ID,    'com.tencent.mm:id/hz')))
        phone_num=input('请输入手机号：')
        phone.send_keys(phone_num)
        print('点击下一步中')
        button=self.wait.until(EC.presence_of_element_located((By.ID,       'com.tencent.mm:id/alr')))
        button.click()
        psw=input('请输入密码：')
        password=self.wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/hz')))
        password.send_keys(psw)
        login=self.driver.find_element_by_id('com.tencent.mm:id/alr')
        login.click()
        #关闭提示
        tip=self.wait.until(EC.element_to_be_clickable((By.ID,'com.tencent.mm:id/an2')))
        tip.click()

    def enter(self):
        #进行爬取前的杂项处理
        print('点击发现——————————')
        tab=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@resource-id="com.tencent.mm:id/cdh"]/..')))
        print('已经找到发现按钮')
        time.sleep(6)
        tab.click()
        print('点击朋友圈')
        friends=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@resource-id="android:id/list"]/*[@class="android.widget.LinearLayout"][1]')))
        friends.click()

    def crawl(self):
        #进入朋友圈并开始爬取
        while True:
            items=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@resource-id="com.tencent.mm:id/dja"]//*[@class="android.widget.FrameLayout"]')))
            self.driver.swipe(300,1000,300,300)
            #模拟手上滑过程
            for item in items:
                try:
                    nickname=item.find_element_by_id('com.tencent.mm:id/as6').get_attribute('text')
                    print(nickname)
                    content=item.find_element_by_id('com.tencent.mm:id/dkf').get_attribute('text')
                    print(content)
                    data={'nickname':nickname,
                    'content':content}
                    self.collection.update({'nickname':nickname,'content':content},{'$set':data},True)
                    #更新数据库，根据昵称和正文来查询，如果信息不存在，则插入数据，否则更新数据，关键点是第三个参数True，这可以实现存在即更新，不存在即插入的代码
                except:
                    pass
    def main(self):
        self.login()
        self.enter()
        self.crawl()

crawl=WeChatCrawl()
crawl.main()