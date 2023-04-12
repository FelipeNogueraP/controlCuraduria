"""Control App Models"""

from django.db import models
#from django.utils import timezone, dateformat


############# AUXILIARY ENTITIES #############


class OtherDetail(models.Model):
    """ Other option detail to save details when selected option other """
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


############# 0. DATOS GENERALES #############


class GeographicLocation(models.Model):
    """ Create Graphic Location its used in table General data """
    department = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    vereda = models.CharField(max_length=50)

    def __str__(self):
        return self.vereda


class GeneralData(models.Model):
    """Create the seccion 0 Datos Generales of form"""
    responsible_office = models.CharField(max_length=50)
    filing_number_location = models.IntegerField()
    filing_number_curator = models.IntegerField()
    filing_number_year = models.IntegerField()
    filing_number_consecutive = models.IntegerField()
    date = models.DateField()
    geographic_location_id = models.ForeignKey(
        GeographicLocation, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "General Data"

    def __str__(self) -> str:
        return self.responsible_office


############# 1.12 REGLAMENTACIÓN DE CONSTRUCCIÓN SOSTENIBLE #############


class RatioWallCeiling(models.Model):
    """ 1.12.5 RELACIÓN MURO VENTANA Y ALTURA PISO A TECHO """
    north = models.CharField(max_length = 3)
    south = models.CharField(max_length = 3)
    east = models.CharField(max_length = 3)
    west = models.CharField(max_length = 3)
    ceiling_height = models.CharField(max_length = 5)
    verbose_name = "Rel Muro/Ventana y altura Piso/Techo"

    def __str__(self) -> str:
        return self.verbose_name
    

class SustainableDeclaration(models.Model):
    """ 1.12 REGLAMENTACIÓN DE CONSTRUCCIÓN SOSTENIBLE """
    """ 1.12.1 DECLARACIÓN SOBRE MEDIDAS DE AHORRO EN ENERGÍA """
    ratio_wall_ceiling_id = models.ForeignKey(RatioWallCeiling, on_delete=models.DO_NOTHING)
    water_saving_exp = models.CharField(max_length = 20)
    energy_saving_exp = models.CharField(max_length = 20)
    verbose_name = "Declaración de sustentabilidad"

    def __str__(self) -> str:
        return self.verbose_name


class MeasureType(models.Model):
    """ Complement of the Measure class """
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name


class Measure(models.Model):
    """ 1.12.1.1 MEDIDAS PASIVAS, 1.12.1.2 MEDIDAS ACTIVAS """
    name = models.CharField(max_length = 100)
    measure_type_id = models.ForeignKey(MeasureType, on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name


class BrSustainableDeclarationMeasure(models.Model):
    """ BRIDGE - SustainableDeclaration & 1.12.1.1  MEDIDAS PASIVAS - 1.12.1.2 MEDIDAS ACTIVAS """
    sustainable_declaration_id = models.ManyToManyField(
        SustainableDeclaration, related_name="Sustainable Declaration Id+")
    measure_id = models.ManyToManyField(Measure, related_name="Measure Id+")


class MaterialityType(models.Model):
    """ Complement of the Materiality class """
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name


class Materiality(models.Model):
    """ 1.12.2 MATERIALIDAD MURO EXTERNO 1.12.3 MATERIALIDAD MURO INTERNO """
    name = models.CharField(max_length = 100)
    materiality_type_id = models.ForeignKey(MaterialityType, on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Materialities"

    def __str__(self) -> str:
        return self.name


class BrSustainableDeclarationMateriality(models.Model):
    """ BRIDGE - SustainableDeclaration & 1.12.2 MATERIALIDAD MURO EXTERNO
      1.12.3 MATERIALIDAD MURO INTERNO """
    sustainable_declaration_id = models.ManyToManyField(SustainableDeclaration,
                                                         related_name="Sustainable Declaration Id+")
    materiality_id = models.ManyToManyField(Materiality, related_name="Materiality Id+")


############# 1. IDENTIFICACIÓN DE LA SOLICITUD #############


class Request(models.Model):
    """ 1.0 IDENTIFICACION DE LA SOLICITUD """
    """ 1.9 CULTURAL BUILDING """
    cultural_building = models.BooleanField()
    sustainable_declaration_id = models.ForeignKey(
        SustainableDeclaration, on_delete = models.CASCADE)


class BrRequestTypeProcedure(models.Model):
    """ BRIDGE - REQUEST & 1.1 TIPO DE TRAMITE """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    type_procedure_id = models.ManyToManyField(Request, related_name="Type Procedure Id+")


class TypeProcedure(models.Model):
    """ 1.1 TIPO DE TRAMITE """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class BrRequestProcedureObjective(models.Model):
    """ BRIDGE - REQUEST & 1.2 OBJETO DEL TRAMITE """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    procedure_objective_id = models.ManyToManyField(Request, related_name="Procedure Objective Id+")
    other_detail_id = models.ManyToManyField(OtherDetail, related_name="Other Detail Id+")


class ProcedureObjective(models.Model):
    """ 1.2 OBJETO DEL TRAMITE """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Modality(models.Model):
    """ 1.3 MODALIDAD LICENCIA URBANIZACION, 
    1.4 MODALIDAD SUBDVISION, 1.5 MODALIDAD LICENCIA DE CONSTRUCCION """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Modalities"

    def __str__(self) -> str:
        return self.name


class BrTypeProcedureModality(models.Model):
    """BRIDGE - TYPEPROCEDURE & 1.3 MODALIDAD LICENCIA URBANIZACION,
      1.4 MODALIDAD SUBDVISION, 1.5 MODALIDAD LICENCIA DE CONSTRUCCION"""
    type_procedure_id = models.ManyToManyField(TypeProcedure,
                                               related_name="Type Procedure Id+")
    modality_id = models.ManyToManyField(Modality, related_name="Modality Id+")


class BrRequestUses(models.Model):
    """ BRIDGE - REQUEST & 1.6 USOS """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    type_uses_id = models.ManyToManyField(Request, related_name="Type Uses Id+")
    other_detail_id = models.ManyToManyField(
        OtherDetail, related_name="Other detail+")


class Uses(models.Model):
    """ 1.6 USOS """
    name = models.CharField(max_length = 50)

    class Meta:
        verbose_name_plural = "Uses"

    def __str__(self) -> str:
        return self.name


class BuildArea(models.Model):
    """ 1.8 AREAS O UNIDADES CONSTRUIDAS """
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name


class BrRequestBuildArea(models.Model):
    """ BRIDGE - Request & 1.7 AREAS O UNIDADES CONSTRUIDAS """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    build_area_id = models.ManyToManyField(BuildArea, related_name="Build Area Id+")


class BrRequestHousingType(models.Model):
    """ BRIDGE - Request & 1.8 TIPO DE VIVIENDA """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    housing_type_id = models.ManyToManyField(Request, related_name="Housing Type Id+")


class HousingType(models.Model):
    """ 1.8 TIPO DE VIVIENDA """
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class InstitutionalType(models.Model):
    """ 1.10 Tipo Institucional """
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class BrRequestInstitutionalType(models.Model):
    """ BRIDGE - Request & 1.10 TIPO INSTITUCIONAL """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    institutional_type_id = models.ManyToManyField(InstitutionalType,
                                                    related_name="Institutional Type Id+")
    other_detail_id = models.ManyToManyField(OtherDetail, related_name="Other Detail+")


class CommercialType(models.Model):
    """ 1.11 TIPO DE COMERCIO Y/O SERVICIOS """
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class BrRequestCommercialType(models.Model):
    """ BRIDGE - Request & 1.11 TIPO DE COMERCIO """
    request_id = models.ManyToManyField(Request, related_name="Request Id+")
    commercial_type_id = models.ManyToManyField(CommercialType, related_name="Commercial Type Id+")
    other_detail_id = models.ManyToManyField(OtherDetail, related_name="Other Detail Id+")


############# 2.0 INFORMACIÓN SOBRE EL PREDIO #############


class Cadastral(models.Model):
    """ 2.6 INFORMACIÓN GENERAL """
    number = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    vereda = models.CharField(max_length=50)
    comuna = models.CharField(max_length=30)
    sector = models.CharField(max_length=30)
    estrato = models.IntegerField()
    corregimiento = models.CharField(max_length=50)
    manzana_number = models.CharField(max_length=30)
    lote_number = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.number


class Property(models.Model):
    """ 2.1, 2.1, 2.3 DIRECCIÓN O NOMENCLATURA,
      MATRICULA INMOBILIARIA, No DE IDENTIFICACIÓN CATASTRAL """
    current_address = models.CharField(max_length=100)
    previous_address = models.CharField(max_length=100)
    real_state_reg_num = models.CharField(max_length=50)
    cadastral_id = models.ForeignKey(Cadastral, on_delete = models.DO_NOTHING)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class SoilClasification(models.Model):
    """ 2.4 CLASIFICACIÓN DEL SUELO """
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class BrPropertySoilClasification(models.Model):
    """ BRIDGE - PROPERTY & 2.4 CLASIFICACIÓN DEL SUELO """
    property_id = models.ManyToManyField(Property, related_name="Property Id+")
    soil_clasification_id = models.ManyToManyField(SoilClasification,
                                                    related_name="Soil Clasification Id+")


class Planimetry(models.Model):
    """ 2.5 PLANIMETRÍA DEL LOTE """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Planimetries"


class BrPropertyPlanimetry(models.Model):
    """ BRIDGE - PROPERTY & 2.5 PLANIMETRÍA DEL LOTE """
    property_id = models.ManyToManyField(Property, related_name="Property Id+")
    planimetry_id = models.ManyToManyField(Planimetry, related_name="Planimetry Id+")


############# 5. TITULARES Y PROFESIONALES RESPONSABLES #############


class LicenceHolderResponsible(models.Model):
    """ 5.1 TITULAR (ES) DE LA LICENCIA. """
    name = models.CharField(max_length=70)
    identification_num = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=40)
    electronic_notification = models.BooleanField(verbose_name="¿Acepta Notificación Electrónica?")
    sign = models.BooleanField(verbose_name="Firma")

    def __str__(self) -> str:
        return self.name


class ProfessionalResponsible(models.Model):
    """ 5.2 PROFESIONALES RESPONSABLES. """
    profession_name_id = models.CharField(max_length=70)
    name = models.CharField(max_length=100)
    identification_num = models.IntegerField()
    professional_licence_num = models.IntegerField()
    licence_expedition = models.DateField()
    email = models.EmailField(max_length=40)
    required_review = models.BooleanField(verbose_name="¿Exige Supervisión Tecnica?")
    sign = models.BooleanField(verbose_name="Firma")

    def __str__(self) -> str:
        return self.name


class ProfessionName(models.Model):
    """ COMPLEMENT OF THE ProfessionalResponsible CLASS """
    name = models.CharField(max_length=50)
    review_option = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name


class PetitionResponsible(models.Model):
    """ 5.3 RESPONSABLE DE LA SOLICITUD. """
    name = models.CharField(max_length=100)
    identification_num = models.IntegerField()
    phone_num = models.IntegerField()
    mailing_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    sign = models.BooleanField(verbose_name="Firma")

    def __str__(self) -> str:
        return self.name


############# 6. DOCUMENTOS QUE ACOMPAÑAN LA SOLICITUD. #############


class Document(models.Model):
    """ 6. DOCUMENTOS QUE ACOMPAÑAN LA SOLICITUD. """
    name = models.CharField(max_length=100)
    mandatory = models.BooleanField(verbose_name="¿Obligatorio?")
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class BrDocumentTypeProcedureModality(models.Model):
    """ BRIDGE - Document & 1.1 TIPO DE TRAMITE, MODALITY """
    document_id = models.ManyToManyField(Document, related_name="Document Id+")
    type_procedure_id = models.ManyToManyField(TypeProcedure, related_name="TypeProcedure Id+")
    modality_id =models.ManyToManyField(Modality, related_name="Modality Id+")


############# 4. LINDEROS, DIMENSIONES Y ÁREAS #############


class BordersDimensionAreas(models.Model):
    """ 4. LINDEROS, DIMENSIONES Y ÁREAS """
    borders_n = models.CharField(max_length=80)
    borders_s = models.CharField(max_length=80)
    borders_e = models.CharField(max_length=80)
    borders_w = models.CharField(max_length=80)
    area_urbanized = models.CharField(max_length=80)
    area_common = models.CharField(max_length=80)
    area_parking = models.CharField(max_length=80)
    total_area = models.CharField(max_length=80)

    class Meta:
        verbose_name_plural = "Borders Dimension Areas"

    def __str__(self) -> str:
        return self.total_area

############# FORMULARIO ÚNICO NACIONAL #############


class UniqueNationalForm(models.Model):
    """ Create national form"""
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


############# 3. INFORMACIÓN DE VECINOS COLINDANTES #############


class Neighbor(models.Model):
    """ 3 INFORMACIÓN DE VECINOS COLINDANTES. """
    housing_address = models.CharField(max_length=80)
    mailing_address = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.housing_address

class BrUniqueNationalFormNeighbor(models.Model):
    """ BRIDGE - Unique National Form & 3. INFORMACIÓN DE VECINOS COLINDANTES """
    unique_national_form_id = models.ManyToManyField(UniqueNationalForm,
                                                     related_name="Unique National Form Id+")
    neighbor_id = models.ManyToManyField(Neighbor, related_name="Neighbor Id+")


class Neighboring(models.Model):
    """ NEIGHBORING, COMPLEMENT OF THE BorderDimensionAreas CLASS """
    neighbor_id = models.ForeignKey(Neighbor, on_delete=models.DO_NOTHING)
    length = models.CharField(max_length=50)
    borders = models.CharField(max_length=50)
