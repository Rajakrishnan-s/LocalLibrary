from django.urls import path
from . import views

app_name = 'catalog' # to avoid namesapace collision from other apps, while referring in the project scope

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors')
]