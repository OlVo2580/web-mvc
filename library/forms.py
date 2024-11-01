from django import forms
from .models import * 

class AddEditionForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Назва')
    abstract = forms.CharField(widget=forms.Textarea, label='Анотація')
    quantity_available = forms.IntegerField(label='Кількість доступних примірників')
    authors = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор', empty_label='не вибрано')
    genres = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Жанри', empty_label='не вибрано')
    subjects = forms.ModelChoiceField(queryset=Subject.objects.all(), label='Тематики', empty_label='не вибрано')
    stutus = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', empty_label='не вибрано')
    

    class Meta:
        model = Edition
        fields = ['name', 'abstract', 'quantity_available', 'authors', 'genres', 'subjects']

class AddAuthorForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="Ім'я")
    last_name = forms.CharField(max_length=50, label="Прізвище")
    pseudonym = forms.CharField(max_length=50, label="Псевдонім")
    country = forms.ModelChoiceField(queryset=Country.objects.all(), label="Країна")

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pseudonym', 'country']


class AuthorForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="Ім'я")
    last_name = forms.CharField(max_length=50, label="Прізвище")
    pseudonym = forms.CharField(max_length=50, label="Псевдонім")
    country = forms.ModelChoiceField(queryset=Country.objects.all(), label="Країна")

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'pseudonym', 'country']

class ChangeEditionStatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


