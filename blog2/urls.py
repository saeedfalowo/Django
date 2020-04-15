from django.urls import path

from .views import (
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView
	)

app_name = 'articles2'
urlpatterns = [
	path('', ArticleListView.as_view(), name='articles2-home'), # as_view turns it into a function based view
	path('<int:my_id>/', ArticleDetailView.as_view(), name='articles2-detail'), # id=pk (primary field)
	path('create/', ArticleCreateView.as_view(), name='articles2-create'),
	path('<int:my_id>/update/', ArticleUpdateView.as_view(), name='articles2-update'),
	path('<int:my_id>/delete/', ArticleDeleteView.as_view(), name='articles2-delete'),
	]

