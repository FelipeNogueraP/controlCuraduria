from django.contrib import admin
from .models import (
    Tenant, Entity_User, Document, Procedure, Action, TimeStamp,
    Role, RolePermissions,
)


# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name','user_id']}),
        ('Details', {'fields':['description','address']})
        ]
    list_display = ('name', 'user_id', 'description', 'address','id' )
    #list_filter = ('name')
    ordering = ('name', '-id')
    #search_fields = ('name')

class Entity_UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['full_name', 
                         'tenant_id', 'id',
                         ]}),
        
        ]
    list_display = ('full_name', 'tenant_id', 'id' )
    #list_filter = ('id')
    ordering = ('name', '-id')
    #search_fields = ('name')



admin.site.register(Tenant, TenantAdmin)
admin.site.register(Entity_User)
admin.site.register(Document)
admin.site.register(Procedure)
admin.site.register(Action)
admin.site.register(TimeStamp)
admin.site.register(Role)
admin.site.register(RolePermissions)


