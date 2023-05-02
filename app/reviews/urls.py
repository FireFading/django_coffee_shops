from reviews.views import AddCommentView
from django.urls import path

app_name = "reviews"

urlpatterns = [
    path('add-comment/<str:product_name>/', AddCommentView.as_view(), name='add-comment'),
]
