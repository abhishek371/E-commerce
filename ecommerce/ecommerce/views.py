from django.http import HttpResponse
from django.shortcuts import render


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
	return render(request,'home.html',context)

