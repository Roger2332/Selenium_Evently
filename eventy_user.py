import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

load_dotenv()


driver_path = r'C:\TestFiles\chromedriver.exe'


service = Service(driver_path)

driver = webdriver.Chrome(service=service)

try:


    driver.get('http://localhost:8000/')


    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'login-button'))
    )
    login_button.click()


    create = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/createuser/"]'))
    )
    create.click()


    file_path = 'Uzytkownicy.json'
    with open(file_path, 'r', encoding='utf-8') as json_file:
        dane_list = json.load(json_file)
    for data in dane_list:


        first_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'first_name'))
        )
        first_name.clear()
        first_name.send_keys(data['First_name'])

        last_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'last_name'))
        )
        last_name.clear()
        last_name.send_keys(data['Last_name'])

        username = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'username'))
        )
        username.clear()
        username.send_keys(data['Username'])

        email = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'email'))
        )
        email.clear()
        email.send_keys(data['Email'])

        password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password1'))
        )
        password.clear()
        password.send_keys(data['Password'])


        password = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password2'))
        )
        password.clear()
        password.send_keys(data['Password'])

        submit = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))
        )
        submit.click()
        create = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/createuser/"]'))
        )
        create.click()

finally:
    time.sleep(10)
    driver.quit()
