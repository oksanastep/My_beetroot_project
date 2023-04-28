from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Comment
from crispy_forms.layout import Submit


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Ім'я клристувача"
        self.fields["password"].label = "Пароль"


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Ім'я користувача"
        self.fields['email'].label = "Електронна пошта"
        self.fields['password1'].label = "Введіть пароль"
        self.fields['password2'].label = "Повторіть пароль"
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = ''

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Відправити'))

    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.TextInput()
        }
