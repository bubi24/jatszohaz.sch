# Generated by Django 2.0.1 on 2018-01-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jatszohaz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jhuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
