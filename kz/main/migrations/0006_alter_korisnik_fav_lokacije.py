# Generated by Django 4.1.4 on 2022-12-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnik',
            name='fav_lokacije',
            field=models.ManyToManyField(blank=True, to='main.lokacija'),
        ),
    ]
