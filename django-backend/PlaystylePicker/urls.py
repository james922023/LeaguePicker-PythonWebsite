from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TopBuildViewSet

router = DefaultRouter()
router.register(r'topbuilds', TopBuildViewSet)

urlpatterns = [
    path("items/", views.item_list),
    path("champs/", views.champ_list),
    path("runes/", views.rune_list),
    path("", include(router.urls)),
]