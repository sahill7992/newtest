from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the Chrome driver
driver = webdriver.Edge()

#
driver.get("https://www.helperplace.com")
driver.implicitly_wait(5)

#click on login button
try:
    search_input_field = driver.find_element(By.CLASS_NAME, "popup-button-login")
    search_input_field.click()
    driver.implicitly_wait(5)
    time.sleep(1)

    #input mailid
    search_input_field = driver.find_element(By.XPATH, "//*[@id='pills-home']/div[1]/div[1]/input[1]")
    search_input_field.click()
    search_input_field.clear()
    search_input_field.send_keys("ramukaka@gmail.com")
    time.sleep(1)

    #input password
    search_input_field = driver.find_element(By.XPATH, "//*[@id='pills-home']/div[1]/div[2]/input[1]")
    search_input_field.click()
    search_input_field.clear()
    search_input_field.send_keys("ramukak1a@123gmail.com")
    search_input_field.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.implicitly_wait(5)
    #cancel notification
    search_input_field = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")
    search_input_field.click()
    time.sleep(1)


except:
    print("inside except")
    # search_input_field = driver.find_element(By.CLASS_NAME, "popup-button-login")
    # driver.implicitly_wait(5)
    # time.sleep(1)

    #input mailid
    search_input_field = driver.find_element(By.XPATH, "//*[@id='pills-home']/div[1]/div[1]/input[1]")
    search_input_field.click()
    search_input_field.clear()
    search_input_field.send_keys("ramukaka@gmail.com")
    time.sleep(4)

    #input password
    search_input_field = driver.find_element(By.XPATH, "//*[@id='pills-home']/div[1]/div[2]/input[1]")
    search_input_field.click()
    search_input_field.clear()
    search_input_field.send_keys("ramukaka@123gmail.com")
    search_input_field.send_keys(Keys.RETURN)
    time.sleep(4)
    driver.implicitly_wait(5)

#cancel notification
search_input_field = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")
search_input_field.click()
time.sleep(1)

#click on find job
search_input_field = driver.find_element(By.CLASS_NAME, "custom-job-action-detail")
search_input_field.click()
time.sleep(3)

# click on job location and select hongkong 
search_input_field = driver.find_element(By.XPATH, "//body/section[1]/app-root[1]/app-jobfind[1]/section[1]/div[1]/div[3]/div[1]/app-filter[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ng-multiselect-dropdown[1]/div[1]/div[1]/span[1]")
search_input_field.click()
time.sleep(1)
search_input_field = driver.find_element(By.XPATH, "//body/section[1]/app-root[1]/app-jobfind[1]/section[1]/div[1]/div[3]/div[1]/app-filter[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ng-multiselect-dropdown[1]/div[1]/div[2]/ul[2]/li[1]/div[1]")
search_input_field.click()
search_input_field = driver.find_element(By.XPATH, "//body/section[1]/app-root[1]/app-jobfind[1]/section[1]/div[1]/div[3]/div[1]/app-filter[1]/div[1]/div[1]/div[1]/div[1]/div[3]/ng-multiselect-dropdown[1]/div[1]/div[1]/span[1]")
search_input_field.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

#select job postion as driver
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[4]/div/div[2]/label/input")
search_input_field.click()
time.sleep(1)

# select job type full time
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[6]/div/div[1]/label/input")
search_input_field.click()
time.sleep(1)

#contract status
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[7]/ng-multiselect-dropdown/div/div[1]/span")
search_input_field.click()
time.sleep(1)
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[7]/ng-multiselect-dropdown/div/div[2]/ul[2]/li[1]/div")
search_input_field.click()
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[7]/ng-multiselect-dropdown/div/div[1]/span")
search_input_field.click()
time.sleep(1)

#post by
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[8]/div/div/label[1]/input")
search_input_field.click()
time.sleep(3)

#language
search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[9]/div[1]/ng-multiselect-dropdown/div/div[1]/span")
search_input_field.click()
time.sleep(1)
search_input_field = driver.find_element(By.XPATH," /html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[9]/div[1]/ng-multiselect-dropdown/div/div[2]/ul[2]/li[1]/div")

search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[1]/app-filter/div/div/div/div/div[9]/div[1]/ng-multiselect-dropdown/div/div[1]/span")
search_input_field.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")



search_input_field = driver.find_element(By.XPATH, "/html/body/section/app-root/app-jobfind/section/div/div[3]/div[2]/div/div/div[1]/div[5]/job-detail-block/div/div[2]/a")
search_input_field.click()
time.sleep(10)


