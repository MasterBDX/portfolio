# Generated by Django 2.2.7 on 2020-02-06 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]