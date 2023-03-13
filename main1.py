import urllib3
import json
def get_data():
    http = urllib3.PoolManager()
    url = "https://cloud.iexapis.com/stable/stock/tsla/previous?token=pk_8c1b9e2e916447dfbc27191e895e212b"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values
get_data()
