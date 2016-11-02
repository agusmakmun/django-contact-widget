from django.contrib import admin
from contact_widget.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'created']
    search_fields = ['email', 'subject']
    list_filter = ['created', ]
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)
