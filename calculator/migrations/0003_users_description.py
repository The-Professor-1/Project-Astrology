# Generated by Django 5.1.3 on 2025-01-31 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_alter_users_mothersname_alter_users_selfname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
