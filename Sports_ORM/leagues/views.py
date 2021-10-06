from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

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

def sports_ii(request):
	football_leagues= League.objects.filter(sport="Football")

	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"atlantic_teams": Team.objects.filter(league__id=5),
		"penguin_players": Team.objects.filter(league__id=5),
		"int_baseball_conf": Team.objects.filter(league__name="International Collegiate Baseball Conference"),
		"players": Player.objects.all(),
		"football_leagues": football_leagues,
		"football_teams": Team.objects.filter(league__name__contains="Football"),
		"football_players": Player.objects.filter(curr_team__league__name__contains="Football"),
		"sophia_teams": Team.objects.filter(curr_players__first_name="Sophia"),
		"lopez_players": Player.objects.filter(curr_team__league_id=7).filter(last_name="Lopez"),
		"flores_players": Player.objects.exclude(curr_team__team_name="Roughriders").filter(last_name="Flores"),
		"samuel_teams": Team.objects.filter(all_players__last_name="Evans").filter(all_players__first_name="Samuel"),
		"manitoba_players": Player.objects.filter(all_teams__location="Manitoba").filter(all_teams__team_name="Tiger-Cats"),
		"wichita_players": Player.objects.filter(all_teams__location="Wichita").filter(all_teams__team_name="Vikings"),
		"curr_wichita_players": Player.objects.filter(curr_team__location="Wichita").filter(curr_team__team_name="Vikings"),
		"jacob_teams": Team.objects.filter(all_players__id=151).exclude(curr_players__curr_team__id=24),
		"joshua_players": Player.objects.filter(first_name="Joshua").filter(all_teams__league__id=3),
		"count_players" : Player.objects.all().annotate(team_count=Count("all_teams")).order_by('-team_count'),
		"count_team_players" : Team.objects.annotate(player_count=Count("all_players")).filter(player_count__gt=11).order_by('-player_count'),


		

	}
	return render(request, "leagues/sports_2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")