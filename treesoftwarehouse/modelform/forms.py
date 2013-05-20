from django.forms import ModelForm
from modelform.models import Author, Book

class AuthorForm(ModelForm):
	class Meta:
		model =  Author
		fields = ['name', 'title', 'birth_date']
	
		
class BookForm(ModelForm):
	class Meta:
		model =  Book
		fields = ['name', 'authors']
