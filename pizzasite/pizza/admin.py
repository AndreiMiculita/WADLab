from django.contrib import admin
from django.db import models
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField
from django.forms import TextInput, Textarea

from .models import Product, Order, Article

MySpecialAdmin = lambda model: type('SubClass' + model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    #'list_select_related': [x.name for x in model._meta.fields if
     #                       isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField))]
})

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Article, YourModelAdmin)
admin.site.register(Product)
admin.site.register(Order, MySpecialAdmin(Order))
