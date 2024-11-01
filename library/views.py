from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import AddAuthorForm, AuthorForm, ChangeEditionStatusForm
from .forms import AddAuthorForm, AddEditionForm


from .models import *



menu = ['Фонд кафедральної бібліотеки', 'Обрати видання', 'Увійти']


def index(request):
    return render(request, 'library/index.html', {'menu': menu, 'title': 'Кафедральна бібліотека'})


def about(request):
    editions = Edition.objects.all()
    edition_statuses = {}
    for edition in editions:
        # Отримання всіх записів ReadersEditions для поточного видання
        readers_editions = ReadersEditions.objects.filter(edition=edition)
        # Отримання останнього статусу для поточного видання
        if readers_editions.exists():
            latest_status = readers_editions.latest('date_taken').status
        else:
            latest_status = None
        edition_statuses[edition] = latest_status
    return render(request, 'library/about.html', {'editions': edition_statuses, 'menu': menu, 'title': 'Фонд кафедральної бібліотеки:'})

def update_edition_status(request, edition_id):
    edition = get_object_or_404(Edition, pk=edition_id)
    if request.method == 'POST':
        form = ChangeEditionStatusForm(request.POST, instance=edition)
        if form.is_valid():
            form.save()
            return redirect('some_success_url') 
        else:
         form = ChangeEditionStatusForm(instance=edition)
    return render(request, 'library/update_edition_status.html', {'form': form})

def author(request):
     author = Author.objects.all()  
     return render(request, 'library/author.html', {'authors': author, 'menu' : menu, 'title' : 'Автори'})

def addauthor(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Автор успішно додано!')
            return redirect('addauthor_success')  # Перенаправлення на сторінку успіху
    else:
        form = AddAuthorForm()

    return render(request, 'library/addauthor.html', {'form': form, 'menu' : menu, 'title' : 'Додати '})

def addauthor_success(request):
    return render(request, 'library/addauthor_success.html')


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('author')  # Перенаправити на сторінку авторів після видалення
    return render(request, 'library/delete_author.html', {'author': author})

def update_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author')  # Перенаправлення на сторінку авторів після успішного оновлення
    else:
        form = AuthorForm(instance=author)

    return render(request, 'library/update_author.html', {'form': form})


def author_edition(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    editions = EditionsAuthors.objects.filter(author=author)

    for edition_author in editions:
        print(edition_author.edition.name)
    return render(request, 'library/works.html', {'title': 'Твори автора', 'author': author, 'works': editions})


def subject(request):
     subject = Subject.objects.all()
     return render(request, 'library/subject.html', {'subjects': subject, 'menu' : menu, 'title' : 'За тематиками'})


def subject_editions(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    editions_subjects = EditionsSubjects.objects.filter(subject=subject)
    editions = [editions_subject.edition for editions_subject in editions_subjects]
    return render(request, 'library/subject_editions.html', {'subject': subject, 'editions': editions})


def abstract(request, edition_id):
    edition = get_object_or_404(Edition, pk=edition_id)
    return render(request, 'library/abstract.html', {'edition': edition})

def editions(request, editionsid):
     if(request.POST):
          print(request.POST)
     return HttpResponse (f"<h1>Видання наявні в бібліотеці</h1><p>{editionsid}</p>")

def genre(request):
     genres = Genre.objects.all()
     return render(request, 'library/genre.html', {'genres': genres, 'menu' : menu, 'title' : 'За жанрами'})


def genre_editions(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    editions = Edition.objects.filter(editionsgenres__genre=genre)
    return render(request, 'library/genre_edition.html', {'genre': genre, 'editions': editions})

def addedition(request):
    if request.method == 'POST':
        form = AddEditionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Дані успішно збережено!")
    else:
        form = AddEditionForm()

    return render(request, 'library/addedition.html', {'form': form, 'menu' : menu, 'title' : 'Додати видання'})






def test(request):
     return render(request, 'library/test.html')


def pageNotFound(request, exception):
     print("404 Сторінку не знайдено")
     return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')
