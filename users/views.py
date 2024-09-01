from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data
        refresh = RefreshToken.for_user(User.objects.get(id=user['id']))
        return Response({
            'user': user,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
