# Generated by Django 2.2.8 on 2021-01-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210128_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
