import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    link_str = models.SlugField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.product_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        self.link_str = slugify(self.product_name)
        self.pub_date = timezone.now()

        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=1)
    address = models.CharField(max_length=200)
    customer_comment = models.CharField(max_length=500)
    time_placed = models.DateTimeField('date order was placed')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=1)
    amount = models.IntegerField(default=0)
    ORDERED = 'OR'
    PREPARING = 'PR'
    SENT = 'SN'
    RECEIVED = 'RC'
    STATE_CHOICES = (
        (ORDERED, 'Ordered'),
        (PREPARING, 'Preparing'),
        (SENT, 'Sent'),
        (RECEIVED, 'Received'),
    )
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=ORDERED,
    )

    def __str__(self):
        return dict(self.STATE_CHOICES)[self.state] + "| Address: " + self.address + " " + self.customer_comment

