# Generated by Django 3.0.6 on 2020-06-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='decription',
            field=models.TextField(default=''),
        ),
    ]
