# Generated by Django 3.0.3 on 2020-02-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.ImageField(upload_to='image'),
        ),
    ]
