from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
# Register your models here.
from . models import LeagueItem
from .models import LeagueChamp
from .models import LeagueRune
from .models import TopBuilds



admin.site.register(LeagueItem)
admin.site.register(LeagueChamp)
admin.site.register(LeagueRune)
admin.site.register(TopBuilds)
