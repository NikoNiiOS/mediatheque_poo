from django.contrib import admin
from django.urls import path
import borrowing.views


urlpatterns = [
    path('borrowing/<int:id>', borrowing.views.borrowing_media, name='borrowing_media'),
    path('borrowing_impossible', borrowing.views.borrowing_impossible, name='borrowing_impossible'),
    path('borrowing_late', borrowing.views.borrowing_late, name='borrowing_late'), 
]