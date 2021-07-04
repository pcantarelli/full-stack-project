from django.shortcuts import redirect, render
from doodles.models import Doodles

# Create your views here.

def cart(request):
    """
    Function to return a view of the cart page

    """
    cart = request.session.get('cart', {})
    doodles = Doodles.objects.all()
    cart_list = []

    # Exclude cart items from doodles list
    for key in cart.keys():
        cart_list.append(key)
    doodles = doodles.exclude(id__in=cart_list)

    context = {
        'doodles': doodles,
        'cart': cart,
    }
    print(doodles)
    return render (request, 'cart/cart.html', context)

def add_to_cart(request, item_id):
    """
    Function to add products to cart object
    """

    cart = request.session.get('cart', {})
    cart[item_id] = 1
    request.session['cart'] = cart

    return redirect('cart')