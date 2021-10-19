from django.contrib import admin
from django.forms import ModelChoiceField
from django import forms

from .models import *

#отображение в админке только ноутбуков при добавлении ноутбуков

class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebook'))
        return super().formfield_for_foreignkey(self, db_field, request, **kwargs)
#отображение в админке только телефонов при добавлении ноутбуков

class SmartphoneAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(self, db_field, request, **kwargs)

admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone,SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
