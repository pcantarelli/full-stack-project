from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Function to overide form inital settings
        """
        super().__init__(*args, **kwargs)
        labels = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postal Code',
            'default_country': 'Country',
        } 
        for field in self.fields:
            label = labels[field]
            self.fields[field].label = label


