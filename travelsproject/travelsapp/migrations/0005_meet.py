# Generated by Django 4.1.7 on 2023-03-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0004_alter_team_img1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics1')),
                ('descr', models.TextField()),
            ],
        ),
    ]