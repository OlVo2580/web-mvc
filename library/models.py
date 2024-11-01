from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=20, null=True)
    pseudonym = models.CharField(max_length=25, null=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.first_name +" " + self.last_name
    class Meta:
        ordering = ['first_name', 'last_name']

class Country(models.Model):
    name = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return self.name


class Edition(models.Model):
    name = models.CharField(max_length=50, null=True)
    abstract = models.TextField(null=True)
    quantity_available = models.IntegerField(null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name 

    class Meta:
         ordering = ['name']
    def __str__(self):
        return self.name 
    class Meta:
         ordering = ['name']


class EditionsAuthors(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
  

    class Meta:
        unique_together = ('edition', 'author')

    def __str__(self):
        return self.author.first_name + " " + self.author.last_name  + "_" + self.edition.name


class EditionsGenres(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('edition', 'genre')

    def __str__(self):
        return self.genre.name + " " +  self.edition.name


class EditionsSubjects(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('edition', 'subject')
        ordering = ['id']


    def __str__(self):
        return self.subject.name + " " +  self.edition.name
    

class Faculty(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name


class Reader(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=13, null=True)
    def __str__(self):
        return self.username

class ReadersEditions(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    date_taken = models.DateField(null=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        reader = str(self.reader)
        edition = str(self.edition)

        return reader + " "+ edition


class Subject(models.Model):
    name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name

