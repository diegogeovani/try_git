from django import forms

class ContactForm(forms.Form):	
	subject = forms.CharField(max_length = 80)
	message = forms.CharField(max_length = 300)
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required = False)
