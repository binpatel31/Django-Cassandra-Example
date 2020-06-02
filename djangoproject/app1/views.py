from django.shortcuts import render
from django.http import HttpResponse
from cassandra.query import dict_factory
# Create your views here.
from cassandra.cluster import Cluster



def home(request):
    cluster = Cluster()
    session = cluster.connect("home")
    session.row_factory = dict_factory
    row = session.execute('SELECT *  FROM home')
    #print(rows[0])
    #for user_row in rows:
    #print user_row.name, user_row.age, user_row.email
    ctx = {'result': row, 'param1': "OM!!!"}
    return render(request, "app1/home.html", ctx) ### here provide path detail starting from inside template folder
    ### so here django will look for all template folders in this project and then in that folder, the folder with name
    ### blog is searched and then ...next step is to get this home.html file

def about(request):
    return render(request, "blog/about.html")

# Create your views here.
