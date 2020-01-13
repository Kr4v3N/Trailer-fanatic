from django.db import models

# Create your models here.


CATEGORY_CHOICE = (
    ('action', 'ACTION'),
    ('comedie', 'COMEDIE'),
    ('drame', 'DRAME'),
    ('fantastique', 'FANTASTIQUE'),
    ('documentaire', 'DOCUMENTAIRE'),
)

LANGUAGE_CHOICE = (
    ('FR', 'FRANÇAIS'),
    ('EN', 'ANGLAIS'),
)

STATUS_CHOICE = (
    ('RA', 'RECEMMENT AJOUTÉ'),
    ('PV', 'LES PLUS VUE'),
    ('MN', 'LES MEILLEURS NOTÉS'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='movies/')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=15)
    Language = models.CharField(choices=LANGUAGE_CHOICE, max_length=2)
    status = models.CharField(choices=STATUS_CHOICE, max_length=2)
    year_of_production = models.DateField()
    cast = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'film'
        verbose_name_plural = 'films'

    def __str__(self):
        return self.title


LINK_CHOICE = (
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)


class Movielinks(models.Model):
    movie = models.ForeignKey('Movie', related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICE, max_length=1)
    link = models.URLField()

    class Meta:
        verbose_name = 'lien film'
        verbose_name_plural = 'liens films'

    def __str__(self):
        return str(self.movie)
