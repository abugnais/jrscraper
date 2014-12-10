from django.db import models
from elasticutils.contrib.django import MappingType

#class Listing(models.Model):
#    id = models.CharField(max_length=50, primary_key=True)
#    title = models.CharField(max_length=1000)
#    image = models.CharField(max_length=1000)
#
#    def __unicode__(self):
#        return self.id
#
#class ListingType(MappingType):
#    @classmethod
#    def get_model(cls):
#        return Listing
#
#    @classmethod
#    def get_mapping(cls):
#        return {
#            'properties': {
#                'id': {'type': 'string'},
#                'title': {'type': 'string'},
#                'image': {'type': 'string'}
#            }
#        }
#
#    @classmethod
#    def extract_document(cls, obj_id, obj=None):
#        if obj is None:
#            obj = cls.get_model().objects.get(pk=obj_id)
#
#        return {
#            'id': obj.id,
#            'title': obj.title,
#            'image': obj.image,
#        }
#