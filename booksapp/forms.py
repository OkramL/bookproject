from django import forms
import bookproject.settings
from .models import *


class LanguageCreateForm(forms.ModelForm):
    language = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter a new language name',
        'class': 'form-control',
        'autofocus': True,
    }))

    class Meta:
        model = Language
        fields = ['language']  # '__all__'


class AuthorCreateForm(forms.ModelForm):
    # https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django
    # https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-2'
            # Can comment
            # visible.field.widget.attrs['placeholder'] = visible.field.label

        self.fields['firstname'].widget.attrs['autofocus'] = True

        self.fields['birth'].widget = forms.widgets.DateInput(attrs={
            'type': 'date',
            'class': 'form-control mb-2'
        })

    class Meta:
        model = Author
        fields = '__all__'


class BookCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            # Add a CSS class to all visible form fields
            visible.field.widget.attrs['class'] = 'form-control mb-2'

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['book_published_year'].widget = forms.widgets.TextInput(attrs={
            'type': 'number',
            'class': 'form-control mb-2',
            'min': 1900,
            'step': 1,
        })

    class Meta:
        model = Book
        fields = '__all__'


# class LanguageUpdateForm(forms.ModelForm):
