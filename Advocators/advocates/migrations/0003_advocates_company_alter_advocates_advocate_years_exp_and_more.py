# Generated by Django 4.1.2 on 2022-10-09 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0002_advocates_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocates',
            name='company',
            field=models.JSONField(default={'href': '', 'id': '', 'logo': '', 'name': ''}),
        ),
        migrations.AlterField(
            model_name='advocates',
            name='advocate_years_exp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='advocates',
            name='profile_pic',
            field=models.ImageField(unique=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='advocates',
            name='short_bio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]