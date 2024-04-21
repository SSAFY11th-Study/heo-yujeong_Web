from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('nickname',)

class BookForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(user=user)
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'genre': forms.TextInput()
        }