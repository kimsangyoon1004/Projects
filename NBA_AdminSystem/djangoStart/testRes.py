from django.http import HttpResponse
from django.shortcuts import render
from DB_Models import models

def showRes(request):
    Team = models.Team.objects.get(pk=3)
    print("Team_ID:%d, Team_Name:%s" %(Team.Team_ID, Team.Team_Name) )
    Coach = models.Coach.objects.get(pk=18)
    print("Coach_Name:%s champ:%d" %(Coach.Coach_Name, Coach.Num_of_Champ))

    BUCKS = models.Team.objects.filter(Team_Name="BUCKS").first()

    Stadium = models.Stadium.objects.get(pk=3)
    print("Stadium_Name:%s Location:%s" %(Stadium.Stadium_Name, Stadium.Location))

    Player = models.Player.objects.get(pk=10)
    print("Player_Name:%s Player_pos:%s" %(Player.Player_Name, Player.Team_ID.Team_Name))

    Game = models.Game.objects.get(pk=30)
    print("Game_score:%s Game_Date:%s Game_Home_Team:%s" %(Game.Score, Game.Date, Game.Home_Team_ID.Team_Name))

    return HttpResponse("get the data")
