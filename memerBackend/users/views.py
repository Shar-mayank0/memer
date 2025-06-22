from rest_framework import generics
from rest_framework.throttling import ScopedRateThrottle
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

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
