from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Article(models.Model):
	title	= models.CharField(max_length=120)
	content	= models.TextField(blank=True, null=True)
	# date	= models.DateField()
	def get_absolute_url(self):
		return reverse("articles:articles-detail", kwargs={"my_id": self.id})