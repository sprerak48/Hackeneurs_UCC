# Generated by Django 2.0.2 on 2018-06-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flyer',
            name='owner',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
