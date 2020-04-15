from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import(
	CreateView, DetailView, ListView,
	UpdateView, DeleteView
	)

# Create your views here.
class ArticleListView(ListView):
	template_name = 'articles2/articles2_landingpage.html'
	queryset = Article.objects.all()
	# ListView means it will look for <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):
	template_name = 'articles2/articles2_detail.html'
	#queryset = Article.objects.all()

	# we can use this function to use the article id instead of pk
	def get_object(self):
		id_ = self.kwargs.get("my_id")
		return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
	template_name = 'articles2/articles2_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all() # <blog>/<modelname>_list.html
	#success_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	def get_success_url(self):
		return '/blog2'

class ArticleUpdateView(UpdateView):
	template_name = 'articles2/articles2_create.html'
	form_class = ArticleModelForm
	# queryset = Article.objects.all() # <blog>/<modelname>_list.html

	def get_object(self):
		id_ = self.kwargs.get("my_id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'articles2/articles2_delete.html'
	#queryset = Article.objects.all()
	def get_object(self):
		id_ = self.kwargs.get("my_id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('articles2:articles2-home')