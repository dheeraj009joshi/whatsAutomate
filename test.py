from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import os
import time

# Specify the path to your ChromeDriver executable
driver_path = "python_server\chromedriver.exe"

# Create a Service object with the executable path
chrome_service = ChromeService(executable_path=driver_path)

# Create a new instance of the Chrome webdriver, passing the Service object
driver = webdriver.Chrome(service=chrome_service)
driver.get("http://web.whatsapp.com")
# os.system('notify-send  "-i" call-start "Whatsapp Monitor Start" "Developed By RIZWAN AHMAD(rizwansoaib@gmail.com)"')
name=input("Please Enter Name for search online status: ")

while True:

    try:
        chat=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/button")
        chat.click()
        time.sleep(2)
        search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]")
        # search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div")
        search.click()
        time.sleep(2)
        search.send_keys(name)
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        # open=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[2]/div")
        # open.click()
        time.sleep(2)


        while True:
            try:
                status = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/header/div[2]/div[2]/span").text
                name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[4]/div/header/div[2]/div[1]/div/div/span").text
                # os.system('notify-send  "-i" call-start "Whatsapp Monitor" "{0}  {1} "'.format(name,status))
                # # -v=language en-us, f= 1 to 5 for male m ,s= speed,a= volume
                # os.system('espeak -ven-us+f4 -s140 -a 500 "{0} has {1}  in whatsapp"'.format(name,status))
                print("{0} {1}".format(name,status))
                if status=='online':
                    text="hi bhaiya online kya kr rhe ho ? "
                    mess=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
                    mess.send_keys(text)
                    time.sleep(2)
                    mess.send_keys(Keys.RETURN)
                # time.sleep(55)
            except Exception as e:
                print(e)
                pass


    except Exception as e:
            print(e)
            pass