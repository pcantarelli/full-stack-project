from django.shortcuts import render
from doodles.models import Doodles
from gallery.models import GalleryImages


# Create your views here.


def index(request):
    """
    Function to return a view of the index page
    """

    doodles = Doodles.objects.all()
    doodles = doodles.order_by("-updated_at")[:4]
    gallery_images = GalleryImages.objects.all()
    gallery_images = gallery_images.order_by("-updated_at")[:3]

    context = {
        "doodles": doodles,
        "gallery_images": gallery_images,
    }
    return render(request, "home/index.html", context)
