import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=200)
    price_small = models.IntegerField(default=0)
    price_big = models.IntegerField(default=0)
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
    address = models.CharField(max_length=200)
    customer_comment = models.CharField(max_length=500)
    time_placed = models.DateTimeField('date order was placed')
    sent = models.BooleanField
    products = models.ManyToManyField(Product, through="Choice")


class Choice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.__str__()}{self.amount.__str__()}"
