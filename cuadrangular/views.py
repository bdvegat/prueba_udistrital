from django.shortcuts import render
from django.http import HttpResponse
from cuadrangular.models import Team
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def create_team(request):
    if request.method == 'POST':
        form_data = json.loads(request.body.decode())
        print(form_data)
        team, created = Team.objects.get_or_create(team_name=form_data['team_name'])
        print(team, created)
        data = {'created':created}
        return JsonResponse(data, safe=False)
        
