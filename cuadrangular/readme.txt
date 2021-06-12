Rutas:
registrar equipo: http://localhost:8000/cuadrangular/create_team
post 
json:
{
    "team_name" : "equipo a"
}
registrar partido: http://localhost:8000/cuadrangular/register_result
post
json:
{
    "team1" : "equipo a",
    "team2" : "equipo b",
    "team1_score" : "12",
    "team2_score" : "12"
}

