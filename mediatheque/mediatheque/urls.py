from django.contrib import admin
from django.urls import path, include
import media
from borrowing import urls as borrowing_urls
from media import urls as media_urls
from users import urls as user_urls
from authent import urls as authent_urls
from authent import views as authent_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authent_views.login_user, name="login"),
    path('logout/', authent_views.logout_user, name="logout"),
    path('home/', media.views.home, name="home"),
    path('media/', include(media_urls)),
    path('borrowing/', include(borrowing_urls)),
    path('users/', include(user_urls)),
    path('authent/', include(authent_urls))
]
