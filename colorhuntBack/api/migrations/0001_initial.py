# Generated by Django 5.0.4 on 2024-04-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('color1', models.CharField(max_length=7)),
                ('color2', models.CharField(max_length=7)),
                ('color3', models.CharField(max_length=7)),
                ('color4', models.CharField(max_length=7)),
            ],
        ),
    ]
