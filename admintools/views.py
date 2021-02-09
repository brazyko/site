from django.shortcuts import render

from django.contrib.auth.models import User
# Create your views here.

def admintools(request):
    return render(request,'admintoolspage.html')


def usermanagment(request):
    all_users = User.objects.all()
    context = {
        'all_users':all_users,
    }
    return render(request,'usermanagment.html',context)