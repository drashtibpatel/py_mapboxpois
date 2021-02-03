from django import forms  
from managepois.models import MapboxPOIs

class MapboxPOIsForms(forms.ModelForm):  

    class Meta:  
        model = MapboxPOIs  
        fields = "__all__" 
        widgets = {'geometry': forms.HiddenInput()} 