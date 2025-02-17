#Created by: Yeferson Chacon


#Used selenium to automate the process of ordering a sub from Publix since it works with Python.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#Imported time since I wanted the app to wait for a few seconds in order to refresh

import time

anita_path = "/opt/homebrew/bin/chromedriver"

service = Service(anita_path)
web_driver = webdriver.Chrome(service=service)
web_driver.get("https://www.publix.com/mc/order-ahead/order-deli-online")
time.sleep(6)
wait_time = WebDriverWait(web_driver, 10)

#Now we will select location

#sub_select = wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="geolocation-button"]/span[2]')))
#sub_select.click()
#print("Location selected")
sub_close = wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar-close-button"]/span')))
sub_close.click()
print("Location Closed!!👀")
#time.sleep(5)

sub_choose = wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div/button[1]/span')))
sub_choose.click()
print("Customized Order Selected!😀")
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

sub_bacon = wait_time.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[4]/div[2]/div[1]/label')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_bacon)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[4]/div[2]/div[1]/label')))
sub_bacon.click()
print("Bacon Selected!👹")

sub_lettuce = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[1]/label')))   
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_lettuce)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[1]/label')))
sub_lettuce.click()
print("Lettuce Unselected!🤡")

sub_tomato = wait_time.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[2]/label')))  
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_tomato)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[5]/div[2]/div[2]/label')))
sub_tomato.click()
print("Tomato Unselected!💀")

sub_mayo = wait_time.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[1]/label')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_mayo)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[1]/label')))
sub_mayo.click()
print("Mayo Selected!👽")

sub_ranch = wait_time.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[9]'))) 
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_ranch)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[9]')))
sub_ranch.click()
print("Ranch Selected!👻")

sub_ranch_extra = wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[9]/div/fieldset/div[3]/div/button/span[2]')))
sub_ranch_extra.click()
print("Extra Ranch Selected!👾"
      )
sub_bbq = wait_time.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/div/div/div[1]/div[2]/fieldset[6]/div[2]/div[11]/label')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_bbq)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div[1]/div[2]/fieldset[7]/div[2]/div[2]/label/div[2]')))
sub_bbq.click()
print("BBQ Selected!👾")

sub_toast = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div[1]/div[2]/fieldset[7]/div[2]/div[2]/label')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_toast)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[2]/div/div/div[1]/div[2]/fieldset[7]/div[2]/div[2]/label')))
sub_toast.click()
print("Toasted Selected!👺")

sub_add = wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="builder-add-to-order-btn-sticky"]/span')))
sub_add.click()
print("Added to Order!👿")

order_review = wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/button/span')))
order_review.click()
print("Order Review Selected!🫂")

order_confirm = wait_time.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmation-btn"]/span[2]')))
order_confirm.click()
print("Order Confirmed!👏")

order_checkout = wait_time.until(EC.element_to_be_clickable((By.XPATH, '//html/body/div[1]/section/div[2]/div/div[2]/div/div/div/div[3]/button/span')))
order_checkout.click()
print("Order Checkout!👍")

pickup_firstname = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[1]/div[1]/div/input')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_firstname)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[1]/div[1]/div/input')))
pickup_firstname.click()
pickup_firstname.send_keys("Yeferson")
print("First Name Entered!👌")

pickup_lastname = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[2]/div[1]/div/input')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_lastname)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[2]/div[1]/div/input')))
pickup_firstname.click()
pickup_lastname.send_keys("Chacon")
print("Last Name Entered!👍")

pickup_phone = wait_time.until(EC.presence_of_element_located((By.XPATH, '//html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[3]/div[1]/div/input')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_phone)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[3]/div[1]/div/input')))
pickup_phone.click()
pickup_phone.send_keys("8133819002")
print("Phone Number Entered!👍")

pickup_email = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[4]/div[1]/div/input')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pickup_email)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[2]/div[4]/div[1]/div/input')))
pickup_email.click()
pickup_email.send_keys("yefchac1@gmail.com")
print("Email Entered!👍")

next_pick = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[3]/button/span[2]')))
web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_pick)
wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[4]/div[2]/form/div[3]/button/span[2]')))
next_pick.click()
print("Next Selected!👍")

time_pick = wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[5]/div[2]/form/div[3]/div/button/span[1]')))
print("Time Selected!👍")

#pay_now = wait_time.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[6]/div[2]/form/div[3]/button/span[2]')))
#web_driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pay_now)
#wait_time.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/div[1]/div[6]/div[2]/form/div[3]/button/span[2]')))
#print("Pay Now Selected!👍")

web_driver.quit()