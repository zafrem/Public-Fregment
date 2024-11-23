# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def parsing(string):
    lists = string.split('\n')
    date = lists[0]
    del lists[0]
    times = []
    team1s = []
    team2s = []
    if 'LIVE' == lists[0]:
        times.append(lists[0])
        team1s.append(lists[2] + lists[3] + lists[4])
        team2s.append(lists[5] + lists[6] + lists[7])
    else:
        for i in range(0, len(lists), 9):
            times.append(lists[i])
            team1s.append(lists[i + 2] + lists[i + 3])
            team2s.append(lists[i + 4] + lists[i + 5])
    print("==============================")
    print(date)
    for time, team1, team2 in zip(times, team1s, team2s):
        print(time + ":" + team1 + " vs " + team2)


def get_today_nfl_schedules():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://www.nfl.com/schedules/'
    driver.get(url)

    try:
        elements = driver.find_elements(By.XPATH,
                                        '/html/body/div[3]/main/div/section/div/div')
        for idx, title in enumerate(elements, 1):
            parsing(title.text)

    except Exception as e:
        print(f"Error : {e}")
    driver.quit()


if __name__ == "__main__":
    get_today_nfl_schedules()
