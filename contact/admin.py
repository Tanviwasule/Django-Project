from django.contrib import admin
from contact.models import contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name1', 'email', 'phone', 'message', 'website')


admin.site.register(contact)
# Register your models here.
