from elasticsearch import Elasticsearch

es  = Elasticsearch()
res = es.search(index="listings", body={"query": {"match_all": {}}})

for listing in res['hits']['hits']:
    print(listing['_source']['title'] + "\r\n")