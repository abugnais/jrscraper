from elasticsearch import Elasticsearch

es = Elasticsearch()
es.indices.delete(index='test-index')