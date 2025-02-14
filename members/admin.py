from django.contrib import admin
from .models import members

#control fields to display here 
class MemAdmin(admin.ModelAdmin):
    list_for_display = ("First name","Last name","Joined date")
admin.site.register(members,MemAdmin)