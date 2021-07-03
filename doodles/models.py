from django.db import models

# Create your models here.
class Doodles(models.Model):

    class Meta:
        verbose_name_plural = 'Doodles'

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.PositiveSmallIntegerField(null=True, blank=True)
    time_to_complete = models.PositiveSmallIntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)  
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name