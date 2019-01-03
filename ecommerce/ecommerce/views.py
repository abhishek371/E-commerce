from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm


def home_page(request):
	context ={
		"l1":"Cart",
		"l2":"Pay"
	}
	return render(request,'home.html',context)

def about_page(request):
	context ={
		"l1":"Address",
		"l2":"Contact"
	}
	if request.method=="POST":
		print(request.POST.get('fullname'))
	return render(request,'contact/view.html',context)



def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
        "form": form
    }
	print("User logged in")
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username  = form.cleaned_data.get("username")
		password  = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
		    #print(request.user.is_authenticated())
		    login(request, user)
		    # Redirect to a success page.
		    #context['form'] = LoginForm()
		    return redirect("/")
		else:
			# Return an 'invalid login' error message.
		    print("Error")

	return render(request,'auth/login.html',context)

def register_page(request):
	User = get_user_model()
	form = RegisterForm(request.POST or None)
	context = {
        "form": form
    }
	if form.is_valid():
		print(form.cleaned_data)
		username  = form.cleaned_data.get("username")
		email  = form.cleaned_data.get("email")
		password  = form.cleaned_data.get("password")
		new_user  = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request,'auth/register.html',context)

