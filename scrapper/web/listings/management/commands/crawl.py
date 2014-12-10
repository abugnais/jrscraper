from django.core.management.base import BaseCommand, CommandError
from listings.search import Search
from lxml import html
from elasticsearch import Elasticsearch
import requests
import re

class Command(BaseCommand):
    help = "crawling and indexing the search page of justrentals"

    base_url        = "http://www.justrentals.com/dubai/property-for-rent.html"
    default_count   = 100


    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count       = self.default_count
        page        = requests.get(self.base_url, params={"limit": count})
        html_tree   = html.fromstring(page.text)
        results     = html_tree.xpath("//div[@class='search_listings_box']")
        search      = Search()

        for res in results:
            title   = res.xpath('.//span[@class="p_title"]/text()')[0].strip()
            image   = res.xpath('.//img[@class="search_results_img"]/@src')[0].strip()
            id      = re.sub('row_[0-9]+_', '', res.xpath('./@id')[0])
            search.save(id, {"title": title, "image": image})
