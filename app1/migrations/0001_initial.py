# Generated by Django 2.2.7 on 2020-02-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.IntegerField()),
                ('mobile', models.BigIntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
