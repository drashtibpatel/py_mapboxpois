from django.shortcuts import render, redirect
from managepois.forms import MapboxPOIsForms  
from managepois.models import MapboxPOIs
import json
import os

# GET  Request: Display form for adding new points of interest details.
# POST Request: save new points of interest details into DB table.
def add_pois(request): 
    mapboxToken = os.environ.get('MAPBOX_TOKEN')
    if request.method == "POST":  
        form = MapboxPOIsForms(request.POST)  
        try:
            formResponse = save_pois_data(form)
            if(formResponse == "Data Saved"):
                return redirect('/admin/view')
        except:  
            pass
    else:  
        form = MapboxPOIsForms()  
    return render(request,'managepois/add-pois.html',{'form':form, 'mapboxToken' : mapboxToken})


# GET  Request: Display all the points of interest details.
def view_pois(request):  
    mapboxPOIs = MapboxPOIs.objects.all()  
    return render(request,"managepois/view-pois.html",{'mapboxPOIs':mapboxPOIs})


# GET  Request: Display form for update points of interest details.
# POST Request: save the updated details of points of interest detail into the DB table.
def edit_pois(request, id):
    mapboxToken = os.environ.get('MAPBOX_TOKEN')
    mapboxPOIs = MapboxPOIs.objects.get(id=id)
    if request.method == "POST":
        form = MapboxPOIsForms(request.POST, instance = mapboxPOIs) 
        try:
            formResponse = save_pois_data(form)
            if(formResponse == "Data Saved"):
                return redirect('/admin/view')
        except:  
            pass
    else:
        form = MapboxPOIsForms(instance = mapboxPOIs) 
        return render(request, 'managepois/edit-pois.html', {'form': form, 'mapboxPOIs': mapboxPOIs, 'mapboxToken' : mapboxToken})  


# GET  Request: Delete points of interest details from the DB table.
def delete_pois(request, id):  
    mapboxPOIs = MapboxPOIs.objects.get(id=id)    
    mapboxPOIs.delete()  
    return redirect('/admin/view')


# Generate GeoJson object based on the points of interest details.
def generate_geo_json(form):
    tempGeometry =  {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [
               float( form.cleaned_data['longitude']),
               float( form.cleaned_data['latitude'])
            ]   
            },
        'properties': {
            'title': form.cleaned_data['name']
            }
        }
    return tempGeometry



# save points of interest details into the DB table.
def save_pois_data(form):
    if form.is_valid():  
        tempGeometry = generate_geo_json(form)
        post = form.save(commit=False)
        post.geometry = tempGeometry
        post.save()
        return "Data Saved"
    else:
        return "Invalid Data"
    