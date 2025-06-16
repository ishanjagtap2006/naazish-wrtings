from django.contrib import admin

# Register your models here.
from .models import Book, AuthorSubmission, ContactMessage

admin.site.register(Book)
admin.site.register(AuthorSubmission)
admin.site.register(ContactMessage)
