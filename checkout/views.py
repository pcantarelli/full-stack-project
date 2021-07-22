import stripe
import json

from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings


from .forms import CheckoutForm
from cart.contexts import cart_items

from .models import Order, OrderLineItem
from doodles.models import Doodles
from custom.models import CustomWorkType, CustomSizes, CustomersFiles


# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    if item_data['product_type'] == 'doodle':
                        doodle = Doodles.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            doodle=doodle,
                            product_type=item_data['product_type'],
                            size=doodle.size,
                            lineitem_total=doodle.price
                        )
                        order_line_item.save()
                    elif item_data['product_type'] == 'custom':
                        print('work_type_id')
                        print(item_data['work_type_id'])
                        work_type = CustomWorkType.objects.get(id=item_data['work_type_id'])  
                        print('work_type')    
                        print(work_type)                     
                        customer_file = CustomersFiles.objects.get(id=item_data['customer_file_id'])                       
                        order_line_item = OrderLineItem(
                            order=order,
                            work_type=work_type,
                            product_type=item_data['product_type'],
                            size=item_data['size'],
                            customer_file=customer_file,
                            lineitem_total=item_data['custom_total_price']
                        )
                        order_line_item.save()
                except Exception as e:
                    messages.error(request, 
                        f'Error trying to create Order, please get in touch \
                        Message: {e}')
                    order.delete()
                    return redirect(reverse('cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_confirmed', args=[order.order_number]))
    else:

        if not cart:
            messages.error(request, 'No items on your cart yet')
            return redirect("/")

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


def order_confirmed(request, order_number):
    """
    Function to return template for successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    doodles = Doodles.objects.all()
    doodles = doodles.order_by('-updated_at')[:4]

    messages.success(request, f'Order processed successfully! \
        New tattoo on the way')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/order_confirmed.html'
    context = {
        'order': order,
        'doodles': doodles,
    }

    return render(request, template, context)