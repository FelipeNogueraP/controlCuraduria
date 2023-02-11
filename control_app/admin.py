from django.contrib import admin
from .models import Tenant

# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name','user_id']}),
        ('Details', {'fields':['description','address']})
        ]
    list_display = ('name', 'user_id', 'description', 'address','id' )


admin.site.register(Tenant, TenantAdmin)
