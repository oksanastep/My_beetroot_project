from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from .models import Container, Waste
from .forms import NewUserForm
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Тепер Ви зареєстровані як {username}.")
                return redirect("home")
            else:
                messages.error(request, "Невірний логін або пароль.")
        else:
            messages.error(request, "Невірний логін або пароль.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Ви успішно вийшли з облікового запису.")
    return redirect("home")