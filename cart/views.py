from django.shortcuts import redirect, render
from doodles.models import Doodles

# Create your views here.

def cart(request):
    """
    Function to return a view of the cart page

    """
    doodles = Doodles.objects.all()

    doodles_context = {
        'doodles': doodles,
    }

    return render (request, 'cart/cart.html', doodles_context)

def add_to_cart(request, item_id):
    """
    Function to add products to cart object
    """

    cart = request.session.get('cart', {})

    cart[item_id] = 1

    request.session['cart'] = cart

    doodles = Doodles.objects.all()

    doodles_context = {
        'doodles': doodles,
    }

    print(request.session['cart'])

    return render (request, 'cart/cart.html', cart)