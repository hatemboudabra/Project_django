# Generated by Django 2.1.5 on 2023-05-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0002_auto_20230520_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisateur',
            name='categorie',
            field=models.CharField(choices=[('BOTOLAPRO', 'Botola PRO'), ('CoupeTrone ', 'Coupe du Trone'), ('RegionalFootballLeagues ', 'Regional Football Leagues'), ('AmateurFootballClub ', 'Amateur Football Club')], max_length=255),
        ),
    ]