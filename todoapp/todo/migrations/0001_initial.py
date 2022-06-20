# Generated by Django 3.2.4 on 2022-05-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]