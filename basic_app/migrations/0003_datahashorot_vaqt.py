# Generated by Django 4.2.7 on 2023-11-11 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_alter_datahashorot_hashorot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datahashorot',
            name='vaqt',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
