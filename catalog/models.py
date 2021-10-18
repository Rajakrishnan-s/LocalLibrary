from django.db import models
from django.urls import reverse

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Model representing a book, but not a specific copy i.e. A library can have a number of specific copies or instances of a given "Book" """
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author', on_delete = model.CASCADE) # "Author" as a string is used, as the Author model hasn't been defined yet
    summary = models.TextField(max_length = 1000, help_text='Enter a brief description of the book', blank=True)
    isbn = models.CharField(verbose_name='ISBN', max_length=13,
            unique = True,
            help_text = 'Type in the 13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
            )
    # ManyToManyField used because genre can contain many books.Books can cover many genres.
    genre = models.ManyToManyField(Genre, help_text= 'Select a genre')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)]) #self.id is the autocreated primary key