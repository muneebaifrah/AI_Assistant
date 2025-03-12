from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

Link = "https://readloud.net/english/american/29-male-voice-joey.html"
chrome_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument("--headless=new")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)
driver.maximize_window()
driver.get(url=Link)

def WaitForTheWebsiteToLoad():
    sleep(2)
    while True:
        try:
            driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea')
            break

        except:
            pass

def TextToSpeech(Text):
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea').send_keys(Text)
    except:
        pass
    
    sleep(0.5)

    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/span/input').click()
    except:
        pass

    sleep(0.5)

    try:
        driver.find_element(by=By.XPATH,value='//*[@id="dle-content"]/article/div[2]/center/div/form/textarea').clear()
    except:
        pass
    
WaitForTheWebsiteToLoad()