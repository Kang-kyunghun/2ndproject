# Generated by Django 3.1.1 on 2020-10-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_wishlist_vintage'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
