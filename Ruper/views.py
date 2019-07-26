from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import UserData


class SignUp(CreateView):
    model = UserData
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Index(View):
    def get(self, request):
        return render(request, 'ruper/index.html', )


# class Login(View):
#     def get(self, request):
#         return render(request, 'registration/login.html', )
