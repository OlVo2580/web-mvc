from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('author/', author, name='author'),
    path('subject/', subject, name='subject'),
    path('abstract/<int:edition_id>/', abstract, name='abstract'), 
    path('author_edition_/<int:author_id>/', author_edition, name='author_edition'),
    path('subject/<int:subject_id>/editions/', subject_editions, name='subject_editions'),
    path('genre/', genre, name='genre'),
    path('genre/<int:genre_id>/', genre_editions, name='genre_editions'),
    path('addedition/', addedition, name='addedition'),
    path('addauthor/', addauthor, name='addauthor'),
    path('addauthor_success/', addauthor_success, name='addauthor_success'),
    path('author/<int:author_id>/delete/', delete_author, name='delete_author'),
    path('author/<int:author_id>/update/', update_author, name='update_author'),
   path('change_status/<int:edition_id>/', update_edition_status, name='change_status')

    ]
