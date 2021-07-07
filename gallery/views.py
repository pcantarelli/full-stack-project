from django.shortcuts import render
from .models import GalleryImages

# Create your views here.

def gallery(request):
    """
    Function to return a view of the gallery images
    """

    gallery_images = GalleryImages.objects.all()
    gallery_images = gallery_images.order_by('-updated_at')

    context = {
        'gallery_images': gallery_images,
    }

    return render (request, 'gallery/gallery.html', context)
