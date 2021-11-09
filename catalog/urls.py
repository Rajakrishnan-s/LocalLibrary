from django.urls import path
from . import views

app_name = 'catalog' # to avoid namesapace collision from other apps, while referring in the project scope

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('allborrowed/', views.AllBorrowedBooksListView.as_view(), name='all_borrowed'),
]
# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]