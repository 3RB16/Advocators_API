# Generated by Django 4.1.2 on 2022-10-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0002_alter_advocates_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocates',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
