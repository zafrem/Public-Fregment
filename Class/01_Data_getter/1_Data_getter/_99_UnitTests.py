#pip install unittest

import unittest
import _1_Stock_yfinance as stock
import _2_Altcoin_google as altcoin
import _3_RSS_Trend_Keyword_Google_trend as trend_1
import _3_Scraping_Trend_Keyword_Blackkiwi as trend_2
import _4_Scraping_Spot_NFL as nfl
import _5_Scraping_Spot_Premier_League as premier_league
import _6_Scraping_Weather_windy as weather

class web_scraping:
    def _stock(self, target):
        return stock.get_today_stock_data(target)

    def _altcoin(self, target):
        return altcoin.get_today_stock_data(target)

    def _google_trend(self, target):
        return trend_1.get_trend(target)

    def _blackkiwi_trend(self):
        return trend_2.get_keyword()

    def _nfl(self):
        return nfl.get_nfl_schedules()

    def _premier_league(self):
        return premier_league.get_keyword()

    def _weather(self):
        return weather.get_keyword()

class PlusTest(unittest.TestCase):
    def setUp(self):
        self.scraping = web_scraping()

    #def test_stock(self):
    #    self.assertIn("Tesla", self.scraping._stock("Tesla"))

    #def test_altcoin(self):
    #    self.assertIn("dogecoin", self.scraping._altcoin("dogecoin"))

    def test_trend_google(self):
        self.assertIn('[Google Trend - KR]', self.scraping._google_trend('KR'))

    def test_trend_blackkiwi(self):
        self.assertIn('1.', self.scraping._blackkiwi_trend())

    def test_nfl(self):
        self.assertTrue(self.scraping._nfl())

    def test_premier_league(self):
        self.assertTrue(self.scraping._premier_league())

    def test_weather(self):
        self.assertIn('Time', self.scraping._weather())


if __name__ == '__main__':
    unittest.main()