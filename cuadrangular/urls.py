from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("create_team",views.create_team),
    path("register_result",views.register_result),
]
