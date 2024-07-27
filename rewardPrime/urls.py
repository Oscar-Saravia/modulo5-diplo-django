from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import getBannerCharacter

router = DefaultRouter()
router.register(r"characters", views.CharacterViewSet)
# router.register(r"bounty", views.BountyViewSet)
# router.register(r"location", views.LocationViewSet)
router.register(r"logCharacter", views.LogCharacterViewSet)
# router.register(r"hunter", views.HunterViewSet)
router.register(r"claimBounty", views.ClaimBountyViewSet)

urlpatterns = [
    path('banner_character/<int:character_id>/', getBannerCharacter, name='get_banner_character'),

    path('bounty/', views.BountyApiView.as_view()),
    path('location/', views.LocationApiView.as_view()),
    # path('logCharacter/', views.LogCharacterApiView.as_view()),
    path('hunter/', views.HunterApiView.as_view()),
    path('', include(router.urls))
]
