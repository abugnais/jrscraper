from django.core.management.base import BaseCommand, CommandError
from listings.search import Search
from lxml import html
from elasticsearch import Elasticsearch
from optparse import make_option
import requests
import re

class Command(BaseCommand):
    help            = "crawling and indexing the search page of justrentals"
    base_url        = "http://www.justrentals.com/dubai/property-for-rent.html"
    default_count   = 30

    option_list = BaseCommand.option_list + (
        make_option(
            "-c",
            "--count",
            dest = "count",
            help = "specify number of crawled listings"
        ),
    )

    def handle(self, *args, **options):
        if(options["count"] == None):
            count = self.default_count
        else:
            count = options["count"]

        page        = requests.get(self.base_url, params={"limit": count})
        html_tree   = html.fromstring(page.text)
        results     = html_tree.xpath("//div[@class='search_listings_box']")
        search      = Search()

        for res in results:
            title   = res.xpath('.//span[@class="p_title"]/text()')[0].strip()
            image   = res.xpath('.//img[@class="search_results_img"]/@src')[0].strip()
            id      = re.sub('row_[0-9]+_', '', res.xpath('./@id')[0])
            search.save(id, {"title": title, "image": image})

