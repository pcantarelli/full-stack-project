from django.shortcuts import get_object_or_404
from doodles.models import Doodles

def cart_items(request):

    cart_items = []
    cart_price_total = 0
    cart_items_count = 0
    cart_time_total = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        item_obj = get_object_or_404(Doodles, pk=item_id)
        cart_price_total += item_obj.price
        cart_items_count += 1
        cart_time_total += item_obj.time_to_complete
        cart_items.append({
            'item_id': item_id,
            'item_obj': item_obj,
        })

    context = { 
        'cart_items': cart_items,
        'cart_price_total': cart_price_total,
        'cart_items_count': cart_items_count,
        'cart_time_total': cart_time_total,
    }

    return context