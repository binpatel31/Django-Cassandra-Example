from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="blog-home"),   ### param1 = url , param 2 = which function should get executed when user get on this url,
                            ### param3 = name of this url which will be helpful for reverse lookup
]
