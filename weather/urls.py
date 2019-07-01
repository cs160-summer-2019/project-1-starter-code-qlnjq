from django.urls import path

from . import views

urlpatterns = [
    path('neareststorm/', views.neareststorm, name='neareststorm'),
    path('seepriority/', views.seepriority, name='seepriority'),
    path('forecast/', views.forecast, name='forecast'),
    path('forecast/alert/', views.forecast_alert, name='forecast_alert'),
    path('', views.index, name='index'),
]