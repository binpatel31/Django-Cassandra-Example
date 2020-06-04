from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from cassandra.query import dict_factory
import uuid
from django.conf import settings

### for connection and ORM     
'''
ACTUALLY HERE IF WE USE ORM THEN NO NEED TO USE CONNECTION AND ALL HERE..BUTI USED HERE BECUASE BELOW IS EXAMPLE WHERE YOU CAN DO FIRE QUERY WITHOUT ORM ...I.E. JUST WITH SIMPLE QUERY STRING AND SESSION OBJECT....SEE BELOW LAST
'''
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster

###for models
from . models import orm
from cassandra.cqlengine.management import sync_table
from cassandra import metadata

### for REST serialzier
from rest_framework.parsers import JSONParser
from .serializers import ormSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


############################################### USING APIS ############################################

@api_view(['GET'])
def api_index(request):
    api_urls = {
     "All Person" : "/all-person/",   ### try to use - instead of _
     "one person full detail" : "/one-person/<str:ormID>/",
     "create person": "/create-person/",
     "update person":"/update-person/<str:ormID>/",
     "delete-person":"/delete-person/<str:ormID>/", 
    }
    return Response(api_urls)

@api_view(["GET"])
def all_person(request):
    person = orm.objects.all()
    serializer  = ormSerializer(person, many = True)  #### may=True becuase it is queryset
    return Response(serializer.data)
    
@api_view(["GET"])
def one_person(request,ormID):
    ormID = uuid.UUID(ormID)
    person = orm.objects.filter(ormID=ormID)
    serializer  = ormSerializer(person, many = True)  #### may=True becuase it is queryset
    return Response(serializer.data)


@api_view(["POST"])
def create_person(request):
    #data = JSONParser().parse(request)
    serializer = ormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(["PUT"])   #### HERE POST ALSO WORKS
def update_person(request,ormID):
    #data = JSONParser().parse(request)
    ormID = uuid.UUID(ormID)
    person = orm.objects.get(ormID=ormID)   ### here i must have to use get because..filter may return multiple data but here bulk update oR delete is no supported. see my django rest google DOC for more information.
    serializer  = ormSerializer(instance = person,data=request.data, many = False)  #### may=True becuase it is queryset
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["DELETE"])
def delete_person(request,ormID):
    ormID = uuid.UUID(ormID)
    person = orm.objects.filter(ormID=ormID)
    person.delete()
    return Response("Item Deleted Successfully!")



###########################################################################################################

### BELOW IS FROM PREVIOUS PRACTICALS ####


def home(request):
    #sync_table(orm)   ### sync to be done for first time to create table in DB ...just like migrate
    session = settings.CONNECTION[1]    #### SEE COMMENT IN LINE 8
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

