from django.db import models

# Create your models here.
class Product(models.Model):
	# title 		= models.TextField()
	title 		= models.CharField(max_length=120) 
	# CharField limits the title length
	description = models.TextField(blank=True, null=True) # If we dont want a description
	price 		= models.DecimalField(decimal_places=2, max_digits=10000) # 2 because it is a currency unit
	summary     = models.TextField(blank=False, null=False)
	# blank=True, null=False  makes the 'Summary' not bold and not essential to be filled before saving in server admin
	# blank=False, null=False  makes the 'Summary' bold and essential to be filled before saving in server admin
	# 'blank' has to do with how the field is rendered
	# 'null' has to do with the database
	# 'blank=False' means it is required
	# 'null=False' means the database can be empty
	featured    = models.BooleanField()
	# null=True means, all the old values should be left empty in the database