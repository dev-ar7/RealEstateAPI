# Generated by Django 4.1.3 on 2022-11-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=175)),
                ('address', models.CharField(max_length=275)),
                ('city', models.CharField(max_length=125)),
                ('state', models.CharField(choices=[('BH', 'Bihar'), ('GU', 'Gujarat'), ('RCH', 'Ranchi'), ('KRL', 'Kerala'), ('H', 'Haryana'), ('KR', 'Karnataka'), ('JK', 'Jharkhand'), ('JAK', 'Jammu and Kashmir'), ('MP', 'Maharashtra'), ('BP', 'Bhopal'), ('P', 'Patna'), ('MP', 'Madya Pradesh'), ('HP', 'Himachal Pradesh'), ('AS', 'Assam'), ('G', 'Goa'), ('AP', 'Arunachal Pradesh'), ('CHG', 'Chhattisgarh'), ('AP', 'Andra Pradesh'), ('WB', 'West Bengal'), ('OD', 'Orissa'), ('Rp', 'Raipur'), ('HYD', 'Hyderabad')], default='WB', max_length=125)),
                ('zipcode', models.CharField(max_length=15)),
                ('desc', models.TextField(blank=True)),
                ('bedrooms', models.PositiveIntegerField(choices=[('2', 2), ('3', 3), ('1', 1), ('4', 4), ('5', 5)], default='2')),
                ('bathrooms', models.PositiveIntegerField()),
                ('garage', models.PositiveIntegerField(default=0)),
                ('sqft', models.DecimalField(decimal_places=2, max_digits=5)),
                ('plot_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('price', models.PositiveIntegerField(choices=[('400000', '₹400000'), ('600000', '₹600000'), ('800000', '₹800000'), ('900000', '₹900000'), ('500000', '₹500000'), ('50000', '₹50000'), ('100000', '₹100000'), ('1000000', '₹1000000'), ('300000', '₹300000'), ('200000', '₹200000'), ('700000', '₹700000')], default='50000')),
                ('pic_1', models.ImageField(upload_to='photos')),
                ('pic_2', models.ImageField(blank=True, upload_to='photos')),
                ('pic_3', models.ImageField(blank=True, upload_to='photos')),
                ('pic_4', models.ImageField(blank=True, upload_to='photos')),
                ('pic_5', models.ImageField(blank=True, upload_to='photos')),
                ('pic_6', models.ImageField(blank=True, upload_to='photos')),
                ('is_published', models.BooleanField(default=False)),
                ('publidhed_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
