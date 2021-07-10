from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import GalleryImages


# Create your views here.

def gallery(request):
    """
    Function to return a view of the gallery images
    """

    gallery_images = GalleryImages.objects.all()
    gallery_images = gallery_images.order_by('-updated_at')
    paginator = Paginator(gallery_images, 9) # Show 9 images per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'gallery_images': gallery_images,
        'page_obj': page_obj
    }

    return render (request, 'gallery/gallery.html', context)


def image(request, image_id):
    """ A view to show individual doodle product page """

    image = get_object_or_404(GalleryImages, pk=image_id)

    context = {
        'image': image,
    }

    return render(request, 'gallery/image.html', context)