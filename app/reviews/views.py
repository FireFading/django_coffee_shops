from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from menu.models import MenuItem
from reviews.forms import QuestionForm, ReviewForm
from reviews.models import Question


class AddCommentView(FormView):
    template_name = "reviews/comment.html"
    form_class = ReviewForm
    success_url = reverse_lazy("menu:detail")

    def form_valid(self, form):
        product_name = self.kwargs["product_name"]
        menu_item = get_object_or_404(MenuItem, name=product_name)
        comment = form.save(commit=False)
        comment.menu_item = menu_item
        comment.user = self.request.user
        comment.save()
        return redirect("menu:detail", product_name=menu_item.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_name = self.kwargs["product_name"]
        context["product"] = get_object_or_404(MenuItem, name=product_name)
        return context


class AskQuestionView(FormView):
    template_name = "reviews/new_question.html"
    form_class = QuestionForm
    success_url = reverse_lazy("reviews:questions")

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = self.request.user
        question.save()
        subject = "Thank you for your question"
        message = render_to_string(
            "mail/thanks_for_question.html",
            {
                "question": question,
            },
        )
        send_email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [question.user.email],
        )
        try:
            send_email.send()
        except Exception as error:
            print(f"Error to send email: {error}")
        return redirect("reviews:questions")


class QuestionsListView(ListView):
    model = Question
    template_name = "reviews/questions.html"
    context_object_name = "questions"
    paginate_by = 50
