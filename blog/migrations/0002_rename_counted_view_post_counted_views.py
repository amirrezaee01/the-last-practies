# Generated by Django 4.2.16 on 2024-11-27 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='counted_view',
            new_name='counted_views',
        ),
    ]
