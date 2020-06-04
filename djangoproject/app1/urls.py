from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_index,name="api-index"),   ### param1 = url , param 2 = which function should get executed when user get on this url,
                             ### param3 = name of this url which will be helpful for reverse lookup

   path('all-person/',views.all_person,name="all_person"),
   path('one-person/<str:ormID>/',views.one_person,name="one_person"),
   path('create-person/',views.create_person,name="create_person"),
   path('update-person/<str:ormID>/',views.update_person,name="update_person"),
   path('delete-person/<str:ormID>/',views.delete_person,name="delete_person"),
]
