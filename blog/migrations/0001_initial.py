# Generated by Django 4.1.7 on 2023-03-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=700)),
                ('body', models.TextField()),
                ('img', models.CharField(max_length=3000)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]