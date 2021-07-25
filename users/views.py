from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import ProfileForm


# Create your views here.
def profile(request):
    """ View to display User Profile information"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile info updated successfully!')
        else:
            messages.error(request, ('Sorry, update failed. Please verify that the form is valid.'))

    form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'users/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,

    }

    return render(request, template, context)