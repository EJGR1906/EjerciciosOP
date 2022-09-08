from django.urls import re_path
from . import views
urlpatterns= [
    re_path(r'^$', views.index,name='index'),

    re_path(r'^movies/$', views.MovieListView.as_view(), name='movies'),
    re_path(r'^movie/(?P<pk>\d+)$', views.MovieDetailView.as_view(), name='movie-detail'),

    re_path(r'^authors/$', views.AuthorListView.as_view(), name='author'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),


]

