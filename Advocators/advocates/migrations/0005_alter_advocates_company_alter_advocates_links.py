# Generated by Django 4.1.2 on 2022-10-09 05:08

import advocates.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0004_alter_advocates_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocates',
            name='company',
            field=models.JSONField(default=advocates.models.company_content),
        ),
        migrations.AlterField(
            model_name='advocates',
            name='links',
            field=models.JSONField(default=advocates.models.links_content),
        ),
    ]
