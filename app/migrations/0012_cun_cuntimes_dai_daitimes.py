# Generated by Django 4.2.6 on 2023-10-22 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_cun_dai_alter_calculator_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='cun',
            name='Cuntimes',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dai',
            name='Daitimes',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
