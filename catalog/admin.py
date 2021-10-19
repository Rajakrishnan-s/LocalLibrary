from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language,)

# Register and Define the admin class for Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Displays the following attributes in the list view in the admin site
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = ('BookInline',)
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )
    inlines = ("BookInstanceInline")#BookInstanceInline class is defined few lines below


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back')
        }),
    )

# An Inline model class for BookInstance, which can be used to declare inline models
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance   
    extra = 0

class BookInline(admin.TabularInline):
    model = Book
    extra = 0