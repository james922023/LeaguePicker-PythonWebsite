from .models import LeagueItem
from typing import Iterable, List, Dict, Any
from rest_framework import serializers
from .models import TopBuilds, MidBuilds, BotBuilds, JungleBuilds, SupportBuilds
#custom function to take an objects from database and turn them into JSON form

def serialize_Items(items: Iterable[LeagueItem]) -> List[Dict[str, Any]]:
    """
    Takes Objects from database and turns them into List of Dictionaries to be turned into JSON.
    
    # Parameters
    items
    
    objects pulled from the database
    
    """
    data=[]
    for item in items:
        data.append({
            'name':item.name,
            'url':item.url
        })
        
    return data

#FRAMEWORK ONES ->
class TopBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopBuilds
        fields = ['champion', 'items', 'runes', 'ability_order']

class MidBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = MidBuilds
        fields = ['champion', 'items', 'runes', 'ability_order']

class BotBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotBuilds
        fields = ['champion', 'items', 'runes', 'ability_order']

class JungleBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = JungleBuilds
        fields = ['champion', 'items', 'runes', 'ability_order']

class SupportBuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportBuilds
        fields = ['champion', 'items', 'runes', 'ability_order']