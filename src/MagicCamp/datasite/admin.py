from django.contrib import admin
from MagicCamp.datasite.models import *

class ServicesAdmin(admin.ModelAdmin):
    list_display  = ('lng','title','season','desc','date_out','date_in','price')
    search_fields = ('desc',)
    list_filter   = ('date_out',)
    ordering      = ('date_out',)
    fields        = ('lng','title','desc','season','date_out','date_in','price')

admin.site.register(News)
admin.site.register(Directions)
admin.site.register(Services,ServicesAdmin)
admin.site.register(Vogatie)
admin.site.register(Info)