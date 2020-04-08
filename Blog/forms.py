from django import forms
from datetime import date
from .models import Article

class ArticleForm(forms.Form):
	class Meta:
		model 	= Article
		# fields	= ['title','content','date']
		fields	= ['title','content','active']

class ArticleModelForm(forms.ModelForm):
	class Meta:
		model 	= Article
		fields	= ['title','content','active']
		# fields	= ['title','content','date']

class RawBlogForm(forms.Form):
	title 		= forms.CharField(
		widget=forms.TextInput(
			attrs={
			"placeholder": "Whats your title?"
			}
			)
		)
	content = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
			"placeholder": "What's on your mind...",
			"rows": 20,
			"cols": 120
			}
			)
		)
	# date		= forms.DateField(initial=date.today)
	active = forms.BooleanField()