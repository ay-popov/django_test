from django.urls import path

from .views import MeView, LoginView, LogoutView, secret_view

app_name = "myauth"

urlpatterns = [

    path("secret/", secret_view, name="secret"),

    path("me/", MeView.as_view(), name="me"),

    path("login/", LoginView.as_view(), name="login"),

    path("logout/", LogoutView.as_view(), name="logout"),
]