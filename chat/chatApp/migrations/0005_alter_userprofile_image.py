# Generated by Django 4.1 on 2022-09-04 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0004_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='static/defaultimg.jpg', null=True, upload_to='profile_images'),
        ),
    ]
