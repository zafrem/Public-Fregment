# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_keyword():
    import time
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.premierleague.com/'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            # Wait loading element
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div/section/div[1]/div[3]/div[1]/div[1]/time'))
        )
        time.sleep(5)
        elements = driver.find_elements(By.XPATH,
                                        '/html/body/main/div/section/div[1]/div[3]/div[1]/div/time')

        for idx, title in enumerate(elements, 1):
            #print(idx, title.text)
            scores = driver.find_elements(By.XPATH,
                                         f'/html/body/main/div/section/div[1]/div[3]/div[1]/div[{str(idx)}]/a/span')
            upcoming = driver.find_elements(By.XPATH,
                                         f'/html/body/main/div/section/div[1]/div[3]/div[1]/div[{str(idx)}]/a/time')
            times = scores + upcoming
            team1s = driver.find_elements(By.XPATH,
                                         f'/html/body/main/div/section/div[1]/div[3]/div[1]/div[{str(idx)}]/a/div[1]')
            team2s = driver.find_elements(By.XPATH,
                                          f'/html/body/main/div/section/div[1]/div[3]/div[1]/div[{str(idx)}]/a/div[2]')
            for _time, _team1, _team2 in zip(times, team1s, team2s):
                _temp = _time.text.replace('\n', '')
                print(f"""{title.text} \t {_temp}: {_team1.text} vs {_team2.text}""")

    except Exception as e:
        print(f"Error : {e}")

    driver.quit()


if __name__ == "__main__":
    get_keyword()
