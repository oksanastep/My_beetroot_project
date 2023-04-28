from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import LoginUserForm, NewUserForm, CommentForm
from .models import Container, Waste, Comment


class HomePageView(TemplateView):

    def get(self, request):
        containers = Container.objects.all()
        form = NewUserForm(request.POST)
        context = {
            'letters': 'абвгґдеєжзіїйклмнопрстуфхцчшщюя',
            'containers': containers,
            'register_form': form
        }
        return render(request, template_name='home.html', context=context)


class AboutUs(TemplateView):
    def get(self, request):
        return render(request, template_name='about_us.html')


class SearchAlphabet(ListView):
    model = Waste
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Waste.objects.filter(Q(name__startswith=query))
        return results


class SearchContainer(ListView):
    model = Waste
    template_name = 'search_container.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Waste.objects.filter(container=query)
        # results = WasteContainer.objects.filter(Q(cont_type__startswith=query))
        return results

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        container = Container.objects.get(pk=self.request.GET.get('q'))
        context.update({'container': container})
        return context


class SearchResultsView(ListView):
    model = Waste
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Waste.objects.filter(Q(name__icontains=query))
        return results


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Невірний логін або пароль.")
        else:
            messages.error(request, "Невірний логін або пароль.")
    form = LoginUserForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect("home")


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
    form_class = CommentForm
    success_url = reverse_lazy('comments')

    def form_valid(self, form):
        user = self.request.user
        comment = form.save(commit=False)
        comment.author = user
        self.object = comment.save()
        return super().form_valid(form)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
