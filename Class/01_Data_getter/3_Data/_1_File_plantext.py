import _0_Coin_Data_getter as coin_data
from datetime import datetime
import time


def save_data_text(filename, price, change_value):
    with open(filename, "a+", encoding="utf-8") as file:
        file.write(
            f"""{datetime.today().strftime("%Y-%m-%d %H:%M:%S")}|{price}|{change_value}\n""")


def load_data_text(filename):
    with open(filename, "r", encoding="utf-8") as read_file:
        while True:
            for lines in read_file.readlines():
                if not lines: break
                row = lines.rstrip("\n").split("|")
                print(f"Date : {row[0]}, Price : {row[1]}, Change Value : {row[2]}")
            print("\n")
            read_file.close()
            break
        read_file.close()


if __name__ == "__main__":
    while True:
        time.sleep(60 * 60 * 24)  # Daily
        coin_name = "bitcoin"
        current_info, change_point = coin_data.get_today_stock_data(coin_name)
        save_data_text(f"{coin_name}_info.txt", current_info, change_point)
        load_data_text(f"{coin_name}_info.txt")
