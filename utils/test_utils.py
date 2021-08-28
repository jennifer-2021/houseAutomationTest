import requests


class TestUtils:

    @staticmethod
    def verify_links(link_url):
        response = requests.get(link_url, timeout=10)
        status_code = response.status_code
        if status_code != 200:
            print("........broken link: " + link_url + "status_code: " + status_code)
            return False
        return True

