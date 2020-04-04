from django.shortcuts import render

# Import the Product class
from .models import  Product
from .forms import ProductForm, RawProductForm
# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description
	# }
	context = {
		'object': obj
	}
	# return render(request, "product/detail.html", context)
	return render(request, "products/product_detail.html", context)

def product_create_view(request):
	obj = Product.objects.get(id=1)
	form = ProductForm(request.POST or None, instance=obj)
	# initial_data = {'title': "My intial data"}
	# form = ProductForm(request.POST or None, initial=initial_data)
	# form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	
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
