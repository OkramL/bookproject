from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                  CreateView, UpdateView,
                                  DetailView, DeleteView)
from django.urls import reverse_lazy
from .forms import *  # All created forms
from .models import *  # All created models


# Create your views here.
class HomeView(TemplateView):
    template_name = 'booksapp/index.html'


class CountryListView(ListView):
    # template_name = 'booksapp/country_list.html'
    model = Country
    # order result by country field name
    queryset = Country.objects.order_by('country')
    context_object_name = 'countries'  # object_list is default


class LanguageListView(ListView):
    # template language_list.html,
    # context_object_name is object_list
    model = Language
    queryset = Language.objects.order_by('language')


class AuthorListView(ListView):
    model = Author


class BookListView(ListView):
    model = Book


class CountryCreateView(CreateView):
    model = Country
    fields = '__all__'  # All fields from model
    success_url = reverse_lazy('booksapp:country_list')


class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageCreateForm
    success_url = reverse_lazy('booksapp:language_list')


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    success_url = reverse_lazy('booksapp:author_list')


class BookCreateView(CreateView):
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('booksapp:book_list')


class CountryUpdateView(UpdateView):
    template_name = 'booksapp/country_form_update.html'
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('booksapp:country_list')

    def form_valid(self, form):
        # Additional checks
        return super().form_valid(form)


class LanguageUpdateView(UpdateView):
    template_name = 'booksapp/language_form_update.html'
    model = Language
    form_class = LanguageCreateForm
    success_url = reverse_lazy('booksapp:language_list')

    def form_valid(self, form):
        # Additional checks
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    template_name = 'booksapp/author_form_update.html'
    model = Author
    form_class = AuthorCreateForm
    success_url = reverse_lazy('booksapp:author_list')

    def form_valid(self, form):
        # Additional checks
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    # template_name = 'booksapp/book_form_update.html'
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('booksapp:book_list')

    def form_valid(self, form):
        # Additional checks
        return super().form_valid(form)