# Generated by Django 2.2.7 on 2020-07-12 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_skill_skill_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skill_color',
        ),
    ]