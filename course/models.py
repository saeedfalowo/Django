from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Course(models.Model):
	title	= models.CharField(max_length=120)
	content	= models.TextField(blank=True, null=True)
	# date	= models.DateField()
	def get_absolute_url(self):
		return reverse("courses:course-detail", kwargs={"my_id": self.id})
		# return reverse("articles2:articles2-detail", kwargs={"my_id": self.id})