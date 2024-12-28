from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .models import Events

# Create your views here.

# afficher touts les events
def event_index(request):
    events = Events.objects.all()
    return render(request, 'events_app/event_index.html', {'events':events})


# afficher les details d'un event
def event_detail(request, id):
    detail = Events.objects.get(id = id)
    return render(request, 'events_app/event_detail.html', {'detail':detail})


# chercher un event
def search(request):
    if request.method == 'POST':
        search_bar_val = request.POST['search_bar']
        matchs = Events.objects.filter(match__contains=search_bar_val)
        return render(request, "events_app/search_result.html", {'search_bar_val':search_bar_val, 'matchs':matchs})
    else:
        return render(request, "events_app/search_result.html")


def laliga_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie='LaLiga')
    return render(request, "events_app/by_category.html", {'matchs_list': matchs_list})

def serie_a_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie='Serie A')
    return render(request, "events_app/by_category.html", {'matchs_list': matchs_list})

def champions_league_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie='Champions League')
    return render(request, "events_app/by_category.html", {'matchs_list': matchs_list})

def coup_de_monde_matchs(request):
    matchs_list = Events.objects.filter(organisateur__categorie='Coupe du Monde')
    return render(request, "events_app/by_category.html", {'matchs_list': matchs_list})