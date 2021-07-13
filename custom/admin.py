from django.contrib import admin
from .models import CustomWorkType, CustomSizes


class CustomWorkTypeAdmin(admin.ModelAdmin):
    list_display = (
        'work_type',
        'price_type',
        'created_at',
        'updated_at',
    )
    ordering = ('-updated_at',)

class CustomSizesAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'price_size',
        'updated_at',
    )
    ordering = ('-updated_at',)

admin.site.register(CustomWorkType, CustomWorkTypeAdmin)
admin.site.register(CustomSizes, CustomSizesAdmin)

