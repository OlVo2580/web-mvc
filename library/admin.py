from django.contrib import admin
from .models import Author, Edition, Country, EditionsAuthors, EditionsGenres, EditionsSubjects, Faculty, Genre, Reader, ReadersEditions, Status, Subject
from django.db import models
from functools import reduce
import operator

class CaseInsensitiveSearchMixin:
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term and self.search_fields:
            orm_lookups = [f"{search_field}__icontains" for search_field in self.search_fields]
            for bit in search_term.split():
                or_queries = [models.Q(**{orm_lookup: bit}) for orm_lookup in orm_lookups]
                queryset = queryset.filter(reduce(operator.or_, or_queries))
        return queryset, use_distinct

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        for field, value in request.GET.items():
            if field in self.list_filter:
                qs = qs.filter(**{f"{field}__icontains": value})
        return qs


admin.site.register(Country)
admin.site.register(Faculty)
admin.site.register(ReadersEditions)


@admin.register(Edition)
class EditionAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'abstract', 'quantity_available')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'abstract')
    list_filter = ('name', 'abstract')  

@admin.register(EditionsAuthors)
class EditionsAuthorsAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'edition', 'author')
    list_filter = ('edition__name', 'author__first_name', 'author__last_name')  

@admin.register(EditionsGenres)
class EditionsGenresAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'edition', 'genre')
    list_filter = ('edition__name', 'genre__name')  

@admin.register(EditionsSubjects)
class EditionsSubjectsAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'edition', 'subject')
    list_filter = ('edition__name', 'subject__name')  

@admin.register(Genre)
class GenreAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Subject)
class SubjectAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'pseudonym', 'country')
    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('country',)
    search_fields = ('first_name', 'last_name')  
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(id=search_term_as_int)
        except ValueError:
            pass
        return queryset, use_distinct

@admin.register(Reader)
class ReaderAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'faculty', 'first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('faculty', 'username')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')  


@admin.register(Status)
class StatusAdmin(CaseInsensitiveSearchMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
