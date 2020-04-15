from django.urls import path

from .views import (
	CourseHome,
	CourseView,
	CourseCreateView,
	CourseUpdateView,
	CourseDeleteView
	)

app_name = 'courses'
urlpatterns = [
	path('', CourseHome.as_view(), name='course-home'), # as_view turns it into a function based view
	path('<int:my_id>/', CourseView.as_view(), name='course-detail'), # id=pk (primary field)
	path('create/', CourseCreateView.as_view(), name='course-create'),
	path('<int:my_id>/update/', CourseUpdateView.as_view(), name='course-update'),
	path('<int:my_id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
	]