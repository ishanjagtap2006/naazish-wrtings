from django.shortcuts import render, redirect
from .models import Book, AuthorSubmission, ContactMessage
from .forms import AuthorSubmissionForm

from rest_framework import generics
from rest_framework.filters import SearchFilter
from .serializers import BookSerializer, AuthorSubmissionSerializer, ContactMessageSerializer

# Home view rendering books and author submission form with search
def home(request):
    query = request.GET.get('q', '')
    
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(genre__icontains=query)
    else:
        books = Book.objects.all()

    success_message = None

    if request.method == 'POST':
        form = AuthorSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Thank you for joining Naazish Writings!"
            form = AuthorSubmissionForm()  # Clear form
    else:
        form = AuthorSubmissionForm()

    return render(request, 'index.html', {
        'books': books,
        'form': form,
        'success_message': success_message,
        'query': query,
    })

# API view for listing books with search
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'genre']

# API view for author form submission
class AuthorCreateView(generics.CreateAPIView):
    queryset = AuthorSubmission.objects.all()
    serializer_class = AuthorSubmissionSerializer

# API view for contact form submission
class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
