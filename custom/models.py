from django.db import models

class CustomWorkType(models.Model):

    work_type = models.CharField(max_length=254)
    price_type = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work_type

    def name_no_space(self):
        return self.work_type.replace(' ', '_')

class CustomSizes(models.Model):

    class Meta:
        verbose_name_plural = 'Custom sizes'

    size = models.PositiveSmallIntegerField(null=True, blank=True)
    price_size = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.size)

class CustomersFiles(models.Model):

    class Meta:
        verbose_name_plural = 'Customers Files'

    customer_file = models.FileField(upload_to='custom/customers_files', null=True, blank=True)
    customer_file_url = models.URLField(max_length=1024, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.id)
