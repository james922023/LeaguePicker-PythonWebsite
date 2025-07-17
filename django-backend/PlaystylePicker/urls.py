from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TopBuildViewSet, MidBuildViewSet,JungleBuildViewSet,SupportBuildViewSet,BotBuildViewSet

router = DefaultRouter()
router.register(r'topbuilds', TopBuildViewSet)
router.register(r'midbuilds', MidBuildViewSet)
router.register(r'junglebuilds', JungleBuildViewSet)
router.register(r'supportbuilds', SupportBuildViewSet)
router.register(r'botbuilds', BotBuildViewSet)

urlpatterns = [
    path("items/", views.item_list),
    path("champs/", views.champ_list),
    path("runes/", views.rune_list),
    path("", include(router.urls)),
]