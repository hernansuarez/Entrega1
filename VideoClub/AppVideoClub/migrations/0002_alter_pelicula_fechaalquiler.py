# Generated by Django 4.0.6 on 2022-08-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVideoClub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='fechaAlquiler',
            field=models.DateField(),
        ),
    ]
