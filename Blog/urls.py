from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    BlogCreateView,
    BlogHomeView
    )

app_name = 'articles'
urlpatterns = [
    path('create', BlogCreateView, name='blog-create'),
    path('', BlogHomeView, name='article-list'),
    path('list', ArticleListView.as_view(), name='article-list'), # as_view turns it into a function based view
    path('<int:id>', ArticleDetailView.as_view(), name='article-detail'), # id=pk (primary field)
    path('art_create', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete', ArticleDeleteView.as_view(), name='article-delete'),
    # path('<int:my_id>/', dynamic_lookup_view, name='product'),
    # path('<int:my_id>/', dynamic_lookup_view, name='product'),
    # path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
]