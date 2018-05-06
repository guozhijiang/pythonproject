#coding:utf-8

from selenium import webdriver
from time import sleep

def vote(username,password='123456',count=5):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://train.51taoshi.com/vote/fore/index.action')
    driver.find_element_by_xpath('//*[text()="优秀研修组织单位"]/../div[2]/button').click()
    # 投票
    driver.find_element_by_xpath('//*[text()="宜昌市三峡高级中学"]/../../div/div/div[2]/button').click()
    driver.find_element_by_id('login_temp').click()
    driver.find_element_by_id('login_username').send_keys(username)
    driver.find_element_by_id('login_password').send_keys(password)
    # 登录
    driver.find_element_by_xpath('//*[@id="login_sb"]/input').click()
    sleep(2)
    # 投票
    for i in range(0,count):
        print('vote for '+str(i+1)+' times')
        driver.find_element_by_xpath('//*[text()="宜昌市三峡高级中学"]/../../div/div/div[2]/button').click()
        sleep(1)

def getUserList():
    with open('./user.txt', 'r') as f:
        userList=[]
        for user in f.readlines():
            # print(user.strip('\n'))
            userList.append(user.strip('\n'))
        return userList

if __name__=='__main__':
    for user in getUserList():
        try:
            print(user+' vote ')
            vote(user)
            sleep(1)
        except Exception as e:
            print(e.message)





