from rest_framework import routers
from charts import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'games', myapp_views.GamesViewset)
router.register(r'organizations', myapp_views.OrganizationsViewset)
router.register(r'players', myapp_views.PlayersViewset)
router.register(r'teams', myapp_views.TeamsViewset)