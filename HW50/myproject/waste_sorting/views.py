from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from .models import WasteContainer, Waste, Comment
from .forms import CommentForm, NewCommentForm, AboutYouForm, RegisterForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.views import View
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from rest_framework import viewsets, generics, pagination
from rest_framework import permissions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model


class HomePageView(TemplateView):

    def get(self, request):
        return render(request, template_name='home.html')


class CommentsView(ListView, CreateView):
    model = Comment
    allow_empty = True
    queryset = Comment.objects.all()
    paginate_by = 5
    paginate_orphans = 3
    context_object_name = 'comments'
    page_kwarg = "page"
    ordering = ['-date_created']
    template_name = 'comments.html'

    object = Comment()
    form_class = NewCommentForm
    success_url = reverse_lazy('comments')

    def form_valid(self, form):
        user = self.request.user
        comment = form.save(commit=False)
        comment.author = user
        self.object = comment.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AboutYouView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='about_you.html',
            context={
                'form': AboutYouForm(),
                'user': request.user
            }
        )

    def post(self, request):
        user = request.user
        form = AboutYouForm(request.POST)

        print(form)
        return self.get(request)


class RegisterView(UserPassesTestMixin, CreateView):
    object = get_user_model()
    form_class = RegisterForm
    success_url = reverse_lazy('comments')
    template_name = 'registration.html'

    def test_func(self):
        if self.request.user.is_anonymous:
            print(self.request.user)
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect(self.success_url)

    def form_valid(self, form):
        user = form.save(commit=False)
        self.object = user.save()

        my_group = Group.objects.get(name='regular_user')
        my_group.user_set.add(user)

        return super().form_valid(form)


class SearchResultsView(ListView):
    model = Waste
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Waste.objects.filter(Q(waste_name__icontains=query))
        return results
