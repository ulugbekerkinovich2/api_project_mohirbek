# Generated by Django 4.2.7 on 2023-11-11 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datahashorot',
            name='hashorot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basic_app.hashorot'),
        ),
        migrations.AlterField(
            model_name='datahashorot',
            name='statistica',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
