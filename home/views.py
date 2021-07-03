from django.shortcuts import render
from doodles.models import Doodles

# Create your views here.

def index(request):
    """
    Function to return a view of the index page
    """

    doodles = Doodles.objects.all()

    context = {
        'doodles': doodles,
    }
    return render (request, 'home/index.html', context)