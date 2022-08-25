from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    ordering = ('date',)
    search_fields  = ('title','email')



admin.site.register(Contact,ContactAdmin)