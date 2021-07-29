from django import forms
from .models import GalleryImages


class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImages
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        """
        Function to overide form inital settings
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == "height" or field == "width" or field == "image_url":
                self.fields[field].label = False
                self.fields[field].widget.attrs["class"] = "hide"

