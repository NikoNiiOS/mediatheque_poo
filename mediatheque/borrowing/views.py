from django.shortcuts import render, redirect
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from media.models import Media
from users.models import User
from borrowing.forms import BorrowingForm
from borrowing.models import Borrowing

import datetime


def is_staff_user(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff_user)
def borrowing_media(request, id):
    media = Media.objects.get(id=id)
    if request.method == "POST":
        if media.disponible:
            form = BorrowingForm(request.POST)
            emprunt = form.save(commit=False)
            emprunt.media = media
            media.date_emprunt = emprunt.date
            user = User.objects.get(id=emprunt.emprunteur.id)

            borroweds_medias = Borrowing.objects.all()
            dates = []
            for borrowed_media in borroweds_medias:
                if borrowed_media.emprunteur == user:
                    date = borrowed_media.date
                    dates.append(date)
            for date in dates:
                delta = datetime.date.today() - date
                if delta.days > 7:
                    return redirect("borrowing_late")
            if user.nombreEmprunts >= 3:
                return redirect("borrowing_impossible")
            else:
                media.disponible = False
                media.save()
                user.nombreEmprunts += 1
                user.save()
                emprunt.save()
            return redirect("borrowing_impossible")
        elif media.disponible == False:
            emprunt = Borrowing.objects.get(media=media.id)
            form = BorrowingForm(request.POST, instance=emprunt)
            emprunt = form.save(commit=False)
            user = User.objects.get(id=emprunt.emprunteur.id)
            media.disponible = True
            media.save()
            user.nombreEmprunts -= 1
            user.save()
            emprunt.delete()
            return redirect("media_detail", media.id)
    form = BorrowingForm()
    return render(request, "borrowing/media_loan.html", {"media": media, "form": form})

@login_required
@user_passes_test(is_staff_user)
def borrowing_impossible(request):
    return render(request, "borrowing/borrowing_impossible.html")


def borrowing_late(request):
    return render(request, "borrowing/borrowing_late.html")