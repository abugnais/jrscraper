from elasticsearch import Elasticsearch

class Search():
    index     = "listings"
    doc_type  = "listing"

    def __init__(self):
        self.es = Elasticsearch()
        pass

    def findAll(self):
        return self.es.search(index=self.index, body={"query": {"match_all": {}}})

    def save(self, id, doc):
        return self.es.index(index=self.index, doc_type=self.doc_type, id=id, body=doc)

    def delete(self, id):
        return self.es.delete(index=self.index, id=id)