# Generated by Django 2.0.1 on 2018-04-18 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jatszohaz', '0005_auto_20180416_2348'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jhuser',
            options={'permissions': (('view_all', 'View all user details'), ('basic_admin', 'Basic admin rights'), ('leader_admin', 'Group leader rights'))},
        ),
    ]
