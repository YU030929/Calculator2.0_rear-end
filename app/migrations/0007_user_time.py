# Generated by Django 4.2.5 on 2023-10-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_beilv_user_pipeizhuangtai_remove_user_tou1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.CharField(default='0', max_length=100),
        ),
    ]