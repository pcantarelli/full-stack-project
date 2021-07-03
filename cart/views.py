from django.shortcuts import render

# Create your views here.

def cart(request):
    """
    Function to return a view of the cart page
    """

    return render (request, 'cart/cart.html', context)