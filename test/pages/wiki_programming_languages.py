import re
import xml.etree.ElementTree as ET
from selenium.webdriver.common.by import By


from test.data_models.website import Website

table_xpath = "//table[caption[contains(text(), 'Programming languages used in most popular websites*')]]/tbody"


def get_websites(driver):
    websites = []

    table = driver.find_element(By.XPATH, table_xpath)

    for row in table.find_elements(By.XPATH, "./tr"):
        if len(row.find_elements(By.XPATH, "./td")) > 0:
            name = row.find_elements(By.XPATH, "./td")[0].find_element(By.XPATH, "./a").text
            popularity = int(re.sub('[^0-9]', '', row.find_elements(By.XPATH, "./td")[1].text))
            front_end = re.sub("(\[\d*\])", "", row.find_elements(By.XPATH, "./td")[2].text)
            back_end = re.sub("(\[\d*\])", "", row.find_elements(By.XPATH, "./td")[3].text)

            website = Website(name, popularity, front_end, back_end)
            websites.append(website)
    return websites
