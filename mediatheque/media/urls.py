from django.urls import path
import media.views

urlpatterns = [
    path("media/", media.views.media, name="media"),
    path("detail/<int:id>", media.views.media_detail, name="media_detail"),
    path("jeu_detail/<int:id>/", media.views.jeu_detail, name="jeu_detail"),
    path("book_create", media.views.book_create, name="book_create"),
    path("dvd_create/", media.views.dvd_create, name="dvd_create"),
    path("cd_create/", media.views.cd_create, name="cd_create"),
    path("jeu_create/", media.views.jeu_create, name="jeu_create"),
    path("book_update/<int:id>/", media.views.book_update, name="book_update"),
    path("dvd_update/<int:id>/", media.views.dvd_update, name="dvd_update"),
    path("cd_update/<int:id>/", media.views.cd_update, name="cd_update"),
    path("jeu_update/<int:id>/", media.views.jeu_update, name="jeu_update"),
    path("media_delete/<int:id>/", media.views.media_delete, name="media_delete"),
    path("jeu_delete/<int:id>/", media.views.jeu_delete, name="jeu_delete"),
]