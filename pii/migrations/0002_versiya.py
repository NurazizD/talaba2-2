# Generated by Django 4.1.7 on 2023-03-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pii', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='versiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000000)),
            ],
        ),
    ]
