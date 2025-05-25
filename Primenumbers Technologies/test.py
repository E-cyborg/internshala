from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://rera.odisha.gov.in/projects/project-list")

# Wait for the 'View Details' buttons to be present
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn.btn-primary"))
)

# Get all "View Details" buttons
view_buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn.btn-primary")

print(f"Found {len(view_buttons)} 'View Details' buttons.")
try:
    if view_buttons:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_buttons[0])
        time.sleep(1)  # let scroll settle
        view_buttons[0].click()
        time.sleep(5)
        pro_details = driver.find_element(By.ID,"ngb-nav-1")
        pro_details.click()
        

except Exception as e:
    print('error',e)
print(view_buttons)


# Optional: wait and close
time.sleep(10)
driver.quit()





# accessing the webpage 
# going to the each page one by one and savin the data one by one
# swal2-confirm swal2-styled



# click on ok 
# check if the button is present or not 

# !-----!---------!_!_!
# element = driver.find_element(By.CLASS_NAME, "swal2-confirm swal2-styled")

# if element:
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm swal2-styled")))


# this is hw the view button looks
# <selenium.webdriver.remote.webelement.WebElement (session="d391992b6fc4fec96f0a716c103b3010", element="f.8CBE2A8A5BAAC7826A5FE01197FD41D7.d.DD4B61BD948AD7F2D181BFD931BE979B.e.160")>