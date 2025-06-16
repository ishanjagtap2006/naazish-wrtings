from django.urls import path
from .views import home, BookListView, AuthorCreateView, ContactCreateView

urlpatterns = [
    path('', home, name='home'),  # Renders the main index.html
    path('books/', BookListView.as_view(), name='book-list'),  # API endpoint to list books
    path('authors/', AuthorCreateView.as_view(), name='author-create'),  # API endpoint for author form
    path('contact/', ContactCreateView.as_view(), name='contact-create'),  # API endpoint for contact form
]
