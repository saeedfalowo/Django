from django.shortcuts import render, reverse,get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course

# Create your views here.

class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('my_id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 

# BASE VIEW CLass = VIEW
class CourseHome(View):
	template_name = "courses/course_landingpage.html"
	queryset = Course.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request, *args, **kwargs):
		context = {'object_list': self.get_queryset()}
		return render(request, self.template_name, context)

class CourseCreateView(View):
	template_name = "courses/course_create.html"

	# GET METHOD
	def get(self, request, *args, **kwargs):
		form = CourseModelForm() # default=='GET' so leave empty
		context = {'form': form}
		return render(request, self.template_name, context)

	# POST METHOD
	def post(self, request, *args, **kwargs):
		form = CourseModelForm(request.POST)
		if form.is_valid():
			form.save()
			form = CourseModelForm() # This re-initialize the actual form clearing the input fields
			return redirect('../')
		context = {'form': form}
		# This will grab the form data to be stored in the database
		return render(request, self.template_name, context)

class CourseView(View):
	template_name = "courses/course_detail.html"
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		id = self.kwargs.get('my_id') # my_id defined in url path in urls.py
		# path('<int:my_id>/', CourseView.as_view(), name='course-detail')
		if id is not None:
			obj = get_object_or_404(Course,id=id)
			context['object'] = obj
		return render(request, self.template_name, context)

# class CourseView(CourseObjectMixin, View):
#     template_name = "courses/course_detail.html" # DetailView
#     def get(self, request, id=None, *args, **kwargs):
#         # GET method
#         context = {'object': self.get_object()}
#         return render(request, self.template_name, context)

class CourseUpdateView(View):
	# template_name = "courses/course_update.html"
	template_name = "courses/course_create.html"

	def get_object(self):
		id_ = self.kwargs.get("my_id")
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id_)
			return obj

	# GET METHOD
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()

		if obj is not None:
			form = CourseModelForm(instance=obj)
			context['object'] = obj
			context['form'] = form
			return render(request, self.template_name, context)

	# POST METHOD
	def post(self, request, *args, **kwargs):
		context = {}
		obj = self.get_object()

		if obj is not None:
			form = CourseModelForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
				return redirect('../../')
			context['object'] = obj
			context['form'] = form
			return render(request, self.template_name, context)

class CourseDeleteView(View):
	template_name = "courses/course_delete.html"

	def get_object(self):
		id_ = self.kwargs.get("my_id")
		obj = None
		if id is not None:
			obj = get_object_or_404(Course, id=id_)
			return obj

	# GET METHOD
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()

		if obj is not None:
			context['object'] = obj
			return render(request, self.template_name, context)

	# POST METHOD
	def post(self, request, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = None
			# return redirect('/course/')
			return redirect('../../')

		return render(request, self.template_name, context)