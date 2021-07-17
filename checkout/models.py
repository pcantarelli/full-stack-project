import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from doodles.models import Doodles
from custom.models import CustomWorkType, CustomSizes, CustomersFiles



class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product_type = models.CharField(max_length=32, null=False, blank=False, editable=False)
    doodle = models.ForeignKey(Doodles, null=True, blank=True, on_delete=models.CASCADE)
    work_type = models.ForeignKey(CustomWorkType, null=True, blank=True, on_delete=models.CASCADE)
    customer_file = models.ForeignKey(CustomersFiles, null=True, blank=True, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField(null=True, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def __str__(self):
        return f'Line item id: {self.id} from order: {self.order.order_number}'
