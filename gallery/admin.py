from django.contrib import admin
from .models import GalleryImages

# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = (
        "height",
        "width",
    )
    list_display = (
        "name",
        "image",
        "created_at",
        "updated_at",
    )
    ordering = ("-updated_at",)


admin.site.register(GalleryImages, GalleryAdmin)
