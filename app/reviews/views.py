from django.shortcuts import get_object_or_404, redirect
from menu.models import MenuItem
from reviews.forms import ReviewForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class AddCommentView(FormView):
    template_name = 'reviews/comment.html'
    form_class = ReviewForm
    success_url = reverse_lazy("menu:detail")

    def form_valid(self, form):
        product_name = self.kwargs['product_name']
        menu_item = get_object_or_404(MenuItem, name=product_name)
        comment = form.save(commit=False)
        comment.menu_item = menu_item
        comment.user = self.request.user
        comment.save()
        return redirect('menu:detail', product_name=menu_item.name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_name = self.kwargs['product_name']
        context['product'] = get_object_or_404(MenuItem, name=product_name)
        return context