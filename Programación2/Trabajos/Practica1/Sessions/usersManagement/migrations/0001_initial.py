# Generated by Django 3.1.5 on 2021-04-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
