# Generated by Django 3.2 on 2023-03-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeprice',
            name='bath',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='homeprice',
            name='location',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='homeprice',
            name='sqft',
            field=models.FloatField(),
        ),
    ]