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
    geographic_location = models.ForeignKey(
        GeographicLocation, on_delete=models.DO_NOTHING)


class GeographicLocation(models.Model):
    """ Create Graphic Location its used in table General data """
    department = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    vereda = models.CharField(max_length=50)


class Request(models.Model):
    """ 1.0 IDENTIFICACION DE LA SOLICITUD """
    """ 1.9 CULTURAL BUILDING """
    cultural_building = models.BooleanField()


class BrRequestTypeProcedure(models.ManyToManyField):
    """ BRIDGE - REQUEST & 1.1 TIPO DE TRAMITE """
    request_id = models.ForeignKey(Request, on_delete=models.DO_NOTHING)
    type_procedure = models.ForeignKey(Request, on_delete=models.DO_NOTHING)


class TypeProcedure(models.Model):
    """ 1.1 TIPO DE TRAMITE """
    name = models.CharField(max_length=50)


class BrRequestProcedureObjective(models.ManyToManyField):
    """ BRIDGE - REQUEST & 1.2 OBJETO DEL TRAMITE """
    request_id = models.ForeignKey(Request, on_delete=models.DO_NOTHING)
    procedure_objective_id = models.ForeignKey(
        Request, on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)


class ProcedureObjective(models.Model):
    """ 1.2 OBJETO DEL TRAMITE """
    name = models.CharField(max_length=50)


class BrTypeProcedureModality(models.ManyToManyField):
    """BRIDGE - TYPEPROCEDURE & 1.3 MODALIDAD LICENCIA URBANIZACION, 1.4 MODALIDAD SUBDVISION, 1.5 MODALIDAD LICENCIA DE CONSTRUCCION"""
    type_procedure_id = models.ForeignKey(
        TypeProcedure, on_delete=models.DO_NOTHING)
    modality_id = models.ForeignKey(Modality, on_delete=models.DO_NOTHING)


class Modality(models.Model):
    """ 1.3 MODALIDAD LICENCIA URBANIZACION, 1.4 MODALIDAD SUBDVISION, 1.5 MODALIDAD LICENCIA DE CONSTRUCCION """
    name = models.CharField(max_length=50)


class BrRequestTypeUse(models.ManyToManyField):
    """ BRIDGE - REQUEST & 1.6 USOS """
    request_id = models.ForeignKey(Request, on_delete=models.DO_NOTHING)
    type_uses_id = models.ForeignKey(Request, on_delete=models.DO_NOTHING)


class Uses(models.Model):
    """ 1.6 USOS """
    name = models.CharField(max_length = 50)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)

class BrRequestBuildArea(models.ManyToManyField):
    """ BRIDGE - Request & 1.7 AREAS O UNIDADES CONSTRUIDAS """
    request_id = models.ForeignKey(Request, on_delete = models.DO_NOTHING)
    build_area_id = models.ForeignKey(BuildArea, on_delete = models.DO_NOTHING)


class BuildArea(models.Model):
    """ 1.8 AREAS O UNIDADES CONSTRUIDAS """
    name = models.CharField(max_length = 50)


class BrRequestHousingType(models.ManyToManyField):
    """ BRIDGE - Request & 1.8 TIPO DE VIVIENDA """
    request_id = models.ForeignKey(Request, on_delete = models.DO_NOTHING)
    housing_type = models.ForeignKey(Request, on_delete = models.DO_NOTHING)


class HousingType(models.Model):
    """ 1.8 TIPO DE VIVIENDA """
    name = models.CharField(max_length = 50)


class OtherDetail(models.Model):
    """ Other option detail to save details when selected option other """
    description = models.CharField(max_length=50)


class InstitutionalType(models.Model):
    """ 1.10 Tipo Institucional """
    name = models.CharField(max_length = 50)


class BrRequestInstitutionalType(models.ManyToManyField):
    """ BRIDGE - Request & 1.10 TIPO INSTITUCIONAL """
    request_id = models.ForeignKey(Request, on_delete = models.DO_NOTHING)
    institutional_type = models.ForeignKey(InstitutionalType, on_delete = models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)


class CommercialType(models.Model):
    """ 1.11 TIPO DE COMERCIO Y/O SERVICIOS """
    name = models.CharField(max_length = 50)


class BrRequestCommercialType(models.ManyToManyField):
    """ BRIDGE - Request & 1.11 TIPO DE COMERCIO """
    request_id = models.ForeignKey(Request, on_delete = models.DO_NOTHING)
    Commercial_Tipe_id = models.ForeignKey(CommercialType, on_delete = models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)


class Property(models.Model):
    """ 2.0 INFORMACIÓN SOBRE EL PREDIO """
    """ 2.1, 2.1, 2.3 DIRECCIÓN O NOMENCLATURA, MATRICULA INMOBILIARIA, No DE IDENTIFICACIÓN CATASTRAL """
    Property_id = models.ForeignKey(UniqueNationalForm, on_delete=models.DO_NOTHING)
    CurrentAddress = models.CharField(max_length=100)
    PreviousAddress = models.CharField(max_length=100)
    RealStateRegNum = models.CharField(max_length=50)
    Cadastral_id = models.CharField(max_length=50)


class SoilClasification(models.Model):
    """ 2.4 CLASIFICACIÓN DEL SUELO """
    name = models.CharField(max_length=50)


class BrPropertySoilClasification(models.ManyToManyField):
    """ BRIDGE - PROPERTY & 2.4 CLASIFICACIÓN DEL SUELO """
    Property_id = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    SoilClasification_id = models.ForeignKey(SoilClasification, on_delete=models.DO_NOTHING)


class Planimetry(models.Model):
    """ 2.5 PLANIMETRÍA DEL LOTE """
    name = models.CharField(max_length=50)


class BrPropertyPlanimetry(models.ManyToManyField):
    """ BRIDGE - PROPERTY & 2.5 PLANIMETRÍA DEL LOTE """
    Property_id = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    Planimetry_id = models.ForeignKey(Planimetry, on_delete=models.DO_NOTHING)


class Cadastral(models.Model):
    """ 2.6 INFORMACIÓN GENERAL """
    Number = models.CharField(max_length=50)
    Neighborhood = models.CharField(max_length=50)
    Vereda = models.CharField(max_length=50)
    Comuna = models.CharField(max_length=30)
    Sector = models.CharField(max_length=30)
    Estrato = models.CharField(max_length=20)
    Corregimiento = models.CharField(max_length=50)
    Manzana_Number = models.CharField(max_length=30)
    Lote_Number = models.CharField(max_length=30)
   

