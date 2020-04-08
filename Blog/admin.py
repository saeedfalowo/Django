from django.contrib import admin

# Register your models here.
from .models import Article
admin.site.register(Article)
# this is a relative import because admin.py and models.py are in the same module
# in the same product tree branch