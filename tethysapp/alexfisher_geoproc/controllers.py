from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    context = {}
    return render(request, 'alexfisher_geoproc/home.html', context)

@login_required()
def team(request):
    context = {}
    return render(request, 'alexfisher_geoproc/team.html', context)

@login_required()
def individual(request):
    context = {}
    return render(request, 'alexfisher_geoproc/individual.html', context)