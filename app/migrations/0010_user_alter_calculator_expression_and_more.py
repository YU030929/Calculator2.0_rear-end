# Generated by Django 4.2.6 on 2023-10-21 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_calculator_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('chouma', models.IntegerField(default=1000)),
                ('xuan1', models.IntegerField(default=0)),
                ('xuan2', models.IntegerField(default=0)),
                ('xuan3', models.IntegerField(default=0)),
                ('xuan4', models.IntegerField(default=0)),
                ('xuan5', models.IntegerField(default=0)),
                ('lishijilu', models.TextField(default='')),
                ('pipeizhuangtai', models.IntegerField(default=0)),
                ('time', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'app_users',
            },
        ),
        migrations.AlterField(
            model_name='calculator',
            name='expression',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='calculator',
            name='result',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='calculator',
            table='app_Calculator',
        ),
    ]
