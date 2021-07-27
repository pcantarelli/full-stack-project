import uuid
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.contrib import messages
from doodles.models import Doodles
from custom.models import CustomWorkType, CustomSizes, CustomersFiles


# Create your views here.

def cart(request):
    """
    Function to return a view of the cart page

    """
    cart = request.session.get('cart', {})
    doodles = Doodles.objects.all()
    doodles_in_cart_list = []

    # Exclude cart items from doodles list
    for item_id, item_data in cart.items():
        if item_data['product_type'] == 'doodle':
            doodles_in_cart_list.append(item_id)

    doodles = doodles.exclude(id__in=doodles_in_cart_list)
    doodles = doodles[:4]

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
    cart[item_id] = {
        'product_type': 'doodle',
        'quantity': 1
        }
    request.session['cart'] = cart
    messages.success(request, f'{doodle.name} added to your cart')

    return redirect('cart')


def remove_from_cart(request, item_id):
    """Function to remove products to cart object"""

    try:
        cart = request.session.get('cart', {})
        cart_item = cart[item_id]
        cart.pop(item_id)

        if cart_item['product_type'] == 'doodle':
            doodle = get_object_or_404(Doodles, pk=item_id)
            messages.success(request, f'{doodle.name} removed sucessfuly')
        else:
            work_type = cart_item['work_type']
            messages.success(request, f'Custom {work_type} removed sucessfuly')

        request.session['cart'] = cart
        return redirect('cart')

    except Exception as e:
        messages.error(request, f'Error trying to remove item: {e}')
        return redirect('cart')

def add_custom_to_cart(request):
    """
    Function to add custom product to cart object
    """
    
    cart = request.session.get('cart', {})
    total_custom_on_cart = 0

    for item_id, item_data in cart.items(): # Check how many custom products are in the cart
        if item_data['product_type'] == 'custom':
            total_custom_on_cart += 1

    item_id = f'C_{total_custom_on_cart + 1}'
    work_type = request.POST.get('work_type')
    size = float(request.POST.get('size'))
    custom_total_price = float(request.POST.get('total_price'))
    new_customer_file = CustomersFiles(customer_file=request.FILES['user_image'])
    new_customer_file.save()
    customer_file_id = new_customer_file.id
    cart[item_id] = {
        'product_type': 'custom',
        'work_type': work_type,
        'size': size,
        'quantity': 1,
        'customer_file_id': customer_file_id,
        'custom_total_price': custom_total_price,
        }
    request.session['cart'] = cart
    messages.success(request, f'Custom tattoo added to your cart')

    return redirect('cart')