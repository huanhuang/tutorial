# Generated by Django 4.0.3 on 2022-05-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_organization_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='data',
            field=models.JSONField(default="{'math':'90'}"),
        ),
    ]
