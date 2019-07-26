from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserData


class CustomUserCreationForm(UserCreationForm):
    def clean(self):
        if len(self.cleaned_data['password1']) < 16:
            self.errors['password1'] = 'Password Must Be at Least 16 characters'
        if self.cleaned_data['password1'] and self.cleaned_data['password2'] and self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.errors['password1'], self.errors['password1'] = 'Passwords don"t match', 'Passwords don"t match'

    class Meta(UserCreationForm):
        model = UserData
        fields = ('first_name', 'last_name', 'username', 'email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = UserData
        fields = ('email', 'username', )
