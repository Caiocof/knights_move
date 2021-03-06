# Generated by Django 4.0.1 on 2022-01-05 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KnightAudits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=70)),
                ('type_piece', models.CharField(max_length=20)),
                ('posisiton', models.CharField(max_length=2)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 1, 5, 14, 10, 31, 514169))),
            ],
            options={
                'verbose_name': 'KnightAudit',
            },
        ),
        migrations.CreateModel(
            name='Pieces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Piece',
            },
        ),
    ]
