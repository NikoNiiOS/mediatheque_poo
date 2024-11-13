import authent.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("logout/", authent.views.logout_user, name ="logout")
]