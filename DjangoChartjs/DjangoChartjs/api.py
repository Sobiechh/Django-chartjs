from rest_framework import routers
from api import api_views as views

router = routers.DefaultRouter()
router.register(r'games', views.GamesViewset)
router.register(r'organizations', views.OrganizationsViewset)
router.register(r'players', views.PlayersViewset)
router.register(r'teams', views.TeamsViewset)