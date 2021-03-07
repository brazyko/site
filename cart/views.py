from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from parts.models import Product
from .models import *
from users.models import *
from .forms import ShippingForm
from .extrafiles import generate_order_id


def get_user_pending_order(request):
    order = Order.objects.filter(owner=request.user, order_status='INC')
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required()
def add_to_cart(request, **kwargs):
    part = Product.objects.filter(id = kwargs.get('item_id',"")).first()
    quantity = request.GET.get('quantity','')
    order_item, status = CartItem.objects.get_or_create(user=request.user,part = part,in_order = False)
    order_item.user = request.user
    order_item.quantity = quantity
    order_item.in_order = True
    order_item.save()
    user_order, status = Order.objects.get_or_create(owner=request.user,order_status='INC')
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
    return redirect(reverse('parts:partslist'))

@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = CartItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('shopping_cart:order_summary'))

@login_required()
def delete_from_cart_list(request, item_id):
    item_to_delete = CartItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('parts:partslist'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)

@login_required
def shipping_info(request):
    form = ShippingForm(request.POST, request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        form.order = get_user_pending_order(request)
        form.save()
        return redirect("shopping_cart:checkout")
    
    else:
    	form = ShippingForm(request.POST, request.FILES)
    context = {
    	'form':form,
    }
    return render(request,'deliver_data.html',context)

@login_required
def checkout(request):
    order = get_user_pending_order(request)
    order.order_status = 'ORD'  
    for order_item in order.items.all():
        order_item.in_order=True
        order_item.save()
        order_item.part.instock -= order_item.quantity
        order_item.part.save()
    order.save()
    return redirect(reverse('users:myprofile'))