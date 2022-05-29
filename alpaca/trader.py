import requests, json
from config import *
from order import *

APCA_API_BASE_URL= PAPER_BASE_URL
ACCOUNT_URL = "{}/v2/account".format(APCA_API_BASE_URL)
ORDER_URL = "{}/v2/orders".format(APCA_API_BASE_URL)
HEADERS = {"APCA_API_KEY_ID": PAPER_API_key, "APCA_API_SECRET_KEY": Secret_key}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)

    return json.loads(r.content)
