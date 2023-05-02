from django.urls import path
from reviews.views import AddCommentView, AskQuestionView, QuestionsListView

app_name = "reviews"

urlpatterns = [
    path("add-comment/<str:product_name>/", AddCommentView.as_view(), name="add-comment"),
    path("ask-question/", AskQuestionView.as_view(), name="ask-question"),
    path("questions/", QuestionsListView.as_view(), name="questions"),
]
