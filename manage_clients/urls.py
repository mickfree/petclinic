from django.urls import path
from .views import * 

urlpatterns=[
    path('',index_manage_client, name='index_manage'),
        ]
