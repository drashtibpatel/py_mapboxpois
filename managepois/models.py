from django.db import models

POI_CATEGORY= [
    ('', 'Select Category'),
    ('Food', 'Food'),
    ('Restaurant', 'Restaurant'),
    ('Cafe', 'Cafe'),
    ('Software company', 'Software company')
    ]

# Create your models here.
class MapboxPOIs(models.Model):  
    name = models.CharField(max_length=50)  
    latitude = models.CharField(max_length=50)  
    longitude = models.CharField(max_length=50)  
    category = models.CharField(max_length=50, choices=POI_CATEGORY, default='')  
    geometry = models.CharField(max_length=200, blank=True)  
    status = models.BooleanField(max_length=50) 
      
    class Meta:  
        db_table = "tbl_mapbox_pois"  
