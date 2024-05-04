import xadmin
from .models import Team, Coach, Stadium, Player, Game
from xadmin import views

class TeamAdmin(object):
    list_display=['Team_ID', 'Team_Name', 'City', 'Area', 'Coach_Name']
    list_per_page=20
    search_fields=['Team_ID', 'Team_Name']
    list_filter=['City', 'Area', 'Coach_Name']
    ordering=['Team_ID']

xadmin.site.register(Team, TeamAdmin)


class CoachAdmin(object):
    list_display=['Coach_ID', 'Team_ID', 'Coach_Name', 'Num_of_Champ', 'Year_Start']
    list_per_page=20
    search_fields=['Coach_ID', 'Coach_Name']
    list_filter=['Num_of_Champ']
    ordering=['Coach_ID']

xadmin.site.register(Coach, CoachAdmin)


class StadiumAdmin(object):
    list_display=['Stadium_ID', 'Team_ID', 'Stadium_Name', 'Location']
    list_per_page=20
    search_fields=['Stadium_ID',  'Stadium_Name']
    ordering=['Stadium_ID']

xadmin.site.register(Stadium, StadiumAdmin)



class PlayerAdmin(object):
    list_display=['Player_ID', 'Team_ID', 'Player_Name', 'Avg_Point', 'Avg_Rebound', 'Avg_Assist', 'Avg_Steal', 'p3Per', 'p2Per', 'freeThrowPer', 'SALARY']
    list_per_page=20
    search_fields=['Player_ID',  'Player_Name']
    list_filter=['Avg_Point', 'Avg_Rebound', 'p3Per', 'p2Per', 'freeThrowPer', 'SALARY']
    ordering=['Player_ID']

xadmin.site.register(Player, PlayerAdmin)



class GameAdmin(object):
    list_display=['Game_ID', 'Away_Team_ID', 'Home_Team_ID', 'Stadium_ID', 'Score', 'Date']
    list_per_page=20
    search_fields=['Game_ID']
    list_filter=['Away_Team_ID', 'Home_Team_ID', 'Stadium_ID']
    ordering=['Game_ID']

xadmin.site.register(Game, GameAdmin)



class GlobalSetting(object):
    site_title = 'NBA Database Administration system'

    site_footer = 'A NBA Database'
    menu_style='according'

xadmin.site.register(views.CommAdminView, GlobalSetting)


class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(views.BaseAdminView, BaseSetting)





