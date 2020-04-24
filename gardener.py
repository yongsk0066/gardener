import requests
import datetime
from bs4 import BeautifulSoup

USERNAME = "yongsk0066"
BASE_URL = "https://www.github.com/"

today = datetime.date.today()
res = requests.get(BASE_URL + USERNAME)

soup = BeautifulSoup(res.text, 'html.parser')
today_count = soup.find('rect', {'data-date': today})['data-count']
