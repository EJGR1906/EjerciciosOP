from django.contrib import admin
from .models import Author,Genre,Movie, MovieInstance
# Register your models here.

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieInstance)

