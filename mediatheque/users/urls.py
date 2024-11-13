from django.contrib import admin
from django.urls import path
import users.views

urlpatterns = [
    path("users/", users.views.users, name="users"),
    path("users/<int:id>/", users.views.user_detail, name="user_detail"),
    path("users/add", users.views.user_create, name="user_create"),
    path("users/<int:id>/update", users.views.user_update, name="user_update"),
    path("users/<int:id>/delete", users.views.user_delete, name="user_delete",
    ),
    path("users/home/", users.views.home, name="users_home"),
]