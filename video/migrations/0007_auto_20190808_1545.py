# Generated by Django 2.2.1 on 2019-08-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20190808_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
