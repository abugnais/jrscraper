import datetime
from haystack import indexes
from myapp.models import Note

class ListingsIndex(indexes.SearchIndex, indexes.Indexable):
    id = indexes.CharField(max_length=50, primary_key=True)
    title = indexes.CharField(max_length=1000)
    image = indexes.CharField(max_length=1000)