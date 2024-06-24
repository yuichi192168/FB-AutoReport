from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set Chrome options
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Specify the correct path to the ChromeDriver executable
chrome_driver_path = "/data/data/com.termux/files/home/FB-AutoReport/chromedriver.exe"  # Update this with your actual path

# Ensure that the ChromeDriver path is correct and the file exists
driver_service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Continue with your script...

driver.get("https://www.facebook.com/")

time.sleep(4)
driver.find_element_by_id("email").send_keys('kafka2@exdonuts.com')  # replace with your email or phone number
time.sleep(2)
driver.find_element_by_id("pass").send_keys('kafka192168')  # replace with your password
time.sleep(2)
driver.find_element_by_name("login").click()
time.sleep(4)
driver.get('https://www.facebook.com/profile.php?id=100088598930447')  # replace with account URL or the account you want to report
time.sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div/div[1]').click()  # three dots
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]').click()  # find or report
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # report option
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div/div/span').click()  # me
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[4]/div/div').click()  # submit
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div').click()  # next button
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div/div/div/div').click()  # done
time.sleep(30)

driver.quit()
