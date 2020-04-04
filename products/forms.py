from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(
		label='Newerer Title',
		widget=forms.TextInput(
			attrs={
			"placeholder": "Whats your title?"
			}
			)
		)
	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
			"class": "new-class-name two",
			"placeholder": "You dont really have to type anything, you can skip if you want...",
			"id":"my-id-for-textarea",
			"rows": 20,
			"cols": 120
			}
			)
		)

	price = forms.DecimalField(initial=0.99)
	email = forms.EmailField(widget=forms.TextInput(
		attrs={"placeholder": "anything@something.somethingelse"}))
	class Meta:
		model 	= Product
		fields	= ['title','description','price']

	def clean_title(self, *args, **kwargs):
		# get the title
		title = self.cleaned_data.get("title")
		# to check if the required char combination, "cfe" exists in title
		if "CFE" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args, **kwargs):
		# get the email
		title = self.cleaned_data.get("email")
		# to check if the required char combination, "cfe" exists in title
		# if not "@" in email:
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email

class RawProductForm(forms.Form):
	title 		= forms.CharField(
		label='Newerer Title',
		widget=forms.TextInput(
			attrs={
			"placeholder": "Whats your title?"
			}
			)
		)
	description = forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
			"class": "new-class-name two",
			"placeholder": "You dont really have to type anything, you can skip if you want...",
			"id":"my-id-for-textarea",
			"rows": 20,
			"cols": 120
			}
			)
		)
	price		= forms.DecimalField(initial=0.99)