import stripe
import json

from django.shortcuts import redirect, render, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings


from .forms import CheckoutForm
from cart.contexts import cart_items

from .models import Order, OrderLineItem
from doodles.models import Doodles
from custom.models import CustomWorkType, CustomSizes, CustomersFiles
from users.models import UserProfile
from users.forms import ProfileForm


@require_POST
def cache_checkout_data(request):
    """ """

    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            (
                "Sorry, your payment cannot be "
                "processed right now. Please try "
                "again later."
            ),
        )
        return HttpResponse(content=e, status=400)


# Create your views here.
def checkout(request):
    """ """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get("cart", {})

    if request.method == "POST":

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "county": request.POST["county"],
        }

        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    if item_data["product_type"] == "doodle":
                        doodle = Doodles.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            doodle=doodle,
                            product_type=item_data["product_type"],
                            size=doodle.size,
                            lineitem_total=doodle.price,
                        )
                        order_line_item.save()
                    elif item_data["product_type"] == "custom":
                        work_type = CustomWorkType.objects.get(
                            id=item_data["work_type_id"]
                        )
                        customer_file = CustomersFiles.objects.get(
                            id=item_data["customer_file_id"]
                        )
                        order_line_item = OrderLineItem(
                            order=order,
                            work_type=work_type,
                            product_type=item_data["product_type"],
                            size=item_data["size"],
                            customer_file=customer_file,
                            lineitem_total=item_data["custom_total_price"],
                        )
                        order_line_item.save()
                except Exception as e:
                    messages.error(
                        request,
                        f"Error trying to create Order, please get in touch \
                        Message: {e}",
                    )
                    order.delete()
                    return redirect(reverse("cart"))

            # Save the info to the user's profile if all is well
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("order_confirmed", args=[order.order_number]))
    else:
        if not cart:
            messages.error(request, "No items on your cart yet")
            return redirect("/")

        checkout_form = CheckoutForm()
        template = "checkout/checkout.html"

        cart_info = cart_items(request)
        cart_price_total = cart_info["cart_price_total"]
        stripe_total = round(cart_price_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                checkout_form = CheckoutForm(
                    initial={
                        "full_name": profile.user.get_full_name(),
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "country": profile.default_country,
                        "postcode": profile.default_postcode,
                        "town_or_city": profile.default_town_or_city,
                        "street_address1": profile.default_street_address1,
                        "street_address2": profile.default_street_address2,
                        "county": profile.default_county,
                    }
                )
            except UserProfile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, ("Stripe public key not found."))

    context = {
        "checkout_form": checkout_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def order_confirmed(request, order_number):
    """
    Function to return template for successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)
    doodles = Doodles.objects.all()
    doodles = doodles.order_by("-updated_at")[:4]

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = ProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order processed successfully! \
        New tattoo on the way",
    )

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/order_confirmed.html"
    context = {
        "order": order,
        "doodles": doodles,
    }

    return render(request, template, context)
