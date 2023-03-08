from django.contrib import admin
from .models import Tenant, Entity_User

# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name','user_id']}),
        ('Details', {'fields':['description','address']})
        ]
    list_display = ('name', 'user_id', 'description', 'address','id' )
    #list_filter = ('id')
    ordering = ('name', '-id')
    #search_fields = ('name')

#class Entity_user_Admin(admin.ModelAdmin):
#   list_per_page = 20



admin.site.register(Tenant, TenantAdmin)
