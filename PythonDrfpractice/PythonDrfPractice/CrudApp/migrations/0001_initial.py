# Generated by Django 4.0.3 on 2022-04-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'RegisterTable',
            },
        ),
    ]
