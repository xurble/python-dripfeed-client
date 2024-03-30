
import requests


class DripFeedException(Exception):
    pass


class DripFeed:

    def __init__(self, api_key, server="https://dripfeed.app", verify_https=True):

        self.api_key = api_key
        self.server = server
        self.verify = verify_https
        self.headers = {
            "Authorization": "Bearer " + api_key
        }

    def list_feeds(self):

        ret = requests.get(f"{self.server}/api/v1/feeds/", headers=self.headers, verify=self.verify)
        if ret.ok:
            return ret.json()

    def add_feed(self, url: str, name=None):

        data = {
            "url": url,
            "name": name
        }
        ret = requests.put(f"{self.server}/api/v1/feeds/", data=data, headers=self.headers, verify=self.verify)
        if ret.ok:
            return ret.json()["feed"]

    def update_feed(self, id: str, name: str, live: bool):

        data = {
            "name": name,
            "live": live
        }
        ret = requests.post(f"{self.server}/api/v1/feed/{id}/", data=data, headers=self.headers, verify=self.verify)
        if ret.ok:
            return ret.json()["item"]

    def delete_feed(self, id: str):

        ret = requests.delete(f"{self.server}/api/v1/feed/{id}/", headers=self.headers, verify=self.verify)
        if ret.ok:
            return True
