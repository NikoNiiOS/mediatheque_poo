# Generated by Django 5.1.3 on 2024-11-13 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrowing', '0001_initial'),
        ('media', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='emprunteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='media.media'),
        ),
    ]
