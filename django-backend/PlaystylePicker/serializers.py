from .models import LeagueItem
from typing import Iterable, List, Dict, Any

#function to take an objects from database and turn them into JSON form

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
            'name':item.name
        })
        
    return data