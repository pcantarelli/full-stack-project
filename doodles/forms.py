from django import forms
from .models import Doodles


class DoodleForm(forms.ModelForm):

    class Meta:
        model = Doodles
        fields = '__all__'

    def __init__(self, *args, **kwargs):    
        """
        Function to overide form inital settings
        """
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'size': 'Size (in cm2)',
            'time_to_complete': 'Time to complete (in hours)',
            'image_url': 'Image URL',
            'image': 'Image file',
        } 
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label