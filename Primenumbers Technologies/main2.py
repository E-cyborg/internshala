from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Set up Selenium (you can use ChromeDriver or any browser driver)
driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
driver.get("https://rera.odisha.gov.in/projects/project-list")

time.sleep(5)

# Get the rendered HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Now try to find <app-project-card> elements
for card in soup.find_all('app-project-card'):
    print(card.prettify())

with open("full_page.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())


