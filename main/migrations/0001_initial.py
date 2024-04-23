# Generated by Django 3.2.12 on 2024-04-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('numberOfSuns', models.IntegerField(default=0)),
                ('preparationTimeNeeded', models.IntegerField()),
                ('preparationItself', models.TextField()),
                ('equipment', models.ManyToManyField(to='main.Equipment')),
                ('ingredients', models.ManyToManyField(to='main.Ingredient')),
            ],
        ),
    ]
