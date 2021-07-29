from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator

from .models import Doodles
from .forms import DoodleForm


def doodles_collection(request):
    """
    Function to return a view of the Doodles Catalog page
    """

    doodles = Doodles.objects.all()
    sort = None
    direction = None
    doodles = doodles.order_by("-updated_at")

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                doodles = doodles.annotate(lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            doodles = doodles.order_by(sortkey)

    sorting = f"{sort}_{direction}"
    paginator = Paginator(doodles, 8)  # Show 8 images per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"doodles": doodles, "sorting": sorting, "page_obj": page_obj}
    return render(request, "doodles/collection.html", context)


def dooddle_page(request, doodle_id):
    """A view to show individual doodle product page"""

    doodle_product = get_object_or_404(Doodles, pk=doodle_id)
    doodles = Doodles.objects.all()
    doodles = doodles.exclude(
        id__in=[doodle_id]
    )  # Exclude doodle product from doodles recomended list

    context = {
        "doodle_product": doodle_product,
        "doodles": doodles,
    }
    return render(request, "doodles/dooddle_page.html", context)


def doodles_search(request):
    """
    Function to return a view of the Doodles search page
    """

    doodles = Doodles.objects.all()
    query = None

    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            messages.error(request, ("No search term enter"))
            return redirect(reverse("home"))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        doodles = doodles.filter(queries)

    context = {
        "doodles": doodles,
        "query": query,
    }
    return render(request, "doodles/doodles_search.html", context)


@login_required
def add_doodle(request):
    """View to add a new doodle"""

    if not request.user.is_superuser:
        messages.error(
            request,
            "Access denied! Only store admin can create a Doodle.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = DoodleForm(request.POST, request.FILES)
        if form.is_valid():
            doodle = form.save()
            messages.success(request, "Doodle added sucessfully!")
            return redirect(reverse("dooddle_page", args=[doodle.id]))
        else:
            messages.error(
                request, ("Adding new doodle failed. "
                          "Check if the form is valid."))
    else:
        form = DoodleForm()

    template = "doodles/add_doodle.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_doodle(request, doodle_id):
    """Edit a doodle in the store"""

    if not request.user.is_superuser:
        messages.error(
            request,
            "Access denied! Only store admin can edit a Doodle.")
        return redirect(reverse("home"))

    doodle = get_object_or_404(Doodles, pk=doodle_id)

    if request.method == "POST":
        form = DoodleForm(request.POST, request.FILES, instance=doodle)
        if form.is_valid():
            form.save()
            messages.success(request, "Doodle edit sucessfully!!")
            return redirect(reverse("dooddle_page", args=[doodle.id]))
        else:
            messages.error(
                request, ("Editing doodle failed. "
                          "Check if the form is valid."))
    else:
        form = DoodleForm(instance=doodle)
        messages.info(request, f"Editing {doodle.name}")

    template = "doodles/edit_doodle.html"
    context = {
        "form": form,
        "doodle": doodle,
    }
    return render(request, template, context)


@login_required
def delete_doodle(request, doodle_id):
    """Delete a doodle from the store"""

    if not request.user.is_superuser:
        messages.error(
            request,
            "Access denied! Only store admin can delete a Doodle.")
        return redirect(reverse("home"))

    doodle = get_object_or_404(Doodles, pk=doodle_id)
    doodle.delete()
    messages.success(request, "Doodle deleted!")

    return redirect(reverse("doodles"))
