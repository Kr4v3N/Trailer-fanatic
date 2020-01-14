from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, Movielinks


class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['recently_added'] = Movie.objects.filter(status='RA')
        context['most_watched'] = Movie.objects.filter(status='PV')
        context['top_rated'] = Movie.objects.filter(status='MN')
        print(context)

        return context


class MovieList(ListView):
    model = Movie
    paginate_by = 5


class MovieDetail(DetailView):
    model = Movie

    def get_object(self, queryset=None):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()

        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = Movielinks.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)  # .order_by[
        # 'created'][0:6]

        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 10

    def get_queryset(self):
        self.category = self.kwargs['category']

        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category

        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 15

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(Language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language

        return context


class MovieSearch(ListView):
    model = Movie
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            print(query)
            print(object_list)
        else:
            object_list = self.model.objects.none()

        return object_list


class MovieYear(YearArchiveView):
    paginate_by = 15
    queryset = Movie.objects.all()
    date_field = "year_of_production"
    make_object_list = True
    allow_future = True

    print(queryset)
