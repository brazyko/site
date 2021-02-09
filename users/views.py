from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 


def register(request):
    if request.method == "POST":
	    form = NewUserForm(request.POST)
	    if form.is_valid():
	    	user = form.save()
	    	login(user,request)
	    	messages.success(request, "Registration successful." )
	    	return redirect("users:login")
	    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    context={
		'register_form':form,
    }
    return render (request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.info(request, f"You are now logged in as {username}.")
                login(request,user)
                return redirect('users:myprofile')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    context={
        "login_form":form,
        }
    return render(request, "login.html", context)


def logout_user(request):
    print('logged out')
    logout(request)
    return redirect("users:login")

def profile(request):
    user = request.user
    context = {
        'user':user,
    }
    return render(request,'myprofile.html',context)