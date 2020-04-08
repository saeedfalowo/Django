from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
	CreateView, DetailView, ListView,
	UpdateView, DeleteView
	)

from .forms import RawBlogForm, ArticleModelForm

from .models import Article
# Create your views here.

class ArticleListView(ListView):
	# template_name = 'articles/article_list.html'
	queryset = Article.objects.all()
	# ListView means it will look for <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	#queryset = Article.objects.all()

	# we can use this function to use the article id instead of pk
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
	template_name = 'articles/blog_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all() # <blog>/<modelname>_list.html

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleUpdateView(UpdateView):
	template_name = 'articles/blog_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all() # <blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'
	#queryset = Article.objects.all()
	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('articles:article-list')


def BlogHomeView(request):
	#queryset = Article.objects.all() # list of objects
	#context = { "object_list": queryset }
	return render(request, "articles/article_list.html", {})#context)


def BlogCreateView(request):
	my_form = RawBlogForm()
	print(request.method)
	# if request.method == "POST":
	# 	my_form = RawBlogForm(request.POST)
	# 	if my_form.is_valid():
	# 		# Now the data is good
	# 		print(my_form.cleaned_data)
	# 		Blog.objects.create(**my_form.cleaned_data)
	# 	else:
	# 		print(my_form.errors)

	my_form = RawBlogForm(request.POST)
	print(my_form.is_valid())
	if my_form.is_valid():
		# Now the data is good
		print(my_form.cleaned_data)
		Blog.objects.create(**my_form.cleaned_data)
	else:
		print(my_form.errors)

	my_form = RawBlogForm()
	context = {
		"form": my_form
	}
# 	return render(request, "products/product_create_djangoraw.html", context)
	# return render(request, "templates/blog_home.html", context)
	return render(request, "articles/blog_create.html", context)