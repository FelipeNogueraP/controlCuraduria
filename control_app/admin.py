from django.contrib import admin
from .models import (
    Tenant, Entity_User, Document, Procedure, Action, TimeStamp,
    Role, RolePermissions,
)


# Register your models here.

class ActionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name',
                         ]}),]
    list_display = ('name', 'id',)


class DocumentsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name', 'description',
                         ]}),]
    list_display = ('name', 'description', 'id',)


class EntityUserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['first_name', 'last_name', 
                         'tenant_id',
                         ]}),
        ]
    list_display = ('first_name', 'last_name', 'tenant_id', 'id',)
    #list_filter = ('id')
    #ordering = ('full_name', '-id')
    #search_fields = ('name')


class ProcedureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['procedure_type',]}),
        ('Details', {'fields':['user_id', 'document',]})
        ]
    list_display = ('procedure_type', 'document', 'user_id', 'id',)
    #list_filter = ('name')
    #search_fields = ('name')
      

class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name','description',]}),
        ('Details', {'fields':['permissions',]})
        ]
    list_display = ('name', 'description', 'permissions',)


class RolePermissionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['description',]}),
        ('Details', {'fields':['procedure_id','action_id',]})
        ]
    list_display = ('description', 'procedure_id','action_id',)
    #list_filter = ('name')
    #search_fields = ('name')


class TenantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name','user_id']}),
        ('Details', {'fields':['description','address']})
        ]
    list_display = ('name', 'user_id', 'description', 'address','id' )
    #list_filter = ('name')
    ordering = ('name', '-id')
    #search_fields = ('name')


class TimeStampAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['action_id','date']}),
        ('Details', {'fields':['user_id',]})
        ]
    list_display = ('action_id', 'date', 'user_id', 'id', )
    #list_filter = ('name')
    #ordering = ('date', '-id')
    #search_fields = ('name')


admin.site.register(Action, ActionAdmin)
admin.site.register(Document, DocumentsAdmin)
admin.site.register(Entity_User, EntityUserAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(RolePermissions, RolePermissionsAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(TimeStamp, TimeStampAdmin)


