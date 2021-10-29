from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import User
from core.serializer import RegisterSerializer, UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)


class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        user: User = serializer.user
        context = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_client": user.is_client,
            "is_superuser": user.is_superuser,
            "access": serializer.validated_data.get("access"),
            "refresh": serializer.validated_data.get("refresh"),
            "book_marks": user.book_marks
        }
        return Response(context, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []

    @action(detail=True, methods=["get"], url_path="add-favorite/(?P<house_id>[0-9]+)")
    def add_bookmark(self, request, house_id, *args, **kwargs):
        user = self.get_object()
        new_bookmarks: list = user.book_marks
        new_bookmarks.append(int(house_id))
        user.book_marks = new_bookmarks
        user.save()
        return Response({"message": "Add bookmark successfully"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], url_path="remove-favorite/(?P<house_id>[0-9]+)")
    def remove_bookmark(self, request, house_id, *args, **kwargs):
        user = self.get_object()
        new_bookmarks: list = user.book_marks
        new_bookmarks.remove(int(house_id))
        user.book_marks = new_bookmarks
        user.save()
        return Response({"message": "Remove bookmark successfully"}, status=status.HTTP_200_OK)