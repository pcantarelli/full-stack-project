from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from .forms import CheckoutForm
from .models import Order, OrderLineItem

# Create your views here.
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error('No items on your cart yet')
        return redirect(reverse('/'))
    
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    
    context = {
        'checkout_form': checkout_form,
    }

    return render(request, template, context)