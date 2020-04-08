from django.db import models
from django.urls import reverse
# from datetime import date

# Create your models here.
class Article(models.Model):
	title		= models.CharField(max_length=120) 
	content		= models.TextField(blank=True, null=True) # If we dont want a description
	active		= models.BooleanField(default=False)
	# date		= models.DateField(default=date.today)
	
	# blank=True, null=False  makes the 'Summary' not bold and not essential to be filled before saving in server admin
	# blank=False, null=False  makes the 'Summary' bold and essential to be filled before saving in server admin
	# 'blank' has to do with how the field is rendered
	# 'null' has to do with the database
	# 'blank=False' means it is required
	# 'null=False' means the database can be empty
	# null=True means, all the old values should be left empty in the database

	def get_absolute_url(self):
		# return f"/products/{self.id}"
		#return f"/blog/create" # "f" denotes f string or string substitution
		return reverse("articles:article-detail", kwargs={"id":self.id})
		# "my_id" refers to the integer id declared in products/<int:my_id>/
		# within the url patterns url with the name, product.
		# self refers to the instance of the object
		# id refers to the id that is built into it