from django.urls import path, include
from rest_framework.routers import DefaultRouter
from challenges.views import (
    ChallengeListCreateView, 
    ChallengeDetailView, 
    UserProgressViewSet, 
    LeaderboardViewSet
)

router = DefaultRouter()
router.register(r'progress', UserProgressViewSet, basename='progress')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('', ChallengeListCreateView.as_view(), name='challenge-list-create'),
    path('<int:pk>/', ChallengeDetailView.as_view(), name='challenge-detail'),
    path('', include(router.urls)),
]
