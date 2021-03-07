from  django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from .models import Product,Category
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.models import *
from django.db.models import Q
# Create your views here.

def partslist(request):
    parts = Product.objects.all()
    my_order = []
    ordered_items = []
    if request.user.is_authenticated:
        my_order = Order.objects.filter(owner = request.user,order_status='INC').first()
        ordered_items = []
        if my_order:
            for item in my_order.items.all():
                ordered_items.append(item.part)

    page_number = request.GET.get('page',1)
    paginator = Paginator(parts,12)
    page_obj = paginator.get_page(page_number)
    try:
    	parts = paginator.page(page_number)
    except PageNotAnInteger:
        parts = paginator.page(1)
    except EmptyPage:
        parts = paginator.page(paginator.num_pages)


    context = {
        'parts':parts,
        'my_order':my_order,
        'ordered_items':ordered_items,
        'page_obj': page_obj,
    }
    return render(request,'parts_list.html',context)

class partdetail(DetailView):
    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Product, id=kwargs['id'])
        my_order = []
        ordered_items = []
        if request.user.is_authenticated:
            my_order = Order.objects.filter(owner = request.user,order_status='INC').first()
            ordered_items = []
            if my_order:
                for item in my_order.items.all():
                    ordered_items.append(item.part)
        context = {
            'part':object,
            'my_order':my_order,
            'ordered_items':ordered_items,
        }
        return render(request,'part_detail_view.html',context)


def partSearch(request):
    search_query = request.GET.get('partnumber','')
    my_order = Order.objects.all().filter(owner= request.user).filter(order_status = 'INC').first()
    if search_query:
        parts = Product.objects.filter(Q(original=search_query) | Q(index=search_query))
        if parts:
            parts_cross = parts.first()
            parts_cross = Product.objects.filter(original = parts_cross.original)
        else:
            parts_cross = None
    context = {
        'parts':parts,
        'my_order':my_order,
        'parts_cross':parts_cross,
    }
    return render(request,'parts_search.html',context)