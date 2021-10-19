from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django import forms
from .models import *
from PIL import Image

class NotebookAdminForm(ModelForm):
    MIN_RESOLUTION = (400,400)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].help_text = 'Загружайте изображение с мин разрешением {}x{}'.format(*self.MIN_RESOLUTION)
    def clean_image(self):
        image = self.cleaned_data['image']
        img= Image.open(image)
        # print(img.width, img.height)
        min_height,min_width = self.MIN_RESOLUTION
        if img.height <min_height or img.width < min_width:
            raise ValidationError ('Разрешение изображения меньше минимального')

        return image

#отображение в админке только ноутбуков при добавлении ноутбуков

class NotebookAdmin(admin.ModelAdmin):
    form = NotebookAdminForm
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
