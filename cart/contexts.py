

def cart_items(request):

    cart_items = []
    cart_total = 0
    cart_items_count = 0

    context = { 
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_items_count': cart_items_count,
    }

    return context