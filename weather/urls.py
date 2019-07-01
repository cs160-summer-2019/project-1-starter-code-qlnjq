from django.urls import path

from . import views

urlpatterns = [
    #path('neareststorm/', views.neareststorm, name='neareststorm'),
    path('seepriority/', views.seepriority, name='seepriority'),
    path('forecast/', views.forecast, name='forecast'),
    path('forecast/without/', views.forecast_without, name='forecast_without'),
    path('alert', views.alert, name='alert'),
    path('', views.index, name='index'),
]