from rest_framework import generics
from rest_framework.throttling import ScopedRateThrottle
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status

class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        response = Response(serializer.validated_data, status=status.HTTP_200_OK)

        # Set JWTs as HTTP-only cookies
        response.set_cookie(
            key="access_token",
            value=serializer.validated_data["access"],
            httponly=True,
            secure=False,  # True in production with HTTPS
            samesite='Lax',
            max_age=3600
        )
        response.set_cookie(
            key="refresh_token",
            value=serializer.validated_data["refresh"],
            httponly=True,
            secure=False,
            samesite='Lax',
            max_age=7 * 24 * 3600
        )

        return response


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer

    # Restrict to POST only
    http_method_names = ['post']

    # No authentication or permissions required
    permission_classes = []
    authentication_classes = []

    # Enable scoped throttling
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'register'
