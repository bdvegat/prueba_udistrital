from django.shortcuts import render
from django.http import HttpResponse
from cuadrangular.models import Team
from cuadrangular.models import Match
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world.")

@csrf_exempt
def create_team(request):
    if request.method == 'POST':
        try:
            form_data = json.loads(request.body.decode())
            team, created = Team.objects.get_or_create(team_name=form_data['team_name'])
            print(team, created)
            data = {'created':created}
        except:
            data = {'error':'empty required parameter'}
        return JsonResponse(data, safe=False)

@csrf_exempt
def register_result(request):
    if request.method == 'POST':
        form_data = json.loads(request.body.decode())
        try:
            team1 = form_data['team1']
            team2 = form_data['team2']
            team1_score = form_data['team1_score']
            team2_score = form_data['team2_score']

            if len(Team.objects.filter(team_name = team1)) == 1:
                if len(Team.objects.filter(team_name = team2)) == 1:
                    team = Match.objects.create(team1=team1,team2 = team2, team1_score=team1_score, team2_score = team2_Score)
                    data = {'status':'registered'}
                else: data = {'error':'team2 not found'}
            else:
                data = {'error':'team1 not found'}
        except ex:
            print(ex)
            data = {'error':'required parameters empty'}
        return JsonResponse(data, safe=False)