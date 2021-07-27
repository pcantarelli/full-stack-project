from django.contrib import admin
from .models import Doodles

# Register your models here.


class DoodlesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "size",
        "time_to_complete",
        "image",
        "created_at",
        "updated_at",
    )
    ordering = ("-updated_at",)


admin.site.register(Doodles, DoodlesAdmin)
