from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('graph', views.graph),
    path('report', views.report),
    path('settings', views.settings),
    path('login', views.login),
]
