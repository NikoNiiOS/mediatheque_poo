import pytest

from django.test import Client
from media.models import Book, Dvd, Cd, JeuDePlateau, Media
from users.models import User
from borrowing.models import Borrowing
from datetime import date

@pytest.mark.django_db
def test_book_model():
    client = Client()
    book = Book.objects.create(name="Harry Potter", auteur="J.K, Rowling")
    expected_value = "Harry Potter, J.K, Rowling"
    
    assert str(book) == expected_value


@pytest.mark.django_db
def test_dvd_model():
    client = Client()
    dvd = Dvd.objects.create(name="La Soupe aux choux", realisateur="Girault, Jean")
    expected_value = "La Soupe aux choux, Girault, Jean"

    assert str(dvd) == expected_value


@pytest.mark.django_db
def test_cd_model():
    client = Client()
    cd = Cd.objects.create(name="Happier Than Ever", artiste="Eilish, Billie")
    expected_value = "Happier Than Ever, Eilish, Billie"

    assert str(cd) == expected_value


@pytest.mark.django_db
def test_game_model():
    client = Client()
    game = JeuDePlateau.objects.create(name="Dice Forge", createur="Bonnessée, Régis")
    expected_value = "Dice Forge, Bonnessée, Régis"

    assert str(game) == expected_value


@pytest.mark.django_db
def test_user_model():
    client = Client()
    user = User.objects.create(username="JohnDoe", first_name="John", last_name="Doe", password="password123", is_staff=True)
    expected_value = "JohnDoe, Doe, John, True"

    assert str(user) == expected_value


@pytest.mark.django_db
def test_borrowing_model():
    user = User.objects.create(username="JohnDoe")

    media = Media.objects.create(name="Media_test")

    borrowing = Borrowing.objects.create(media=media, emprunteur=user, date=date.today())

    assert borrowing.media == media
    assert borrowing.emprunteur == user
    assert borrowing.date == date.today()