# Generated by Django 2.2.17 on 2020-11-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201119_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='NEW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancd', models.BigIntegerField()),
            ],
        ),
    ]