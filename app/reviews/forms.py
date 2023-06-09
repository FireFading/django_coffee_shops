from django import forms
from reviews.models import Question, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("text",)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("text", "summary")
