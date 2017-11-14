import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Variety(models.Model):
    question_text = models.CharField(max_length=200)
    question_desc = models.CharField(max_length=200)
    link_str = models.SlugField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        self.link_str = slugify(self.question_text)

        super(Variety, self).save(*args, **kwargs)


class Order(models.Model):
    address = models.CharField(max_length=200)
    time_placed = models.DateTimeField('date order was placed')
    products = models.ManyToManyField(Variety, through="Choice")


class Choice(models.Model):
    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.variety.__str__() + self.amount.__str__()
