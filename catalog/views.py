from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Book, Author, BookInstance

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin # for adding login required constraint to the view classes

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 3

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book

class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author