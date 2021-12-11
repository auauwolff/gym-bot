from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')

browser = webdriver.Chrome(options = options)
browser.set_page_load_timeout(30)

browser.get('https://members.gymvue.com.au/training-programs/51')

myemail = "auauwolff@gmail.com"
mypassword = "locomotion"

email = browser.find_element_by_xpath('//*[@id="email"]')
email.send_keys(myemail)

passwrd = browser.find_element_by_xpath('//*[@id="password"]')
passwrd.send_keys(mypassword)

try:
    loginButton = browser.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/form/div[4]/span/button')
    browser.execute_script("arguments[0].click();", loginButton)
except:
    print('unable to log in')

try:
    bookTimeSlots = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[2]')
    browser.execute_script("arguments[0].click();", bookTimeSlots)
except:
    print('filter button error')
      
try:
    filterButton = browser.find_element_by_xpath('//*[@id="program-check-835"]')
    browser.execute_script("arguments[0].click();", filterButton)
except:
    print('filter checkbox error')  
    
time.sleep(2)   

try:
    applyFilterButton = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[4]/div/button[2]')
    browser.execute_script("arguments[0].click();", applyFilterButton)
except:
    print('Apply filter error') 
        
time.sleep(2) 

try:
    selectDate = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[4]')
    browser.execute_script("arguments[0].click();", selectDate)
except:
    print('Date error select')
    
time.sleep(4) 

try:
    selectDate = browser.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[4]')
    browser.execute_script("arguments[0].click();", selectDate)
except:
    print('Date2 error select')
    
time.sleep(4) 

try:
    selectPilates = browser.find_element_by_xpath("//*[contains(text(), '06:30 - 07:30')]")
    browser.execute_script("arguments[0].click();", selectPilates)
except:
    print('Pilates error select class')

try:
    bookyesButton = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[3]/div/div/div/div/div[2]/div/button')
    browser.execute_script("arguments[0].click();", bookyesButton)
except:
    print('Error confirm booking')

time.sleep(2) 

try:
    bookyesButton2 = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]')
    browser.execute_script("arguments[0].click();", bookyesButton2)
except:
    print('Error confirm booking 2')
browser.close()






# =============================================================================
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import os
# import sys
# from datetime import timedelta, date
# 
# 
# def userInfo():
#     myemail = "auauwolff@gmail.com"
#     mypassword = "locomotion"
#     
#     # myemail = "sararkoerich@gmail.com"
#     # mypassword = "every123"
# 
#     email = driver.find_element_by_xpath('//*[@id="email"]')
#     email.send_keys(myemail)
# 
#     passwrd = driver.find_element_by_xpath('//*[@id="password"]')
#     passwrd.send_keys(mypassword)
# 
#     #time.sleep(2)
# 
#     login()
# 
# def login():
#     try:
#         loginButton = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/form/div[4]/span/button')
#         driver.execute_script("arguments[0].click();", loginButton)
#     except:
#         print('unable to log in')
# 
#     #time.sleep(2)
# 
# #     chooseTrain()
# #     #chooseDay()
# 
# # def chooseTrain():
# #     try:
# #         selectTrainButton = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/nav/a[2]')
# #         driver.execute_script("arguments[0].click();", selectTrainButton)
# #     except:
# #         print('unable to select Train')
# #         # driver.quit()
# #         # driver.close()
# #     #time.sleep(2)
# 
# #     try:
# #         selectLocationButton = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/main/div[2]/div/div/div[1]/select/option[2]')
# #         driver.execute_script("arguments[0].click();", selectLocationButton)
#         
# #     except:
# #         print('unable to select Location')
#         # driver.quit()
#         # driver.close()
#     # try:
#     #     selectEMFButton = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/main/div[2]/div/div/div[1]/select/option[11]')
#     #     driver.execute_script("arguments[0].click();", selectEMFButton)
#         
#     # except:
#     #     print('unable to select Train')
#     
# #     selectTime()
# 
# # def chooseDay():
# #     try:
# #         selectDayButton = driver.find_element_by_xpath('//*[@id="btn_date_select"]')
# #         driver.execute_script("arguments[0].click();", selectDayButton)
# #     except:
# #         print('unable to select day')
# #         driver.quit()
# #         driver.close()
# 
# #     try:
# #         dateSelected = date.today() + timedelta(days=2)
# #         dayButton = driver.find_element_by_xpath('//*[@id="date_' + str(dateSelected) + '"]')
# #         driver.execute_script("arguments[0].click();", dayButton)
# #     except:
# #         print('date not there')
# #         driver.quit()
# #         driver.close()
#     
#     selectTime()
# 
# def selectTime():
#     try:
#         bookTimeSlots = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[2]')
#         driver.execute_script("arguments[0].click();", bookTimeSlots)
#     except:
#         print('reformer pilates error')
#         # driver.quit()
#         # driver.close()
#     try:
#         filterButton = driver.find_element_by_xpath('//*[@id="program-check-835"]')
#         driver.execute_script("arguments[0].click();", filterButton)
#     except:
#         print('filter error')  
#     
#     time.sleep(2)   
#     try:
#         applyFilterButton = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[4]/div/button[2]')
#         driver.execute_script("arguments[0].click();", applyFilterButton)
#     except:
#         print('Apply filter error') 
#         
#     time.sleep(2) 
#     selectClass()
#     
# def selectClass():
#     try:
#         selectDate = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[4]')
#         driver.execute_script("arguments[0].click();", selectDate)
#     except:
#         print('Date error select')
#     time.sleep(2) 
#     try:
#         selectDate = driver.find_element_by_xpath('//*[@id="calendar"]/div[1]/div[2]/div/button[4]')
#         driver.execute_script("arguments[0].click();", selectDate)
#     except:
#         print('Date2 error select')
#     time.sleep(4) 
#     try:
#         selectPilates = driver.find_element_by_xpath("//*[contains(text(), '06:30 - 07:30')]")
#         driver.execute_script("arguments[0].click();", selectPilates)
#     except:
#         print('Pilates error select')
#     
# #"//*[contains(text(), '06:30 - 07:30')]"
#     confirmBooking()
# 
# def confirmBooking():
#     try:
#         bookyesButton = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[3]/div/div/div/div/div[2]/div/button')
#         driver.execute_script("arguments[0].click();", bookyesButton)
#     except:
#         print('Error confirm booking')
#     time.sleep(2) 
#     try:
#         bookyesButton2 = driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]')
#         driver.execute_script("arguments[0].click();", bookyesButton2)
#     except:
#         print('Error confirm booking 2')
# 
# if __name__ == '__main__':
#     # Load chrome
#     driver = webdriver.Chrome()
#     driver.get("https://members.gymvue.com.au/training-programs/51")
#     #driver.get("https://members.gymvue.com.au/")
# 
#    # time.sleep(2)
# 
#     userInfo()
#     # driver.quit()
#     # driver.close()
# 
# 
# =============================================================================
