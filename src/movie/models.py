from django.db import models
from django.utils.text import slugify

# Create your models here.


CATEGORY_CHOICE = (
    ('action', 'ACTION'),
    ('comedie', 'COMEDIE'),
    ('drame', 'DRAME'),
    ('fantastique', 'FANTASTIQUE'),
    ('documentaire', 'DOCUMENTAIRE'),
)

LANGUAGE_CHOICE = (
    ('Français', 'FRANÇAIS'),
    ('Englais', 'ANGLAIS'),
)

STATUS_CHOICE = (
    ('RA', 'RECEMMENT AJOUTÉ'),
    ('PV', 'LES PLUS VUE'),
    ('MN', 'LES MEILLEURS NOTÉS'),
)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='movies/')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=15)
    Language = models.CharField(choices=LANGUAGE_CHOICE, max_length=15)
    status = models.CharField(choices=STATUS_CHOICE, max_length=2)
    year_of_production = models.DateField()
    duration = models.IntegerField()
    realized_by = models.CharField(max_length=200)
    cast = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)

    slug = models.SlugField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

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
    link = models.URLField(max_length=350)

    class Meta:
        verbose_name = 'lien film'
        verbose_name_plural = 'liens films'

    def __str__(self):
        return str(self.movie)
