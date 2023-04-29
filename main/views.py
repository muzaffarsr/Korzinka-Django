from django.shortcuts import render
from .models import Product, Categorys


def home(request):
	products = Product.objects.order_by('-pub_date')
	categorys = Categorys.objects.all()
	context = {
		'products':products,
		'categorys':categorys,
	}
	return render(request, 'main/index.html', context)

def product(request, pid):
	product = Product.objects.get( id = pid )
	context = {
		'p':product,
	}
	return render(request, 'main/product.html', context)

def accept(request):
	return render(request, 'main/accept.html')

def thanks(request):
	return render(request, 'main/thanks.html')

def search(request):
	products = Product.objects.filter( name__icontains = request.GET.get('search') )
	categorys = Categorys.objects.all()
	context = {
		'products':products,
		'categorys':categorys,
	}
	return render(request, 'main/index.html', context)

def category(request, cid):
	products = Product.objects.filter( category = cid )
	categorys = Categorys.objects.all()
	context = {
		'products':products,
		'categorys':categorys,
	}
	return render(request, 'main/index.html', context)