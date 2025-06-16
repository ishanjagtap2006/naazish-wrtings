from rest_framework import serializers
from .models import Book, AuthorSubmission, ContactMessage

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorSubmission
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
