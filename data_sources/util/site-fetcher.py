import requests
from lxml import html
class SiteFetcher:

    def get_site(url):

        r=requests.get(url)
        tree = html.fromstring(page.content)
        return tree


