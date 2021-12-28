import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import News




class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Электронная почта',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class NewsForm(forms.ModelForm):  # forms.Form
    class Meta:
        model = News
        fields = ["title", 'content', 'is_published', 'category']  # __all__ - представлены все поля из модели формы
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):  # Кастомный валидатор
        title = self.cleaned_data['title']
        if re.match(r'^\d', title):
            raise ValidationError('Название не должно начинаться c цифры')
        return title

# ---------------------------ФОРМА НЕ СВЯЗАННАЯ С МОДЕЛЯМИ---------------------------------------------------------
# title = forms.CharField(max_length=150, label='Название новости:',
#                         widget=forms.TextInput(attrs={"class": "form-control"}))
# content = forms.CharField(label="Содержание", required=False,
#                           widget=forms.Textarea(attrs={
#                               "class": "form-control",
#                               "rows": 5,
#                           }))
# # required - обязательно ли заполнение.
# is_published = forms.BooleanField(label="Статус", initial=True)  # initisl - начальное значение.
# category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория",
#                                   empty_label="Выберите категорию",
#                                   widget=forms.Select(attrs={"class": "form-control"}))
#                                         empty_label - атрибут выпадающих списков.
