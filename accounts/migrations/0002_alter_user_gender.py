# Generated by Django 4.1.3 on 2022-11-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('O', 'Others'), ('F', 'Female')], max_length=1),
        ),
    ]
