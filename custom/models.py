from django.db import models

class CustomWorkType(models.Model):

    work_type = models.CharField(max_length=254)
    price_type = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work_type

class CustomSizes(models.Model):

    class Meta:
        verbose_name_plural = 'Custom sizes'

    size = models.PositiveSmallIntegerField(null=True, blank=True)
    price_size = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.size)