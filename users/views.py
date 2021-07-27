from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import ProfileForm


@login_required
def profile(request):
    """View to display User Profile information"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile info updated successfully!")
        else:
            messages.error(
                request, ("Sorry, update failed. Please verify that the form is valid.")
            )
    else:
        form = ProfileForm(instance=profile)
        orders = profile.orders.all()
        orders = orders.order_by("-updated_at")

    template = "users/profile.html"
    context = {
        "profile": profile,
        "form": form,
        "orders": orders,
    }
    return render(request, template, context)
