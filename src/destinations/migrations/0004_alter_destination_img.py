# Generated by Django 4.0.5 on 2022-07-01 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0003_destination_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='media/pics'),
        ),
    ]