# Generated by Django 3.2.4 on 2022-12-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=32, verbose_name='城市名称'),
        ),
    ]
