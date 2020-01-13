from django.db import models

# Create your models here.


CATEGORY_CHOICE = (
    ('AC', 'ACTION'),
    ('CO', 'COMEDIE'),
    ('DR', 'DRAME'),
    ('FA', 'FANTASTIQUE'),
    ('DO', 'DOCUMENTAIRE'),
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
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    Language = models.CharField(choices=LANGUAGE_CHOICE, max_length=2)
    status = models.CharField( choices=STATUS_CHOICE, max_length=2)
    year_of_production = models.DateField()
    view_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'film'
        verbose_name_plural = 'films'

    def __str__(self):
        return self.title
