# Generated by Django 2.1.1 on 2018-09-04 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cea_login', models.CharField(max_length=30)),
                ('cima_login', models.CharField(max_length=30)),
            ],
        )
    ]