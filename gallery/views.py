from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import GalleryImages
from .forms import GalleryForm

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
    """ A view to show individual image page """

    image = get_object_or_404(GalleryImages, pk=image_id)

    context = {
        'image': image,
    }

    return render(request, 'gallery/image.html', context)


@login_required
def add_image(request):
    """ View to add a new image"""
    if not request.user.is_superuser:
        messages.error(request, 'Access denied! Only store admin can add an image.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            messages.success(request, 'Image added sucessfully!')
            return redirect(reverse('image', args=[image.id]))
        else:
            messages.error(request,
                           ('Adding new image failed. '
                            'Check if the form is valid.'))
    else:
        form = GalleryForm()

    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }
    return render(request, template, context)



@login_required
def edit_image(request, image_id):
    """ Edit a image in the store gallery"""
    if not request.user.is_superuser:
        messages.error(request, 'Access denied! Only store admin can edit a image.')
        return redirect(reverse('home'))

    image = get_object_or_404(GalleryImages, pk=image_id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image edited sucessfully!!')
            return redirect(reverse('image', args=[image.id]))
        else:
            messages.error(request,
                           ('Editing image failed. '
                            'Check if the form is valid.'))
    else:
        form = GalleryForm(instance=image)
        messages.info(request, f'Editing {image.name}')

    template = 'gallery/edit_image.html'
    context = {
        'form': form,
        'image': image,
    }
    return render(request, template, context)


@login_required
def delete_image(request, image_id):
    """ Delete a image from the store gallery"""
    if not request.user.is_superuser:
        messages.error(request, 'Access denied! Only store admin can delete a image.')
        return redirect(reverse('home'))

    image = get_object_or_404(GalleryImages, pk=image_id)
    image.delete()
    messages.success(request, 'Image deleted!')
    return redirect(reverse('gallery'))