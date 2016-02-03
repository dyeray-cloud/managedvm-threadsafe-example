from google.appengine.ext import ndb


class NumInstances(ndb.Model):
    count = ndb.IntegerProperty(default=0)
