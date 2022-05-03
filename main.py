from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

sisLink = "https://sis.jhu.edu/sswf/"

email = "zjoven1@jh.edu"
password = "" # insert real password

driver = webdriver.Chrome()
driver.maximize_window()

def init():
    driver.get(sisLink)
    time.sleep(1)

    signIn = driver.find_element_by_id("linkSignIn")
    signIn.click()
    time.sleep(3)

def authenticate():
    emailField = driver.find_element_by_id("i0116")
    emailField.send_keys(email)
    emailField.send_keys(Keys.RETURN)

    time.sleep(5)
    passField = driver.find_element_by_id("i0118")
    passField.send_keys(password)
    passField.send_keys(Keys.RETURN)
    time.sleep(5)

def openCart():
    clipboard = driver.find_element_by_xpath("//*[@id='sidebar-menu']/ul/li[1]/a")
    clipboard.click()
    time.sleep(1)

    cart = driver.find_element_by_xpath("//*[@id='sidebar-menu']/ul/li[1]/ul/li[3]/a")    
    cart.click()
    time.sleep(3)

def register():
    selectAll = driver.find_element_by_id("SelectAllCheckBox")
    selectAll.click()
    time.sleep(3)

def submit():
    enroll = driver.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")
    enroll.click()

def waitUntilTime(hours, minutes):
    while(True):
        currentTime = time.localtime()
        currentHour = currentTime.tm_hour
        currentMinute = currentTime.tm_min

        if(currentHour >= hours and currentMinute >= minutes):
            return
        else:
            time.sleep(1)

def main():
    waitUntilTime(6, 58)

    init()
    authenticate()
    openCart()
    register()

    waitUntilTime(7, 0)
    submit()

    return

main()