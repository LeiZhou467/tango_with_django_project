# Generated by Django 2.1.5 on 2021-07-31 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('content', models.CharField(max_length=128)),
            ],
        ),
    ]
