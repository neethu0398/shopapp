# Generated by Django 5.0.1 on 2024-02-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]