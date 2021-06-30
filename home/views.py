from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Function to return a view of the index page
    """
    return render (request, 'home/index.html')