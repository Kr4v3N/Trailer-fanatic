from django.contrib import admin

# Register your models here.

from .models import Movie, Movielinks

admin.site.register(Movie)
admin.site.register(Movielinks)
