from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tenant(models.Model):
    """Create the company user, aka tenant."""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=80)

    
class Entity_User(models.Model):
   #Create internal or external Users
    id = models.AutoField(primary_key=True)
    #role_id = models.ForeignKey(Role, on_delete=models.RESTRICT)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.RESTRICT)
    firs_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.title 

