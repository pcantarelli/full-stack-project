from django.shortcuts import render
from .models import CustomWorkType, CustomSizes
from doodles.models import Doodles


def custom(request):
    """A view to show individual doodle product page"""

    work_types = CustomWorkType.objects.all().order_by("price_type")
    sizes = CustomSizes.objects.all().order_by("price_size")
    doodles = Doodles.objects.all()
    doodles = doodles.order_by("-updated_at")[:4]

    context = {
        "work_types": work_types,
        "sizes": sizes,
        "doodles": doodles,
    }
    return render(request, "custom/custom.html", context)
