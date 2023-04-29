from django.shortcuts import render, redirect
from main.models import Product, Categorys
from .forms import ProductForm, CategoryForm


def home(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		form.save()
	count = Product.objects.count()
	products = Product.objects.order_by('-pub_date')
	form = ProductForm()
	context = {
		'count':count,
		'form':form,
		'products':products
	}
	return render(request, 'control/index.html', context)

def categorys(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		form.save()
	count = Categorys.objects.count()
	categorys = Categorys.objects.all()
	form = CategoryForm()
	context = {
		'count':count,
		'form':form,
		'categorys':categorys
	}
	return render(request, 'control/categorys-control.html', context)

def search_admin(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		form.save()
	count = Product.objects.count()
	products = Product.objects.filter( name__icontains = request.GET.get('search_admin') )
	form = ProductForm()
	context = {
		'count':count,
		'form':form,
		'products':products
	}
	return render(request, 'control/index.html', context)

def search_category(request):
	if request.method == 'POST':
		form = CCategryForm(request.POST)
		form.save()
	count = Categorys.objects.count()
	categorys = Categorys.objects.filter( name__icontains = request.GET.get('search_admin') )
	form = CategoryForm()
	context = {
		'count':count,
		'form':form,
		'categorys':categorys
	}
	return render(request, 'control/categorys-control.html', context)

def edit(request, pid):
	product = Product.objects.get( id = pid )
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		form.save()
		return redirect('manage')
	form = ProductForm(instance=product)
	context = {
		'form':form,
	}
	return render(request, 'control/edit.html', context)

def remove(request, pid):
	product = Product.objects.get( id = pid )
	if request.method == 'POST':
		product.delete()
		return redirect('manage')

	context = {
		'product':product,
	}
	return render(request, 'control/remove.html', context)

def edit_category(request, cid):
	category = Categorys.objects.get( id = cid )
	if request.method == 'POST':
		form = CategoryForm(request.POST, instance=category)
		form.save()
		return redirect('categorys')
	form = CategoryForm(instance=category)
	context = {
		'form':form,
	}
	return render(request, 'control/edit-category.html', context)

def remove_category(request, cid):
	category = Categorys.objects.get( id = cid )
	if request.method == 'POST':
		category.delete()
		return redirect('categorys')

	context = {
		'category':category,
	}
	return render(request, 'control/categorys-remove.html', context)
