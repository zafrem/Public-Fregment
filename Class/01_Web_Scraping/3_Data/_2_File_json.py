import _0_Coin as coin_data
import json
from datetime import datetime
import time


def init_json_file(coin_name, filename):
    data = {
    }
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # indent=4 makes the JSON readable
    print(f"Data init successfully to {filename}.")


def load_data_json(filename):
    try:
        with open(filename, 'r') as file:
            loaded_data = json.load(file)
            return loaded_data
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty dictionary.")
        return {}


def save_data_json(filename, coin_name, price, change_value):
    data = load_data_json(filename)
    print(data)
    add_data = {datetime.today().strftime("%Y-%m-%d %H:%M:%S") : f"{price} ({change_value})"}
    data.update(add_data)
    print(data)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)  # indent=4 makes the JSON readable


if __name__ == "__main__":
    coin_name = "bitcoin"
    #init_json_file(coin_name, f"{coin_name}_info.json")

    current_info, change_point = coin_data.get_today_stock_data(coin_name)
    save_data_json(f"{coin_name}_info.json", coin_name, current_info, change_point)
    # load_data_json(f"{coin_name}_info.json")
