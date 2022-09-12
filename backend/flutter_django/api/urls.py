
from urllib.parse import urlparse
from django.urls import path
from api import views

from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('login/', views.login),
    path('generatetoken/', obtain_auth_token, name='api_token_auth'),
    #path('generatetoken/', views.GenerateTokenView.as_view(), name='GenerateToken'),
]

