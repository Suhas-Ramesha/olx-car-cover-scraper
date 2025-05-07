from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.olx.in/items/q-car-cover"
driver.get(url)
time.sleep(5)  

titles, prices, locations, links = [], [], [], []

items = driver.find_elements(By.CSS_SELECTOR, 'li.EIR5N')
for item in items:
    try:
        title = item.find_element(By.TAG_NAME, 'span').text
        price = item.find_element(By.CLASS_NAME, '_89yzn').text
        location = item.find_element(By.CLASS_NAME, 'tjgMj').text
        link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
        
        titles.append(title)
        prices.append(price)
        locations.append(location)
        links.append(link)
    except:
        continue

driver.quit()

df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Location": locations,
    "Link": links
})
df.to_csv("olx_car_covers.csv", index=False)
print("Search results saved to olx_car_covers.csv")
