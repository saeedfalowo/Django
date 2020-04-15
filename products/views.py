from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Import the Product class
from .models import  Product
from .forms import ProductForm, RawProductForm
# Create your views here.

def product_create_view(request):
	#obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None)#, instance=obj)
	# initial_data = {'title': "My intial data"}
	# form = ProductForm(request.POST or None, initial=initial_data)
	# form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
		return redirect('../')
	
	context = {
		'form': form
	}
	# return render(request, "product/detail.html", context)
	return render(request, "products/product_create.html", context)

# def product_create_view(request):
# 	if request.method == "POST"
# 		# print(request.GET)
# 		# print(request.POST)
# 		my_new_title = request.POST.get('title')
# 		print(my_new_title)
# 		# Product.objects.create(title=my_new_title)
# 	context = {}
# 	return render(request, "products/product_create_raw.html", context)

# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == "POST":
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			# Now the data is good
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)

# 	my_form = RawProductForm()
# 	context = {
# 		"form": my_form
# 	}
# 	return render(request, "products/product_create_djangoraw.html", context)

def dynamic_lookup_view(request,my_id):
	# obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product, id=my_id)
	# try:
	# 	obj = Product.objects.get(id=my_id)
	# except Product.DoesNotExist:
	# 	raise Http404

	context = {
		"object": obj
	}
	return render(request, "products/product_detail_url_routing.html", context)
	# return render(request, "products/product_detail_dynamic_url_linking.html", context)

# def product_detail_view(request):
# 	obj = Product.objects.get(id=1)
# 	# context = {
# 	# 	'title': obj.title,
# 	# 	'description': obj.description
# 	# }
# 	context = {
# 		'object': obj
# 	}
# 	# return render(request, "product/detail.html", context)
# 	return render(request, "products/product_detail.html", context)

def product_delete_view(request,my_id):
	obj = get_object_or_404(Product, id=my_id)
	# POST request
	if request.method == "POST":
		obj.delete() # confirming delete
		return redirect('../../')
	context = {
		"object": obj
	}
	return render(request, "products/product_detail_delete.html", context)


def product_list_view(request):
	queryset = Product.objects.all() # list of objects
	context = { "object_list": queryset }
	# return render(request, "products/product_detail_obj_list.html", context)
	return render(request, "products/product_detail_dynamic_url_linking.html", context)

"""def dynamic_url_lookup_view(request,my_id):
	# obj = Product.objects.get(id=my_id)
	obj = get_object_or_404(Product, id=my_id)
	# try:
	# 	obj = Product.objects.get(id=my_id)
	# except Product.DoesNotExist:
	# 	raise Http404

	context = {
		"object": obj
	}
	# return render(request, "products/product_detail_url_routing.html", context)
	return render(request, "products/product_detail_dynamic_url_linking.html", context)
"""