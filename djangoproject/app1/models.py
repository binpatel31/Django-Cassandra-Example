from django.db import models
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


# Create your models here.

class orm(Model):
    __keyspace__ = 'home'
    ormID = columns.UUID(primary_key = True)
    #below will work as clustering key . so to add clustering key means define second primary key
    #so in short apart from first column which is defined as primary key, if we mention primary key n any other column it will become clustering key
    #stud_id = columns.Integer(primary_key = True, clustering_order = "DESC")
    first_name = columns.Text()
    last_name = columns.Text()
