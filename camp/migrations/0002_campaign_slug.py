# Generated by Django 4.1.7 on 2023-04-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
