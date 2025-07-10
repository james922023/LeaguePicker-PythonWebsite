from .models import LeagueItem
from typing import Iterable, List, Dict, Any
from rest_framework import serializers
from .models import TopBuilds
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
class Build_serializer(serializers.ModelSerializer):
    class Meta:
        model=TopBuilds
        fields=['champion', 'items', 'runes', 'ability_order']