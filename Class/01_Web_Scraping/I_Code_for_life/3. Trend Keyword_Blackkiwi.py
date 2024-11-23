# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_keyword():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://blackkiwi.net/service/trend'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            # First element
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div[1]/main/div/div[2]/div[1]/div/div[2]/div/div[2]/div['
                                            '1]/div[1]/span[2]/span/a'))
        )

        elements = driver.find_elements(By.XPATH,
                                        '/html/body/div[1]/main/div/div[2]/div[1]/div/div['
                                        '2]/div/div/div/div/span/span/a')
        for idx, title in enumerate(elements, 1):
            print(f"{idx}. {title.text}")

    except Exception as e:
        print(f"Error: {e}")

    driver.quit()


if __name__ == "__main__":
    get_keyword()
