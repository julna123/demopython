# Generated by Django 4.1.7 on 2023-03-05 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='name1',
        ),
    ]