from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({"message": "Login successful", "tokens": response.data}, status=status.HTTP_200_OK)

@api_view(["GET"])
def protected_view(request):
    return Response({"message": "This is a protected route!"})
