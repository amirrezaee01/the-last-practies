# Generated by Django 4.2.16 on 2024-12-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defualt.jpg', upload_to='blog/'),
        ),
    ]
