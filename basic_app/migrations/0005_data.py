# Generated by Django 4.2.7 on 2023-11-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_datahashorot_vlajnost'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summa', models.CharField(max_length=250)),
                ('eggs', models.CharField(max_length=250)),
                ('lichinka', models.CharField(max_length=250)),
                ('dlyazrelix', models.CharField(max_length=250)),
                ('letat', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]