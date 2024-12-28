from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_index, name='event_index'),
    path('match-detail/<int:id>', views.event_detail, name='event_detail'),
    path('search-result', views.search, name="search"),

    # Pages par catégorie
    path('laliga', views.laliga_matchs, name='LaLiga_matchs'),
    path('serie-a', views.serie_a_matchs, name='Serie_A_matchs'),
    path('champions-league', views.champions_league_matchs, name='champions_League_matchs'),
    path('coup-de-monde', views.coup_de_monde_matchs, name='coup_de_monde_matchs'),
]
