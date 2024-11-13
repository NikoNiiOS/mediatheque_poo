from django.contrib import admin

from media.models import Book, Dvd, Cd, JeuDePlateau, Media
from users.models import User
from borrowing.models import Borrowing


class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)


class MediaAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(User, UserAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Book)
admin.site.register(Dvd)
admin.site.register(Cd)
admin.site.register(JeuDePlateau)
admin.site.register(Borrowing)