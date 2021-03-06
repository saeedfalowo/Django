from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
	title	= forms.CharField(
		# widget=forms.TextInput(
		# 	attrs={
		# 	"placeholder": "Whats your title?"
		# 	}
		# 	)
		)
	content	= forms.CharField(
		# widget=forms.Textarea(
		# 	attrs={
		# 	"placeholder": "What's on your mind...",
		# 	"rows": 20,
		# 	"cols": 120
		# 	}
		# 	)
		)
	# date		= forms.DateField(initial=date.today)
	# active = forms.BooleanField()
	class Meta:
		model	= Course
		fields	= ['title', 'content']
