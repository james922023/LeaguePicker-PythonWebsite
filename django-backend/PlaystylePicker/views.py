from .models import LeagueItem
from .serializers import serialize_Items
from django.http import JsonResponse
from .models import LeagueChamp
from .models import LeagueRune
from .models import TopBuilds
from rest_framework import permissions, viewsets
from PlaystylePicker.serializers import Build_serializer
from django.views.generic import TemplateView
from rest_framework.permissions import BasePermission, SAFE_METHODS

# Create your views here.

def item_list(request):
    """
    returns a JSON of all LeagueItem from the database.
    # Parameters
    request
    
    """
    items = LeagueItem.objects.all()
    return JsonResponse(serialize_Items(items), safe=False) #returns a JSON of all LeagueItem Objects&Attributes from the database

def champ_list(request):
    """
    returns a JSON of all LeagueChamp from the database.
    # Parameters
    request
    
    """
    items = LeagueChamp.objects.all()
    return JsonResponse(serialize_Items(items), safe=False) #returns a JSON of all LeagueItem Objects&Attributes from the database

def rune_list(request):
    """
    returns a JSON of all LeagueRune from the database.
    # Parameters
    request
    
    """
    items = LeagueRune.objects.all()
    return JsonResponse(serialize_Items(items), safe=False) #returns a JSON of all LeagueItem Objects&Attributes from the database

# ALOOWS PUBLIC TO GET, CUZ CLASS BELOW RESTIRCTS ACCESS
class ReadOnlyOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated
        )

##FRAMEWORK FOR POST
class TopBuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TopBuilds to be viewed or edited.
    """
    queryset = TopBuilds.objects.all()
    serializer_class = Build_serializer
    permission_classes = [ReadOnlyOrAuthenticated]
    


    
    
class ReactAppView(TemplateView):
    template_name = "index.html"
    