# Generated by Django 4.0.3 on 2022-04-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_solutions_user_problems_testcases'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserData',
        ),
    ]
