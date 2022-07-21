from . import views
from django.urls import path
from django.template import RequestContext

app_name = 'socialApp'
urlpatterns= [
    path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('profile/<str:name>/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('doLogin/', views.home, name='doLogin'),
]