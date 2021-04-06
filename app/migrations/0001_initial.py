# Generated by Django 3.1.7 on 2021-04-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
                ('imei_1', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=250)),
            ],
        ),
    ]