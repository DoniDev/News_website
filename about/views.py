from django.shortcuts import render
from . models import *


def about(request):
    about = About.objects.all()[0]
    stats = Statistics.objects.all()
    team = Team.objects.all()

    context = {
        'about':about,
        'stats':stats,
        'team':team
    }

    return render(request,'about/about.html',context=context)
