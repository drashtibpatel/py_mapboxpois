from django.shortcuts import render, redirect
from managepois.models import MapboxPOIs
import json
import os

def view_mapbox(request):
    mapboxToken = os.environ.get('MAPBOX_TOKEN')
    mapboxPOIs = MapboxPOIs.objects.all().filter(status=1)
    mapboxData = []
    for mapboxPOI in mapboxPOIs:
        mapboxData.append(eval(mapboxPOI.geometry))
    mapboxData = json.dumps(mapboxData) 
    return render(request,"mapbox/index.html",{'mapboxData':mapboxData, 'mapboxToken' : mapboxToken})
