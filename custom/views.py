from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CustomWorkType, CustomSizes

# Create your views here.
def custom(request):
    """ A view to show individual doodle product page """

    work_types = CustomWorkType.objects.all()
    sizes = CustomSizes.objects.all()
    size_max = sizes.order_by('-size').first()
    size_min = sizes.order_by('size').first()


    context = {
        'work_types': work_types,
        'sizes': sizes,
        'size_max': size_max,
        'size_min': size_min,       
    }

    return render(request, 'custom/custom.html', context)