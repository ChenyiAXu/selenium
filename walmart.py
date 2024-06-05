from selenium import webdriver
import time

def get_page_title(url):
    try:
        cService = webdriver.ChromeService(executable_path='C:\\Program Files (x86)\\chromedriver.exe')
        driver = webdriver.Chrome(service=cService)
        driver.get(url)
        print(driver.title)   
        # Wait indefinitely
        input("Press Enter to quit...")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()


get_page_title("https://www.walmart.ca/en")

