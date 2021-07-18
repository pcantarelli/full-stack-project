import stripe

from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.conf import settings


from .forms import CheckoutForm
from cart.contexts import cart_items

# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})

    if not cart:
        messages.error('No items on your cart yet')
        return redirect(reverse('/'))
    
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'

    cart_info = cart_items(request)
    cart_price_total = cart_info['cart_price_total']
    stripe_total = round(cart_price_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key not found.'))

    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)