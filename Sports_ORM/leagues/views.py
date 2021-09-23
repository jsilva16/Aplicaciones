from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all().order_by("location"),
		"inverted_teams": Team.objects.all().order_by("-team_name"),
		"players": Player.objects.all(),
		"cooper_players": Player.objects.filter(last_name="Cooper"),
		"players_name_filter": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),
		"cooper_notJoshua_players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"joshua_players": Player.objects.filter(first_name="Joshua"),
		"women_leagues": League.objects.filter(name__contains="women"),
		"hockey_leagues": League.objects.filter(name__contains="hockey"),
		"football_leagues": League.objects.filter(name__contains="football"),
		"conference_leagues": League.objects.filter(name__contains="conference"),
		"atlantic_leagues": League.objects.filter(name__contains="atlantic"),
		"city_team": Team.objects.filter(location__contains="city"),
		"t_team": Team.objects.filter(team_name__startswith="t"),
		

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")