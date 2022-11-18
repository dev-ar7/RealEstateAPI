from django.db import models


BEDROOM_CHOICES = {
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
}

PRICE_CHOICES = {
    ('50000', '₹50000'),
    ('100000', '₹100000'),
    ('200000', '₹200000'),
    ('300000', '₹300000'),
    ('400000', '₹400000'),
    ('500000', '₹500000'),
    ('600000', '₹600000'),
    ('700000', '₹700000'),
    ('800000', '₹800000'),
    ('900000', '₹900000'),
    ('1000000', '₹1000000'),
}

STATE_CHOICES = {
    ('AP', 'Andra Pradesh'),
    ('HYD' , 'Hyderabad'),
    ('AP' , 'Arunachal Pradesh'),
    ('AS','Assam'),
    ('BH','Bihar'),
    ('P','Patna'),
    ('CHG','Chhattisgarh'),
    ('Rp','Raipur'),
    ('G', 'Goa'),
    ('GU','Gujarat'),
    ('H', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JAK'  , 'Jammu and Kashmir'),
    ('JK', 'Jharkhand'),
    ('RCH', 'Ranchi'),
    ('KR', 'Karnataka'),
    ('KRL' , 'Kerala'),
    ('MP' , 'Madya Pradesh'),
    ('BP' ,  'Bhopal'),
    ('MP','Maharashtra'),
    ('OD' ,  'Orissa'),
    ('WB' , 'West Bengal')
}


class Listing(models.Model):

    title = models.CharField(max_length=175)
    address = models.CharField(max_length=275)
    city = models.CharField(max_length=125)
    state = models.CharField(max_length=125, choices=STATE_CHOICES, default='WB')
    zipcode = models.CharField(max_length=15)
    desc = models.TextField(blank=True)
    bedrooms = models.PositiveIntegerField(choices=BEDROOM_CHOICES, default='2')
    bathrooms = models.PositiveIntegerField()
    garage = models.PositiveIntegerField(default=0)
    sqft = models.DecimalField(max_digits=5, decimal_places=2)
    plot_size = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.PositiveIntegerField(choices=PRICE_CHOICES, default='50000')
    pic_1 = models.ImageField(upload_to='photos')
    pic_2 = models.ImageField(upload_to='photos', blank=True)
    pic_3 = models.ImageField(upload_to='photos', blank=True)
    pic_4 = models.ImageField(upload_to='photos', blank=True)
    pic_5 = models.ImageField(upload_to='photos', blank=True)
    pic_6 = models.ImageField(upload_to='photos', blank=True)
    is_published = models.BooleanField(default=False)
    publidhed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.price}'