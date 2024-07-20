from django.shortcuts import render

# Create your views here.
# users/views.py
from djoser.views import TokenCreateView as DjoserTokenCreateView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from .utils import * 
class CustomTokenCreateView(DjoserTokenCreateView):
    def _action(self, serializer):
        # Get the user
        user = serializer.user
        # Generate the token
        refresh = RefreshToken.for_user(user)
        # Return the response with user data
        response_data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'ntel': user.ntel,
                'role': user.role,
                'date_naissance': user.date_naissance,
                'date_joined': user.date_joined,
                'last_login': user.last_login,
                'last_update_profile':user.last_update_profile,
            }
        }
        return Response(response_data)
# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions

User = get_user_model()
#pour retourner info user
class UserFromTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, access_token):
        try:
            access = AccessToken(access_token)
            user_id = access['user_id']
            user = get_object_or_404(User, id=user_id)
            user_data = {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'ntel': user.ntel,
                'role': user.role,
                'date_naissance': user.date_naissance,
                'date_joined': user.date_joined,
                'last_update_profile': user.last_update_profile
            }
            return Response(user_data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    def perform_update(self, serializer):
        serializer.save()
        '''''
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        user_serializer = CreateUserSerializer(instance)
        return Response(user_serializer.data)

        '''

class UserListView(generics.ListAPIView):
    queryset = User.objects.filter(role=False, is_staff=False)
    serializer_class = UserlistSerializer


class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# views.py
from djoser.views import UserViewSet
from .serializers import CustomUserCreateSerializer

class CustomUserViewSet(UserViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserCreateSerializer
        return super().get_serializer_class()


class SendAcontactusEmailView(APIView): 
    def post(self, request): 
        serializer = contactusSerializer(data=request.data) 
        if serializer.is_valid(): 
            subject = serializer.validated_data['subject'] 
            message = serializer.validated_data['message'] 
            sender_email = serializer.validated_data['sender_email'] 
            try: 
                send_contactus_email(subject, message, [settings.ADMIN_EMAIL],sender_email) 
                return Response({"detail": "Email sent successfully."}, status=status.HTTP_200_OK) 
            except Exception as e: 
                return Response({"detail": f"Failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)