# Generated by Django 4.0 on 2021-12-15 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share_place', '0003_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='full_name',
            new_name='Fullname',
        ),
    ]