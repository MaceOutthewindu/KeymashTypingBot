import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

userName = input("Input your windows username:")
gameIndex = 0
randomNumber = 1
characters = "abcdefghijklmnopqrstuvwxyz"

link = input("Enter Link:")

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("user-data-dir=C:\\Users\\" + str(userName) + "\\AppData\\Local\\Google\\Chrome\\User Data")
'''browser = webdriver.Chrome(executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe',
                           chrome_options=option)'''
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)


try:
    browser.get(link)
except:
    print("Link Is Not Valid")


def main():
    global gameIndex
    gameIndex += 1
    print("Game " + str(gameIndex))
    fullText = ""
    time.sleep(1)
    hehe = browser.find_elements(By.TAG_NAME, 'button')
    for t in hehe:
        if t.text == "PLAY NOW":
            t.click()
            break

    time.sleep(11)
    html = browser.page_source
    soup = BeautifulSoup(html, features="html.parser")

    for s in soup.find_all("span", class_="text-gray-400"):
        fullText += s.text

    time.sleep(1)
    searchBar = browser.find_element(By.CSS_SELECTOR, "input.border-orange-400")
    for f in fullText:
        numberOfMisspels = random.randint(1, 3)
        randomNumber = random.randint(0, random.randint(10, 20))
        if randomNumber != 1:
            searchBar.send_keys(f)
        else:
            for j in range(numberOfMisspels):
                searchBar.send_keys(characters[random.randint(0, 25)])
            time.sleep(0.08)
            for k in range(numberOfMisspels):
                searchBar.send_keys(Keys.BACKSPACE)
                time.sleep(0.08)
            searchBar.send_keys(f)
        time.sleep(random.randint(8, 10) / 100)
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "red").click()
    if random.randint(0, 6) == 1:
        time.sleep(random.randint(10, 30))


while True:
    main()
