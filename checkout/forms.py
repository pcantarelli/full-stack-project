from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Function to overide form inital settings
        """
        super().__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs["autofocus"] = True
