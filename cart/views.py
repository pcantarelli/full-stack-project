from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib import messages
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
    return render (request, 'cart/cart.html', context)

def add_to_cart(request, item_id):
    """
    Function to add products to cart object
    """
    doodle = get_object_or_404(Doodles, pk=item_id)
    cart = request.session.get('cart', {})
    cart[item_id] = 1
    request.session['cart'] = cart
    messages.success(request, f'{doodle.name} added to your cart')

    return redirect('cart')


def remove_from_cart(request, item_id):
    """Function to remove products to cart object"""

    redirect_url = request.POST.get('redirect_url')

    try:
        doodle = get_object_or_404(Doodles, pk=item_id)
        cart = request.session.get('cart', {})


        cart.pop(item_id)
        messages.success(request, f'{doodle.name} removed sucessfuly')

        request.session['cart'] = cart
        return redirect('cart', status=200)

    except Exception as e:
        messages.error(request, f'Error trying to remove item: {e}')
        return redirect(redirect_url, status=500)
