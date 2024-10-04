from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.decorators import method_decorator
from .serializers import UserSerializer


User = get_user_model()


class RegisterUserView(APIView):
    """
    Register a new user.
    Expects 'email', 'username', and 'password' in the request body.
    Returns success message with JWT tokens or errors if validation fails.
    """

    @method_decorator(csrf_exempt)
    def post(self, request):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        if not all([email, username, password]):
            return Response(
                {"error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "This email already exists"}, status=status.HTTP_403_FORBIDDEN
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"}, status=status.HTTP_403_FORBIDDEN
            )

        new_user = User.objects.create(
            email=email, username=username, password=make_password(password)
        )

        refresh = RefreshToken.for_user(new_user)

        return Response(
            {
                "message": "User created successfully",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginUserView(APIView):
    """
    Log in an existing user.
    Expects 'identifier' (email or username) and 'password' in the request body.
    Returns success message with JWT tokens or errors if authentication fails.
    """

    @method_decorator(csrf_exempt)
    def post(self, request):
        identifier = request.data.get("identifier")
        password = request.data.get("password")

        if not all([identifier, password]):
            return Response(
                {"error": "Identifier (email or username) and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = self.authenticate_user(identifier)

        if user is None or not user.check_password(password):
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK,
        )

    def authenticate_user(self, identifier):
        try:
            return User.objects.get(email=identifier)
        except User.DoesNotExist:
            try:
                return User.objects.get(username=identifier)
            except User.DoesNotExist:
                return None


class GetAllUsersView(APIView):
    """
    Fetch all users.
    """

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
