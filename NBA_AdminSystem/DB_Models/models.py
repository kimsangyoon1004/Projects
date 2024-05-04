from django.db import models



class Team(models.Model):
    #db_index创建索引
    Team_ID = models.AutoField(verbose_name="Team_ID", primary_key=True, db_index=True) 
    Team_Name = models.CharField(verbose_name="Team Name", max_length=20, db_index=True)
    City = models.CharField(verbose_name="City", max_length=35)
    Area = models.CharField(verbose_name="Area", max_length=5)
    Coach_Name = models.CharField(verbose_name="Coach", max_length=35)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Team_Name




class Coach(models.Model):
    Coach_ID = models.AutoField(verbose_name="Coach_id", primary_key=True, db_index=True) 
    #ForeignKey
    Team_ID = models.ForeignKey("Team" , on_delete=models.CASCADE, verbose_name="Team Name") 

    Coach_Name = models.CharField(verbose_name="Coach Name", max_length=35, db_index=True)
    Num_of_Champ = models.IntegerField(verbose_name="Num_of_Champ", default=0)
    SALARY = models.DecimalField(verbose_name="SALARY", max_digits=6, decimal_places=2)
    Year_Start = models.DateField(verbose_name="Coach year start")

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Coach_Name



class Stadium(models.Model):
    Stadium_ID = models.AutoField(verbose_name="Stadium_ID", primary_key=True, db_index=True) 
    Team_ID = models.ForeignKey("Team" , on_delete=models.CASCADE, verbose_name="Team") 

    Stadium_Name = models.CharField(verbose_name="Stadium Name", max_length=50)
    Location = models.CharField(verbose_name="Location", max_length=50)

    class Meta:
        verbose_name = "Stadium"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Stadium_Name



class Player(models.Model):
    Player_ID = models.AutoField(verbose_name="Player_id", primary_key=True, db_index=True) 
    Team_ID = models.ForeignKey("Team" , on_delete=models.CASCADE, verbose_name="Team") 

    Player_Name = models.CharField(verbose_name="Player Name", max_length=35, db_index=True)
    Avg_Point = models.DecimalField(verbose_name="Avg_Point", max_digits=4, decimal_places=1)
    Avg_Rebound = models.DecimalField(verbose_name="Avg_Rebound", max_digits=4, decimal_places=1)
    Avg_Assist = models.DecimalField(verbose_name="Avg_Assist", max_digits=4, decimal_places=1)
    Avg_Steal = models.DecimalField(verbose_name="Avg_Steal", max_digits=4, decimal_places=1)
    Avg_Block = models.DecimalField(verbose_name="Avg_Block", max_digits=4, decimal_places=1)
    Avg_Trunover = models.DecimalField(verbose_name="Avg_Trunover", max_digits=4, decimal_places=1)
    Avg_Foul = models.DecimalField(verbose_name="Avg_Foul", max_digits=4, decimal_places=1)

    p3Per = models.DecimalField(verbose_name="3point%", max_digits=3, decimal_places=1)
    p2Per = models.DecimalField(verbose_name="shoot%", max_digits=3, decimal_places=1)
    freeThrowPer = models.DecimalField(verbose_name="freeThrow%", max_digits=3, decimal_places=1)
    Position = models.CharField(verbose_name="Position", max_length=15, db_index=True)
    SALARY = models.DecimalField(verbose_name="SALARY(/10000 dollars)", max_digits=6, decimal_places=2)


    class Meta:
        verbose_name = "Player"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Player_Name



class Game(models.Model):
    Game_ID = models.AutoField(verbose_name="Game_id", primary_key=True, db_index=True) 
    Away_Team_ID = models.ForeignKey("Team" , related_name="Away_Team", on_delete=models.CASCADE, verbose_name="Away_Team") 
    Home_Team_ID = models.ForeignKey("Team" , related_name="Home_Team", on_delete=models.CASCADE, verbose_name="Home_Team")
    Stadium_ID = models.ForeignKey("Stadium" , on_delete=models.CASCADE, verbose_name="Stadium")

    Score = models.CharField(verbose_name="Score", max_length=10)
    Date = models.DateField(verbose_name="Date")

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = verbose_name

