# Generated by Django 4.0.2 on 2022-04-14 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yardSite', '0005_review_reviewer_alter_review_rating_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pending',
            field=models.BooleanField(default=False),
        ),
    ]
