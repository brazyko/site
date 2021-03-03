from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse
from cart.models import *

def admintools(request):
    if request.user.is_superuser:
        return render(request,'admintoolspage.html')
    else:
        return redirect(reverse('pagenotfound'))

def usermanagment(request):
    if request.user.is_superuser:
        all_users = User.objects.all()
    else:
        return redirect(reverse('pagenotfound'))
    context = {
        'all_users':all_users,
    }
    return render(request,'usermanagment.html',context)

def orders_administration(request):
    if request.user.is_superuser:
        orders = Order.objects.all().exclude(order_status="INC").order_by('-date_ordered')
    else:
        return redirect(reverse('pagenotfound'))
    context ={
        'orders':orders,
    }
    return render(request,'orders_administration.html',context)

def orders_shipping_administration(request):
    if request.user.is_superuser:
        orders_shipping_data = ShippingData.objects.all().order_by('-date_ordered')
    else:
        return redirect(reverse('pagenotfound'))
    context ={
        'orders_shipping_data':orders_shipping_data,
    }
    return render(request,'orders_shipping_administration.html',context)

def orders_shipping_administration_formed(request,ref):
    if request.user.is_superuser:
        order = Order.objects.all().filter(ref_code = ref).first()
        order.order_status = 'PRP'
        order.save()
        return redirect(reverse('admintools:orders_admin'))
    else:
        return redirect(reverse('pagenotfound'))

def orders_shipping_administration_confirm(request,ref):
    if request.user.is_superuser:
        order = Order.objects.all().filter(ref_code = ref).first()
        order.order_status = 'SHP'
        order.save()
        return redirect(reverse('admintools:orders_shipping_admin'))
    else:
        return redirect(reverse('pagenotfound'))