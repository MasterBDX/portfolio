# Generated by Django 2.2.7 on 2020-07-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_aboutme_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]