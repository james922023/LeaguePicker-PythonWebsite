from .models import LeagueItem
from .serializers import serialize_Items
from django.http import JsonResponse

# Create your views here.

def item_list(request):
    """
    returns a JSON of all LeagueItem from the database.
    # Parameters
    request
    
    """
    items = LeagueItem.objects.all()
    return JsonResponse(serialize_Items(items), safe=False) #returns a JSON of all LeagueItem Objects&Attributes from the database
    