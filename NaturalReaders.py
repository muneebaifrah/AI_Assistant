from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

Link = "https://www.naturalreaders.com/online/"
chrome_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=Link)
ButtonOneXpath = '//*[@id="pw-voice-page"]/div[3]/button'
ButtonTwoXpath = '//*[@id="switch-pw-card"]/a'
ButtonThreeXpath = '//*[@id="pw-reading-scroll"]/div[1]/button'

Voice2Xpath = '//*[@id="v_66_ms"]'
Voice3Xpath = '//*[@id="v_73_ms"]'
Voice4Xpath = '//*[@id="v_63_ms"]'
NextPageXpath = '//*[@id="voice-next"]'
JasonXpath = '//*[@id="v_72_ms"]'
AndrewXpath = '//*[@id="v_120_ms"]'

def WebsiteStart():
    sleep(3)

    try:
        driver.find_element(by=By.XPATH,value=NextPageXpath).click()

    except:
        pass

    sleep(1)

    try:
        driver.find_element(by=By.XPATH,value=AndrewXpath).click()

    except:
        pass

    sleep(1)

    try:
        driver.find_element(by=By.XPATH,value=ButtonOneXpath).click()

    except:
        pass

    sleep(1.5)
    try:
        driver.find_element(by=By.XPATH,value=ButtonTwoXpath).click()

    except:
        pass

    sleep(3)

    try:
        driver.find_element(by=By.XPATH,value=ButtonThreeXpath).click()

    except:
        pass

WebsiteStart()

TextAreaXpath = '//*[@id="inputDiv"]'
StartVoiceXpath = '//*[@id="pw-reading-page"]/div[1]/div/div[2]/app-pw-reading-bar/div/div/button[3]'

def TextToSpeech(Text):
    try:
        driver.find_element(by=By.XPATH,value=TextAreaXpath).clear()

    except:
        pass

    try:
        driver.find_element(by=By.XPATH,value=TextAreaXpath).send_keys(Text)

    except:
        pass

    sleep(0.5)

    try:
        driver.find_element(by=By.XPATH,value=StartVoiceXpath).click()

    except:
        pass

while True:
    TextToSpeech(input("Enter TTS : "))