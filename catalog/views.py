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

class LoanedBooksByUserListView(LoginRequiredMixin,generic. ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return (BookInstance.objects
        .filter(borrower=self.request.user)
        .filter(status__exact='o')
        .order_by('due_back'))

from django.contrib.auth.mixins import PermissionRequiredMixin
class AllBorrowedBooksListView(LoginRequiredMixin,PermissionRequiredMixin,generic. ListView):
    """GCBV listing all books currently borrowed by all users"""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10
    permission_required = ['catalog.can_mark_returned']
    def get_queryset(self):
        return(BookInstance.objects
        .filter(status__exact = 'o')
        .order_by('due_back'))