from django.shortcuts import render
from django.http import HttpResponse
from cassandra.query import dict_factory
import uuid
from django.conf import settings

### for connection and ORM
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster


###for models
from . models import orm
from cassandra.cqlengine.management import sync_table
from cassandra import metadata

def home(request):
    #sync_table(orm)   ### sync to be done for first time to create table in DB ...just like migrate
    session = settings.CONNECTION[1]
    session.row_factory = dict_factory
    ormid = uuid.uuid1() 
    orm.create(ormID=ormid,first_name = "Bin", last_name="patel")
    #obj.save() ### either we can do orm(//pass column data) and then do save ----  OR ----- directly do orm.create(//pass the data)

    '''  printing the data which was just inserted       '''
    #row = session.execute('SELECT *  FROM home.orm where ormID ='+ormid)   ### same as below
    row = orm.objects.filter(ormID=ormid)  

    ctx = {'result': row, 'param1': "OM!!!"}
    return render(request, "app1/home.html", ctx) ### here provide path detail starting from inside template folder
    ### so here django will look for all template folders in this project and then in that folder, the folder with name
    ### blog is searched and then ...next step is to get this home.html file

