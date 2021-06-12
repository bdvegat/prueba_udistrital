from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=30) 

class Match(models.Model):
    team1 = models.ForeignKey(Team,related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team,related_name='team2', on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)