# Generated by Django 3.1.4 on 2021-11-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_models', '0023_auto_20211109_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_dependence',
            field=models.TextField(blank=True, help_text='服务依赖关系', null=True, verbose_name='服务依赖关系'),
        ),
    ]
