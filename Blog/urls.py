from django.urls import path

from .views import (
	BlogHomeView,
	BlogCreateView,
	BlogDetailView,
	BlogDeleteView,
	BlogUpdateView
	)

app_name = 'articles'
urlpatterns = [
	path('', BlogHomeView, name='articles-home'),
	path('create', BlogCreateView, name='articles-create'),
	path('<int:my_id>/', BlogDetailView, name='articles-detail'),
	path('<int:my_id>/delete/', BlogDeleteView, name='articles-delete'),
	path('<int:my_id>/update/', BlogUpdateView, name='articles-create'),
]