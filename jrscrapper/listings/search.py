from elasticsearch import Elasticsearch

class Search():
    index     = "listings"
    doc_type  = "listing"

    def __init__(self):
        self.es = Elasticsearch()

    def findAll(self):
        result = self.es.search(index=self.index, body={"query": {"match_all": {}}})

        for res in result["hits"]["hits"]:
            yield {"title": res["_source"]["title"], "image": res["_source"]["image"], "id": res["_id"]}

    def save(self, id, doc):
        return self.es.index(index=self.index, doc_type=self.doc_type, id=id, body=doc)

    def delete(self, id):
        return self.es.delete(index=self.index, id=id)