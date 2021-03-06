from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="30" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id','thumbnail','car_title','color','city','model','body_style','fuel_type','is_featured')
    list_display_links = ('thumbnail','id','car_title',)

    search_fields = ('city','car_title','color','model','body_style','fuel_type','is_featured')
    list_filter = ('color','fuel_type','city',)
    list_editable=('is_featured',)

admin.site.register(Car,CarAdmin)
