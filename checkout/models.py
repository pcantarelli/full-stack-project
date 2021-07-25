import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from doodles.models import Doodles
from custom.models import CustomWorkType, CustomSizes, CustomersFiles
from users.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    original_cart = models.TextField(null=False, blank=False, default='')
    order_total = models.DecimalField(max_digits=10, decimal_places=2,null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Function to create random unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Funtion to update the order_total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Function to override the standard save method and set an order_number if does not exits
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product_type = models.CharField(max_length=32, null=False, blank=False)
    doodle = models.ForeignKey(Doodles, null=True, blank=True, on_delete=models.CASCADE)
    work_type = models.ForeignKey(CustomWorkType, null=True, blank=True, on_delete=models.CASCADE)
    customer_file = models.ForeignKey(CustomersFiles, null=True, blank=True, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField(null=True, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def __str__(self):
        return f'Line item id: {self.id} from order: {self.order.order_number}'
