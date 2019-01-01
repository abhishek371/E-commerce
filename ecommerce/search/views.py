from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product


# Create your views here.

class SearchProductView(ListView):
	template_name="search/view.html"


	def get_queryset(self,*args,**kwargs):
		request = self.request
		print(request.GET)
		query = request.GET.get('q',None)
		if query is not None:
			lookups = Q(title__icontains=query)|Q(description__icontains=query)|Q(price__icontains=query)
			return Product.objects.filter(lookups)
		return Product.objects.none()
		return Product.objects.filter(title__icontains='shirt')