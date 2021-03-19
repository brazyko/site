from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from parts.models import Product
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

class PartsManage(ListView):
    model = Product
    paginate_by = 40
    template_name = 'manage_parts.html'


class CreatePart(CreateView):
    model = Product
    fields = ['producer','index','description','original','instock','price']
    template_name = 'manual_create_part.html'
    def get_success_url(self):
        return reverse('admintools:manage-parts')

class DeletePart(DeleteView):
    model = Product
    template_name ='product_confirm_delete.html'
    def get_success_url(self):
        return reverse('admintools:manage-parts')

    def get_object(self):
    	id = self.kwargs.get("id")
    	return get_object_or_404(Product,id=id)

class UpdatePart(UpdateView):
    model = Product
    fields = "__all__"
    template_name = 'update.html'

    def get_object(self):
    	id = self.kwargs.get("id")
    	return get_object_or_404(Product,id=id)
    
    def get_success_url(self):
        return reverse('admintools:manage-parts')