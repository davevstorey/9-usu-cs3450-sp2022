# Generated by Django 3.2.7 on 2022-04-07 12:30

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_owner(apps, schema_editor):
    User = apps.get_model('accounts', 'CustomUser')
    owner = User(username='owner', email='owner@yardwrk.com', is_superuser=True, is_staff=True)
    owner.password = make_password('password')
    owner.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_owner)
    ]