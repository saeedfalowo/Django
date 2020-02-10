from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# *args    = arguments
# **kwargs = keyword arguments
def home_view(request,*args, **kwargs):
	print(args,kwargs)
	print(request.user)
	# the *args and **kwargs print out (<WSGIRequest: GET '/'>,) {}
	# request.user prints out the user accessing the server, saeed
	# When accessed from a different browser, incognito browser or maybe after logging out
	# request.user prints out the user accessing the server, AnonymousUser


	# This function will return an HTML code that will return "Hello World"
	# "<h1>Hello World</h1>" = string of HTML code, not HTML code
	# HttpResponse will execute the string as an HTML code
	# return HttpResponse("<h1>Hello World</h1>")
	return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
	# This function will return an HTML code that will return "Hello World"
	# "<h1>Hello World</h1>" = string of HTML code, not HTML code
	# HttpResponse will execute the string as an HTML code
	# return HttpResponse("<h1>You're it!</h1>")

	my_context = {
		"my_text"	: "This is my contact",
		"my_number"	: 12369,
		"my_list"	: [123,456,789]

	}
	return render(request, "contact.html",my_context)
