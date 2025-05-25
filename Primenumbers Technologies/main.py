from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()



for x in range(5):
    # loading the webpage
    driver.get("https://rera.odisha.gov.in/projects/project-list")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn.btn-primary")))

    # getting all the view buttons
    view_buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn.btn-primary")

    # Scrolling the page to find the view so it can be click
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_buttons[x])
    time.sleep(1) #waiting to load the page
    view_buttons[x].click() #clicking the view button
    time.sleep(1)

    # getting the div that stores the data of project 
    div_element = driver.find_element(By.CLASS_NAME, "card-body")
    driver.execute_script("arguments[0].scrollIntoView();", div_element)
    time.sleep(1)  

    html_inside_div = div_element.get_attribute("innerHTML")
    soup = BeautifulSoup(html_inside_div, "html.parser")
    tags = soup.find_all(["strong", "label"])

    tag_data = [tag.text.strip() for tag in tags]

    # storing the data in dict
    dict={}
    for x in range(0,int((len(tag_data)/2)+1),2):
        dict[tag_data[x]] = tag_data[x+1]

    # nav to second section
    driver.refresh()
    Promoter_Details = driver.find_element(By.ID,"ngb-nav-1")
    Promoter_Details.click()


    div_element = driver.find_element(By.CLASS_NAME, "card-body")
    driver.execute_script("arguments[0].scrollIntoView();", div_element)
    time.sleep(1)  

    html_inside_div = div_element.get_attribute("innerHTML")
    soup = BeautifulSoup(html_inside_div, "html.parser")
    tags = soup.find_all(["strong", "label"])

    tag_data = [tag.text.strip() for tag in tags]
    for x in range(0,int((len(tag_data)/2)+1),2):
        dict[tag_data[x]] = tag_data[x+1]

    print(dict)

    # will run only 5 time 


time.sleep(2)
driver.quit()
