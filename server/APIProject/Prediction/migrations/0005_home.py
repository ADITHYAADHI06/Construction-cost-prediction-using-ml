# Generated by Django 3.2 on 2023-03-08 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prediction', '0004_jwt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='homes')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]