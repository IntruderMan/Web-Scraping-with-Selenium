from email.headerregistry import Address
from unicodedata import name
import pandas as pd

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#location of crome_driver file (its work for automation)
driver = webdriver.Chrome(executable_path="/home/zec/ZecData/Selenium/chromedriver_linux64/chromedriver")

# Open “Google” in the browser.
driver.get("https://www.google.com/")

# search “Programming Coaching in Indore”. And then search it by Click or Enter button.
driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("programming coaching in indore", Keys.ENTER)
# driver.implicitly_wait(1) '''wait in seconds'''

# And then maximize it
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"wUrVib").click()
sleep(1)

# create lists for inserting data.
l1 = []
l2 = []
l3 = []
Names = []
Addresss = []
Phone = []

# Pagination
# Go to next page by clicking
k = 0
while True:
    if k == 0:
        pass
    elif k == 5:          #Type stoping page number and program will stop
        break
    else:
        driver.find_element(By.ID, "pnnext").click()
        sleep(1)
    sleep(1)
    master = driver.find_elements(By.CLASS_NAME,"VkpGBb")
    for i in master:
        a = i.find_elements(By.TAG_NAME, "a")
        Title = i.find_element(By.CLASS_NAME, "dbg0pd").text
        l1.append(Title)                                                   #insert Title in list l1
        try:    
            Website = a[1].get_attribute("href")
            l2.append(Website)                                             #insert Website in list l1
        except:
            l2.append(None)                                                #insert null value when Website is not present

        google = "https://www.google.com/"                                 #create new variable for add google link in the address
        try:
            location = google+(a[2].get_attribute("data-url"))
            l3.append(location)                                            #insert location with google link
        except:
            l3.append(0)                                                   #insert null value when location is not available

        # After that Click on the Title name for open a popup
        i.find_element(By.TAG_NAME, "a").click()
        sleep(1)
        
        # Find the text of title, address and phone number from popup bar
        Title2 = driver.find_element(By.CLASS_NAME, "kno-ecr-pt").text
        Names.append(Title2)                                               #Insert Title name in the list of Names
    
        try:
            add2 = driver.find_element(By.CLASS_NAME,"LrzXr").text
            Addresss.append(add2)                                          #Insert Address in the list of Addresss
        except:
            Addresss.append(None)                                          #Insert None value in list of Addresss when no data there
            print("address is none")
    
        try:
            phn = driver.find_element(By.CLASS_NAME,"kno-fv").text
            Phone.append(phn)                                              #Insert Phone Number in the list of Phone
        except:
            Phone.append(None)                                             #Insert None value in list of Addresss when no data there
    k+=1

print(len(l1))
print(len(l2))
print(len(l3))
print(len(Names))
print(len(Addresss))
print(len(Phone))


# insert these all data in a csv file.
df=pd.DataFrame({'Title Name':l1,'Website':l2,'Direction':l3,'Title':Names,'Address':Addresss,'Phone Number':Phone})             #create column name for dataframe and insert list there
df.to_csv('Task3.csv', encoding = 'utf-8-sig', index = False)                             #convert dataframe into csv file 


