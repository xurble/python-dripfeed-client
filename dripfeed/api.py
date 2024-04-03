
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

    def add_feed(self, url: str, name=None, live=True):

        data = {
            "url": url,
            "name": name,
            "live": live
        }
        ret = requests.put(f"{self.server}/api/v1/feeds/", json=data, headers=self.headers, verify=self.verify)
        if ret.ok:
            return ret.json()["feed"]
        else:
            if ret.status_code == 500:
                raise DripFeedException("Server Error")
            else:
                raise DripFeedException(ret.json()["detail"])

    def update_feed(self, id: str, name: str, live: bool):

        data = {
            "name": name,
            "live": live
        }
        ret = requests.post(f"{self.server}/api/v1/feed/{id}/", json=data, headers=self.headers, verify=self.verify)
        if ret.ok:
            return ret.json()["feed"]
        else:
            if ret.status_code == 500:
                raise DripFeedException("Server Error")
            else:
                raise DripFeedException(ret.json()["detail"])

    def delete_feed(self, id: str):

        ret = requests.delete(f"{self.server}/api/v1/feed/{id}/", headers=self.headers, verify=self.verify)
        if not ret.ok:
            if ret.status_code == 500:
                print(ret.content)
                raise DripFeedException("Server Error")
            else:
                raise DripFeedException(ret.json()["detail"])
