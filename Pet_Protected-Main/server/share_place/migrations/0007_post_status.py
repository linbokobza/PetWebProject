# Generated by Django 4.0 on 2021-12-26 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share_place', '0006_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share_place.product'),
        ),
    ]