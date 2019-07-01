from django.shortcuts import render
from django.http import HttpResponse

def forecast(request):
    return render(request, 'weather/forecast.html')

def forecast_alert(request):
    return render(request, 'weather/forecast-alert.html')

def neareststorm(request):
    return render(request, 'weather/nearest-storm.html')

def seepriority(request):
    return render(request, 'weather/see-priority-storms.html')

def index(request):
    return render(request, 'weather/index.html')