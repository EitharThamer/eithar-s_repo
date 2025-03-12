from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    
    path('links/', views.links, name="books.links"),
    path('formatting/', views.formatting, name="books.formatting"),
    path('listing/', views.listing, name="books.listing"),
    path('tables/', views.tables, name="books.tables"),
]
 
