# books/forms.py
from django import forms
from .models import AuthorSubmission

class AuthorSubmissionForm(forms.ModelForm):
    class Meta:
        model = AuthorSubmission
        fields = ['name', 'email', 'bio', 'past_works', 'reason_to_join']
