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
    # options.add_argument('headless')
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.premierleague.com/'
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            # Wait loading element
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[5]/div/nav/div[2]/div[1]/div/a/time')),
        )
        elements = driver.find_elements(By.XPATH,
                                        '/html/body/main/div[5]/div/nav/div[2]/div[1]/div')
        for idx, title in enumerate(elements, 1):
            date = title.text.split('\n')
            times = driver.find_elements(By.XPATH,
                                        f'/html/body/main/div[5]/div/nav/div[2]/div[1]/div[{idx}]/a/time')
            team1s = driver.find_elements(By.XPATH,
                                         f'/html/body/main/div[5]/div/nav/div[2]/div[1]/div[{idx}]/a/div[1]/span[1]')
            team2s = driver.find_elements(By.XPATH,
                                         f'/html/body/main/div[5]/div/nav/div[2]/div[1]/div[{idx}]/a/div[2]/span[2]')
            for time, team1, team2 in zip(times, team1s, team2s):
                print(f"{idx}. {date[0]} \t {time.text} : {team1.text} vs {team2.text}")

    except Exception as e:
        print(f"Error : {e}")

    driver.quit()

if __name__ == "__main__":
    get_keyword()
