import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
 
# linkedin post liker
#
# Add your post url (if any) to your posts here for others to like them : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
#
#
#
# To like other people's post:
# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb
 
# step 1 change this from : https://docs.google.com/document/d/1YiPKlYkzGMO08HfpZuOZ-S4B-t6KrA7-Xe1x1ElFmnk/edit?usp=sharing
#step 2 : run code , check if you are logged in (if not, then login) then press 1 in console
#step 3 : the code shoud take care of the rest add your posts that you would want to get liked
 
 
 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
 
driver.get("https://linkedin.com")
# delete this after every month
 
while "1" != input("press 1 when signed in: "):
    pass

driver.get("https://www.linkedin.com/mynetwork/")

sleep(4)

buttons = driver.find_elements_by_class_name("invitation-card__action-btn")

sleep(2)       
for button in buttons:
    word= button.get_attribute("aria-label").split(" ")[0]
    
    if(word == "Accept"):
        print("Accepting request...")
        button.click()
        print("Accepted")
        sleep(2)

 
driver.close()