from django.contrib import admin
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField

from .models import Product, Order

MySpecialAdmin = lambda model: type('SubClass' + model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    #'list_select_related': [x.name for x in model._meta.fields if
     #                       isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField))]
})

admin.site.register(Product)
admin.site.register(Order, MySpecialAdmin(Order))
