from django.urls import path
from . import views
from stream.views import *
urlpatterns = [
    path('',index,name='stream'),
    # path('more/',More,name='viewmore'),
    path('moviespage/',top_movies,name='topmovies'),
    path('moviespage2/',bottom_movies,name='bottommovies'),
    path('seriespage/',series_page,name='topseries'),
    path('searchname/',search_name,name='search_name'),
    path('moviedetails/<int:id>',movie_details,name='moviedetails'),
    path('seriesdetails/<int:id>',series_details,name='seriesdetails'),
    path('seasonepisode/',season_episode,name='seasonepisode'),
    # path('a/',series,name='check')
   
]
