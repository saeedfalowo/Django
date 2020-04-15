from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def BlogHomeView(request):
	queryset = Article.objects.all() # list of objects
	context = { "object_list": queryset }
	return render(request, "articles/articles_landingpage.html", context)

def BlogCreateView(request):
	#model = Article
	form = ArticleForm(request.POST or None)
	print('Is form valid? ', form.is_valid())
	print('The form request? ', request.method)
	print(form.errors)
	if form.is_valid():
		form.save()
		print(form.cleaned_data)
		form = ArticleForm()
		return redirect('/blog')
	context = {
		'form': form
		}
	return render(request, "articles/articles_create.html", context)

def BlogDetailView(request,my_id):
	#obj = Article.objects.get(id=my_id)
	obj = get_object_or_404(Article, id=my_id)
	context = {
		'object': obj
	}
	return render(request, "articles/articles_detail.html", context)

def BlogDeleteView(request, my_id):
	#obj = Article.objects.get(id=my_id)
	obj = get_object_or_404(Article, id=my_id)
	if request.method == "POST":
		obj.delete()
		return redirect('/blog/')
	context = {
		"object": obj
		}
	return render(request, "articles/articles_delete.html", context)

def BlogUpdateView(request, my_id=id):
    obj = get_object_or_404(Article, id=my_id)
    form = ArticleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')
    context = {
        'form': form
    }
    return render(request, "articles/articles_create.html", context)