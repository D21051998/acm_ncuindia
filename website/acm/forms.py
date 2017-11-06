from django import forms
from .models import *


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('email', 'content')


class UpcomingEventsForm(forms.ModelForm):

    class Meta:
        model = UpcomingEvents
        fields = ('title', 'content', 'active')