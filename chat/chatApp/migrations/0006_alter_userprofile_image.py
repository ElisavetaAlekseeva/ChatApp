# Generated by Django 4.1 on 2022-09-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0005_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='images/defaultimg.jpg', null=True, upload_to='profile_images'),
        ),
    ]
