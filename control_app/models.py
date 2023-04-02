from django.db import models
from django.utils import timezone, dateformat
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
    # Create internal or external Users.
    id = models.AutoField(primary_key=True)
    # role_id = models.ForeignKey(Role, on_delete=models.RESTRICT)
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # full_name = (first_name, last_name)
    related_name = ("Entity User")

    def __str__(self):
        return (self.first_name)


class Document(models.Model):
    # Create a required document.
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Procedure(models.Model):
    # Create a procedure, like "new license".
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Entity_User, on_delete=models.DO_NOTHING)
    procedure_type = models.CharField(max_length=50)
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.procedure_type


class BridgeProcedureDocument(models.ManyToManyField):
    # Create relationship betwen Procedure and Document.
    id = models.AutoField(primary_key=True)
    procedure_id = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Entity_User, on_delete=models.CASCADE)
    hint = models.CharField(max_length=50)
    required = models.BooleanField(default=True)


class Action(models.Model):
    # Different actions that can be made.
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TimeStamp(models.Model):
    # Create a timestamp for changes.
    id = models.AutoField(primary_key=True)
    action_id = models.ForeignKey(Action, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(Entity_User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.action_id} - {self.date} - {self.user_id}"


class BridgeUserProcedure(models.ManyToManyField):
    # Create relationship betwen User and Procedure.
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Entity_User, on_delete=models.CASCADE)
    procedure_id = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    timeStamp_id = models.ForeignKey(TimeStamp, on_delete=models.CASCADE)


class RolePermissions(models.Model):
    # Create Permissions for diferent Roles
    id = models.AutoField(primary_key=True)
    procedure_id = models.ForeignKey(Procedure, on_delete=models.PROTECT)
    action_id = models.ForeignKey(Action, on_delete=models.PROTECT)
    description = models.CharField(max_length=100)
    # role_to_conceed_permissions = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return self.description


class Role(models.Model):
    # Create Roles for diferent users
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    permissions = models.ForeignKey(
        RolePermissions, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


############# New structure#####################
class UniqueNationalForm(models.Model):
    """Create national form"""
    general_data_id = models.ForeignKey(GeneralData, on_delete=models.CASCADE)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    borders_dimension_areas = models.ForeignKey(
        BordersDimensionAreas, on_delete=models.CASCADE)
    licence_holder_responsible = models.ForeignKey(
        LicenceHolderResponsible, on_delete=models.CASCADE)
    professional_responsible = models.ForeignKey(
        ProfessionalResponsible, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)

class GeneralData(models.Model):
    """Create the seccion 0 Datos Generales of form"""
    responsible_office = models.CharField(max_length=50)
    filing_number_location = models.IntegerField()
    filing_number_curator = models.IntegerField()
    filing_number_year = models.IntegerField()
    filing_number_consecutive = models.IntegerField()
    date = models.DateField()
    geographic_location = models.ForeignKey(GeographicLocation, on_delete=models.DO_NOTHING)



