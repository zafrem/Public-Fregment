import requests
from bs4 import BeautifulSoup


def get_today_stock_data(corr):
    # Step 1: Send a GET request to the website
    url = f"https://www.google.com/search?q={corr}+stock"
    # https://www.whatismybrowser.com/detect/what-is-my-user-agent/
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/131.0.0.0 Safari/537.36"
    header = {"User-Agent": user_agent}
    response = requests.get(url, headers=header)

    # Step 2: Check the response status
    if response.status_code == 200:
        print("Successfully fetched the webpage!")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        exit()

    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.html) #debug code

    # Step 4: Extract specific data
    current = soup.select_one('#knowledge-finance-wholepage__entity-summary > div.aviV4d > g-card-section > div > '
                              'g-card-section > div.wGt0Bc > div.PZPZlf > span:nth-child(1) > span > '
                              'span.IsqQVc.NprOob.wT3VGc')
    changed = soup.select_one('#knowledge-finance-wholepage__entity-summary > div.aviV4d > g-card-section > div > '
                              'g-card-section > div.wGt0Bc > div.PZPZlf > span.WlRRw.IsqQVc.fw-price-up > '
                              'span:nth-child(1)')
    persent = soup.select_one('#knowledge-finance-wholepage__entity-summary > div.aviV4d > g-card-section > div > '
                              'g-card-section > div.wGt0Bc > div.PZPZlf > span.WlRRw.IsqQVc.fw-price-up > span.jBBUv '
                              '> span:nth-child(1)')

    # Step 5: Display the extracted data
    print("Extracted current html tag:", current)
    print("Extracted changed html tag:", changed)
    print("Extracted persent html tag:", persent)

    # Step 6: Save the data to a file (optional)
    from datetime import datetime

    with open("titles.txt", "a+", encoding="utf-8") as file:
        file.write(f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}: {corr} {current.get_text().strip()}" \
            f"({changed.get_text().strip()})\n")
        print("Titles saved to titles.txt")


if __name__ == "__main__":
    get_today_stock_data("Tesla")
