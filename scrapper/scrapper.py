import requests
import md5
from lxml import html
from elasticsearch import Elasticsearch

page = requests.get('http://www.justrentals.com/dubai/property-for-rent.html?limit=30')
tree = html.fromstring(page.text)

results = tree.xpath("//div[@class='search_listings_box']")
es = Elasticsearch()

for res in results:
    title = res.xpath('.//span[@class="p_title"]/text()')[0].strip()
    image = res.xpath('.//img[@class="search_results_img"]/@src')[0].strip()
    id = res.xpath('./@id').replace()

    doc = {
        'title' : title,
        'image' : image
    }
    es.index(index="test-index", doc_type='listing', id=id, body=doc)

es.indices.refresh(index="test-index")