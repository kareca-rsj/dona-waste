# Generated by Django 4.1 on 2023-07-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('datetime_created', models.DateTimeField()),
                ('weight_grams', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
