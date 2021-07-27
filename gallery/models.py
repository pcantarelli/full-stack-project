from django.db import models

# Create your models here.


class GalleryImages(models.Model):
    class Meta:
        verbose_name_plural = "Gallery images"

    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to="gallery/",
        null=False,
        blank=False,
        height_field="height",
        width_field="width",
    )
    height = models.IntegerField(
        null=True,
        blank=True,
    )
    width = models.IntegerField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
