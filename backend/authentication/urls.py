from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import CustomTokenObtainPairView, protected_view

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', protected_view, name='protected_view'),
]
