# Generated by Django 4.0.5 on 2022-06-29 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_destination_oferta_alter_destination_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='precio',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
