
import requests


class DripFeedException(Exception):

    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)


class DripFeed:

    def __init__(self, api_key, server="https://dripfeed.app", verify_https=True):

        self.api_key = api_key
        self.server = server
        self.verify = verify_https
        self.headers = {
            "Authorization": "Bearer " + api_key
        }

    def list_feeds(self):

        try:
            ret = requests.get(f"{self.server}/api/v1/feeds/", headers=self.headers, verify=self.verify)
        except Exception as ex:
            raise DripFeedException(0, str(ex))

        if ret.ok:
            return ret.json()
        else:
            if ret.status_code == 500:
                raise DripFeedException(500, "Server Error")
            else:
                raise DripFeedException(ret.status_code, ret.json()["detail"])

    def add_feed(self, url: str, name=None, live=True):

        data = {
            "url": url,
            "name": name,
            "live": live
        }
        try:
            ret = requests.put(f"{self.server}/api/v1/feeds/", json=data, headers=self.headers, verify=self.verify)
        except Exception as ex:
            raise DripFeedException(0, str(ex))

        if ret.ok:
            return ret.json()["feed"]
        else:
            if ret.status_code == 500:
                raise DripFeedException(500, "Server Error")
            else:
                raise DripFeedException(ret.status_code, ret.json()["detail"])

    def get_or_add_feed(self, url, name=None, live=True):

        try:
            return self.add_feed(url, name, live)
        except DripFeedException as ex:
            if ex.status_code == 400:
                feeds = self.list_feeds()["feeds"]
                for feed in feeds:
                    if feed["source_url"] == url:
                        if name is None:
                            name = feed["name"]

                        if name != feed["name"] or live != feed["live"]:
                            return self.update_feed(feed["uuid"], name, live)
                        else:
                            return feed
                # Getting here is weird
                raise DripFeedException(0, "Could not add feed.")
            else:
                raise ex

    def update_feed(self, id: str, name: str, live: bool):

        data = {
            "name": name,
            "live": live
        }
        try:
            ret = requests.post(f"{self.server}/api/v1/feed/{id}/", json=data, headers=self.headers, verify=self.verify)
        except Exception as ex:
            raise DripFeedException(0, str(ex))

        if ret.ok:
            return ret.json()["feed"]
        else:
            if ret.status_code == 500:
                raise DripFeedException(500, "Server Error")
            else:
                raise DripFeedException(ret.status_code, ret.json()["detail"])

    def delete_feed(self, id: str):

        try:
            ret = requests.delete(f"{self.server}/api/v1/feed/{id}/", headers=self.headers, verify=self.verify)
        except Exception as ex:
            raise DripFeedException(0, str(ex))

        if not ret.ok:
            if ret.status_code == 500:
                raise DripFeedException(500, "Server Error")
            else:
                raise DripFeedException(ret.status_code, ret.json()["detail"])
