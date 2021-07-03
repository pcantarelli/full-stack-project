from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Doodles

# Create your views here.

def doodles_collection(request):
    """
    Function to return a view of the Doodles Catalog page
    """

    doodles = Doodles.objects.all()
    sort = None
    direction = None
    doodles = doodles.order_by('-updated_at')

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            print(sortkey)
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                doodles = doodles.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            print(sortkey)
            doodles = doodles.order_by(sortkey)

    sorting = f'{sort}_{direction}'

    context = {
        'doodles': doodles,
        'sorting': sorting,
    }

    return render (request, 'doodles/collection.html', context)

def dooddle_page(request, doodle_id):
    """ A view to show individual doodle product page """

    doodle_product = get_object_or_404(Doodles, pk=doodle_id)
    doodles = Doodles.objects.all()
    

    context = {
        'doodle_product': doodle_product,
        'doodles': doodles,
    }

    return render(request, 'doodles/dooddle_page.html', context)

def doodles_search(request):
    """
    Function to return a view of the Doodles search page
    """

    doodles = Doodles.objects.all()
    query = None

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("No search term enter"))
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            doodles = doodles.filter(queries)

    context = {
        'doodles': doodles,
        'query': query,
    }

    return render (request, 'doodles/doodles_search.html', context)