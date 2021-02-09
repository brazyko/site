from  django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.detail import DetailView
from .models import Product,Category
from django.contrib import messages

from cart.models import Order,OrderItem
# Create your views here.

def partslist(request):
    parts = Product.objects.all()
    order_items = OrderItem.objects.all()
    order_parts = []
    for item in order_items:
        order_parts.append(item.part)
    print(order_parts)
    context = {
        'parts':parts,
        'order_items':order_items,
        'order_parts':order_parts,
    }
    return render(request,'parts_list.html',context)

class partdetail(DetailView):
    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Product, id=kwargs['id'])
        context = {
            'part':object,
        }
        return render(request,'part_detail_view.html',context)


def partSearch(request):
    search_query = request.GET.get('partnumber','')
    if search_query:
        parts_cross  = Product.objects.all()
        part = parts_cross.filter(original = search_query).first()
        if part != None:
            parts_cross = Product.objects.filter(cross = part.cross)
        else:
            parts_cross = None
            print('not extsts')
            messages.error(request, 'Ми не змогли знайти деталей з таким номером')
    context = {
        'part':part,
        'parts_cross':parts_cross,
    }
    return render(request,'parts_search.html',context)