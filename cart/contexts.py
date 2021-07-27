from django.shortcuts import get_object_or_404
from doodles.models import Doodles
from custom.models import CustomWorkType


def cart_items(request):

    cart_items = []
    cart_price_total = 0
    cart_items_count = 0
    cart = request.session.get("cart", {})

    for item_id, item_data in cart.items():
        if item_data["product_type"] == "doodle":
            item_obj = get_object_or_404(Doodles, pk=item_id)
            cart_price_total += float(item_obj.price)
            cart_items_count += 1
            cart_items.append(
                {
                    "item_id": item_id,
                    "item_obj": item_obj,
                }
            )
        elif item_data["product_type"] == "custom":
            cart_price_total += item_data["custom_total_price"]
            work_type = get_object_or_404(
                CustomWorkType, work_type=item_data["work_type"]
            )
            item_data["work_type_id"] = work_type.id
            cart_items_count += 1
            cart_items.append(
                {
                    "item_id": item_id,
                    "item_obj": item_data,
                }
            )

    context = {
        "cart_items": cart_items,
        "cart_price_total": cart_price_total,
        "cart_items_count": cart_items_count,
    }

    return context
