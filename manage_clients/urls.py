from django.urls import path
from .views import * 
from django.contrib.auth.views import LogoutView


urlpatterns=[
    path('', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('index/',index_manage_client, name='index_manage'),
    ]
