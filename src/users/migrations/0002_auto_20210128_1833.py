# Generated by Django 2.2.8 on 2021-01-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='role',
            field=models.CharField(choices=[('PROFESSOR', 'professor'), ('STUDENT', 'student')], max_length=32),
        ),
    ]
