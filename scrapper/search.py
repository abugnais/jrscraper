from elasticsearch import Elasticsearch

es = Elasticsearch()
res = es.search(index="test-index", body={"query": {"match_all": {}}})

for listing in res['hits']['hits']:
    print(listing['_source']['title'] + "\r\n")