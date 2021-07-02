from django.shortcuts import render
from .models import Doodles

# Create your views here.

def doodles_collection(request):
    """
    Function to return a view of the Doodles Catalog page
    """

    doodles = Doodles.objects.all()

    context = {
        'doodles': doodles,
    }

    return render (request, 'doodles/collection.html', context)