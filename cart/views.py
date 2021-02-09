from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from parts.models import Product
from .models import *
from users.models import *

from .extrafiles import generate_order_id

def get_user_pending_order(request):
    order = Order.objects.filter(owner=request.user, order_status='ORD')
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required()
def add_to_cart(request, **kwargs):
    part = Product.objects.filter(id = kwargs.get('item_id',"")).first()
    quantity = request.GET.get('quantity','')
    order_item, status = OrderItem.objects.get_or_create(part = part)
    order_item.quantity = quantity
    order_item.in_order = True
    order_item.save()
    user_order, status = Order.objects.get_or_create(owner=request.user)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request,'Товар успішно додано в корзину!')
    return redirect(reverse('parts:partslist'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('shopping_cart:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)