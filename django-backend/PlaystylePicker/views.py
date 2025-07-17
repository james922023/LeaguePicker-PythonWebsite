from .models import LeagueItem
from .serializers import serialize_Items
from django.http import JsonResponse
from .models import LeagueChamp
from .models import LeagueRune
from .models import TopBuilds
from .models import MidBuilds
from .models import BotBuilds
from .models import SupportBuilds
from .models import JungleBuilds
from rest_framework import permissions, viewsets

from django.views.generic import TemplateView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Min, Max
import random
from rest_framework.permissions import BasePermission, SAFE_METHODS

from PlaystylePicker.serializers import (
    TopBuildSerializer,
    MidBuildSerializer,
    BotBuildSerializer,
    JungleBuildSerializer,
    SupportBuildSerializer,
)

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
    serializer_class = TopBuildSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    
    @action(detail=False, methods=['get'], url_path='random')
    def random_build(self, request):
        min_id = self.queryset.aggregate(Min('id'))['id__min']
        max_id = self.queryset.aggregate(Max('id'))['id__max']

        if min_id is None or max_id is None:
            return Response({'detail': 'No builds found'}, status=404)

        while True:
            random_id = random.randint(min_id, max_id)
            build = self.queryset.filter(id=random_id).first()
            if build:
                serializer = self.get_serializer(build)
                return Response(serializer.data)

class MidBuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MidBuilds to be viewed or edited.
    """
    queryset = MidBuilds.objects.all()
    serializer_class = MidBuildSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    
    @action(detail=False, methods=['get'], url_path='random')
    def random_build(self, request):
        min_id = self.queryset.aggregate(Min('id'))['id__min']
        max_id = self.queryset.aggregate(Max('id'))['id__max']

        if min_id is None or max_id is None:
            return Response({'detail': 'No builds found'}, status=404)

        while True:
            random_id = random.randint(min_id, max_id)
            build = self.queryset.filter(id=random_id).first()
            if build:
                serializer = self.get_serializer(build)
                return Response(serializer.data)
    
class BotBuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MidBuilds to be viewed or edited.
    """
    queryset = BotBuilds.objects.all()
    serializer_class = BotBuildSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    
    @action(detail=False, methods=['get'], url_path='random')
    def random_build(self, request):
        min_id = self.queryset.aggregate(Min('id'))['id__min']
        max_id = self.queryset.aggregate(Max('id'))['id__max']

        if min_id is None or max_id is None:
            return Response({'detail': 'No builds found'}, status=404)

        while True:
            random_id = random.randint(min_id, max_id)
            build = self.queryset.filter(id=random_id).first()
            if build:
                serializer = self.get_serializer(build)
                return Response(serializer.data)
    
class JungleBuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MidBuilds to be viewed or edited.
    """
    queryset = JungleBuilds.objects.all()
    serializer_class = JungleBuildSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    
    @action(detail=False, methods=['get'], url_path='random')
    def random_build(self, request):
        min_id = self.queryset.aggregate(Min('id'))['id__min']
        max_id = self.queryset.aggregate(Max('id'))['id__max']

        if min_id is None or max_id is None:
            return Response({'detail': 'No builds found'}, status=404)

        while True:
            random_id = random.randint(min_id, max_id)
            build = self.queryset.filter(id=random_id).first()
            if build:
                serializer = self.get_serializer(build)
                return Response(serializer.data)

class SupportBuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MidBuilds to be viewed or edited.
    """
    queryset = SupportBuilds.objects.all()
    serializer_class = SupportBuildSerializer
    permission_classes = [ReadOnlyOrAuthenticated]   
    
    @action(detail=False, methods=['get'], url_path='random')
    def random_build(self, request):
        min_id = self.queryset.aggregate(Min('id'))['id__min']
        max_id = self.queryset.aggregate(Max('id'))['id__max']

        if min_id is None or max_id is None:
            return Response({'detail': 'No builds found'}, status=404)

        while True:
            random_id = random.randint(min_id, max_id)
            build = self.queryset.filter(id=random_id).first()
            if build:
                serializer = self.get_serializer(build)
                return Response(serializer.data) 
    
class ReactAppView(TemplateView):
    template_name = "index.html"
    