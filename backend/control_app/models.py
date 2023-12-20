"""Control App Models"""

from django.db import models
#from django.utils import timezone, dateformat


############# AUXILIARY ENTITIES #############


class OtherDetail(models.Model):
    """ Other option detail to save details when selected option other """
    description = models.CharField(max_length=50)
    br_request_procedure_obj = models.ManyToManyField(
        'Request', through='BrRequestProcedureObjective', blank=True)
    br_request_uses = models.ManyToManyField(
        'Uses', through='BrRequestUses', blank=True)    
    br_request_institutionalType = models.ManyToManyField(
        'InstitutionalType', through='BrRequestInstitutionalType', blank=True)
    br_request_commercialType = models.ManyToManyField(
        'CommercialType', through='BrRequestCommercialType', blank=True)

    def __str__(self):
        return self.description


############# 0. DATOS GENERALES #############


class GeographicLocation(models.Model):
    """ Create Graphic Location its used in table General data """
    department = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    vereda = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk}'


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
        return f'{self.pk}'


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
        return f'{self.pk}'


class MeasureType(models.Model):
    """ Complement of the Measure class """
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Measure(models.Model):
    """ 1.12.1.1 MEDIDAS PASIVAS, 1.12.1.2 MEDIDAS ACTIVAS """
    name = models.CharField(max_length = 100)
    measure_type_id = models.ForeignKey(MeasureType, on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, on_delete=models.DO_NOTHING)
    br_sustainable_measure = models.ManyToManyField(
        'SustainableDeclaration', through='BrSustainableDeclarationMeasure', blank=True)

    def __str__(self) -> str:
        return self.name


class SustainableDeclaration(models.Model):
    """ 1.12 REGLAMENTACIÓN DE CONSTRUCCIÓN SOSTENIBLE """
    """ 1.12.1 DECLARACIÓN SOBRE MEDIDAS DE AHORRO EN ENERGÍA """
    ratio_wall_ceiling_id = models.ForeignKey(RatioWallCeiling, on_delete=models.DO_NOTHING)
    water_saving_exp = models.CharField(max_length = 20)
    energy_saving_exp = models.CharField(max_length = 20)
    verbose_name = "Declaración de sustentabilidad"
    br_sustainable_measure = models.ManyToManyField(
        Measure, through='BrSustainableDeclarationMeasure', blank=True)
    br_materiality = models.ManyToManyField(
        'Materiality', through='BrSustainableDeclarationMateriality', blank=True)

    def __str__(self):
        return f'{self.pk}'


class BrSustainableDeclarationMeasure(models.Model):
    """ BRIDGE - SustainableDeclaration & 1.12.1.1  MEDIDAS PASIVAS - 1.12.1.2 MEDIDAS ACTIVAS """
    sustainable_declaration_id = models.ForeignKey(
        SustainableDeclaration, on_delete=models.DO_NOTHING)
    measure_id = models.ForeignKey(
        Measure, on_delete=models.DO_NOTHING, related_name= "Medida o mecanismo+")

    class Meta:
        unique_together = ('sustainable_declaration_id', 'measure_id')

    def __str__(self):
        return f'{self.measure_id}, {self.sustainable_declaration_id}'


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
    br_sustainable = models.ManyToManyField(
        'SustainableDeclaration', through='BrSustainableDeclarationMateriality', blank=True)

    class Meta:
        verbose_name_plural = "Materialities"

    def __str__(self) -> str:
        return self.name


class BrSustainableDeclarationMateriality(models.Model):
    """ BRIDGE - SustainableDeclaration & 1.12.2 MATERIALIDAD MURO EXTERNO
      1.12.3 MATERIALIDAD MURO INTERNO """
    sustainable_declaration_id = models.ForeignKey(SustainableDeclaration,
                                                         related_name="Sustainable Declaration Id+",
                                                          on_delete=models.DO_NOTHING)
    materiality_id = models.ForeignKey(Materiality, related_name="Materiality Id+",
                                            on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('sustainable_declaration_id', 'materiality_id')

    def __str__(self):
        return f'{self.materiality_id}, {self.sustainable_declaration_id}'


############# 1. IDENTIFICACIÓN DE LA SOLICITUD #############


class Request(models.Model):
    """ 1.0 IDENTIFICACION DE LA SOLICITUD """
    """ 1.9 CULTURAL BUILDING """
    cultural_building = models.BooleanField()
    sustainable_declaration_id = models.ForeignKey(
        SustainableDeclaration, on_delete = models.CASCADE)
    br_type_procedure = models.ManyToManyField(
        'TypeProcedure', through='BrRequestTypeProcedure', blank=True)
    br_procedure_objective = models.ManyToManyField(
        'ProcedureObjective', through='BrRequestProcedureObjective', blank=True)
    br_request_uses = models.ManyToManyField(
        'Uses', through='BrRequestUses', blank=True)
    br_request_buildArea = models.ManyToManyField(
        'BuildArea', through='BrRequestBuildArea', blank=True)
    br_request_housingType = models.ManyToManyField(
        'Housingtype', through='BrRequestHousingType', blank=True)    
    br_request_institutionalType = models.ManyToManyField(
        'InstitutionalType', through='BrRequestInstitutionalType', blank=True)
    br_request_commercialType = models.ManyToManyField(
        'CommercialType', through='BrRequestCommercialType', blank=True)


class TypeProcedure(models.Model):
    """ 1.1 TIPO DE TRAMITE """
    name = models.CharField(max_length=100)
    br_request = models.ManyToManyField(
        'Request', through='BrRequestTypeProcedure', blank=True)
    br_typeProcedure_modality = models.ManyToManyField(
        'Modality', through='BrTypeProcedureModality', blank=True)    
    br_document_typeProcedure_modality = models.ManyToManyField(
        'Document', through='BrDocumentTypeProcedureModality', blank=True)

    def __str__(self) -> str:
        return self.name


class BrRequestTypeProcedure(models.Model):
    """ BRIDGE - REQUEST & 1.1 TIPO DE TRAMITE """
    request_id = models.ForeignKey(Request,
                                   related_name="Request Id+", on_delete=models.DO_NOTHING)
    type_procedure_id = models.ForeignKey(TypeProcedure,
                                          related_name="Type Procedure Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'type_procedure_id')

    def __str__(self):
        return f'{self.request_id}, {self.type_procedure_id}'


class ProcedureObjective(models.Model):
    """ 1.2 OBJETO DEL TRAMITE """
    name = models.CharField(max_length=50)
    br_request_procedure_obj = models.ManyToManyField(
        'Request', through='BrRequestProcedureObjective', blank=True)

    def __str__(self) -> str:
        return self.name


class BrRequestProcedureObjective(models.Model):
    """ BRIDGE - REQUEST & 1.2 OBJETO DEL TRAMITE """
    request_id = models.ForeignKey(Request, related_name="Request Id+", on_delete=models.DO_NOTHING)
    procedure_objective_id = models.ForeignKey(ProcedureObjective,
                                               related_name="Procedure Objective Id+", on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(OtherDetail,
                                        related_name="Other Detail Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'procedure_objective_id', 'other_detail_id')

    def __str__(self):
        return f'{self.request_id}, {self.procedure_objective_id}, {self.other_detail_id}'


class Modality(models.Model):
    """ 1.3 MODALIDAD LICENCIA URBANIZACION, 
    1.4 MODALIDAD SUBDVISION, 1.5 MODALIDAD LICENCIA DE CONSTRUCCION """
    name = models.CharField(max_length=50)
    br_typeProcedure_modality = models.ManyToManyField(
        'TypeProcedure', through='BrTypeProcedureModality', blank=True)
    br_document_typeProcedure_modality = models.ManyToManyField(
        'Document', through='BrDocumentTypeProcedureModality', blank=True)

    class Meta:
        verbose_name_plural = "Modalities"

    def __str__(self) -> str:
        return self.name


class BrTypeProcedureModality(models.Model):
    """BRIDGE - TYPEPROCEDURE & 1.3 MODALIDAD LICENCIA URBANIZACION,
      1.4 MODALIDAD SUBDVISION, 1.5 MODALIDAD LICENCIA DE CONSTRUCCION"""
    type_procedure_id = models.ForeignKey(TypeProcedure,
                                               related_name="Type Procedure Id+", on_delete=models.DO_NOTHING)
    modality_id = models.ForeignKey(Modality,
                                    related_name="Modality Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('type_procedure_id', 'modality_id')

    def __str__(self):
        return f'{self.type_procedure_id}, {self.modality_id}'


class BrRequestUses(models.Model):
    """ BRIDGE - REQUEST & 1.6 USOS """
    request_id = models.ForeignKey(Request,
                                   related_name="Request Id+", on_delete=models.DO_NOTHING)
    type_uses_id = models.ForeignKey("Uses",
                                     related_name="Type Uses Id+", on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(
        OtherDetail, related_name="Other detail+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'type_uses_id', 'other_detail_id')

    def __str__(self):
        return f'{self.request_id}, {self.type_uses_id}, {self.other_detail_id}'


class Uses(models.Model):
    """ 1.6 USOS """
    name = models.CharField(max_length = 50)
    br_request_uses = models.ManyToManyField(
        'Request', through='BrRequestUses', blank=True)

    class Meta:
        verbose_name_plural = "Uses"

    def __str__(self) -> str:
        return self.name


class BuildArea(models.Model):
    """ 1.8 AREAS O UNIDADES CONSTRUIDAS """
    name = models.CharField(max_length = 100)
    br_request_buildArea = models.ManyToManyField(
        'Request', through='BrRequestBuildArea', blank=True)

    def __str__(self) -> str:
        return self.name


class BrRequestBuildArea(models.Model):
    """ BRIDGE - Request & 1.7 AREAS O UNIDADES CONSTRUIDAS """
    request_id = models.ForeignKey(Request,
                                   related_name="Request Id+", on_delete=models.DO_NOTHING)
    build_area_id = models.ForeignKey(BuildArea,
                                      related_name="Build Area Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'build_area_id',)

    def __str__(self):
        return f'{self.request_id}, {self.build_area_id}'


class HousingType(models.Model):
    """ 1.8 TIPO DE VIVIENDA """
    name = models.CharField(max_length = 50)
    br_request_housingType = models.ManyToManyField(
        'Request', through='BrRequestHousingType', blank=True)

    def __str__(self) -> str:
        return self.name


class BrRequestHousingType(models.Model):
    """ BRIDGE - Request & 1.8 TIPO DE VIVIENDA """
    request_id = models.ForeignKey(Request, related_name="Request Id+",
                                        on_delete=models.DO_NOTHING)
    housing_type_id = models.ForeignKey(HousingType,
                                         related_name="Housing Type Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'housing_type_id',)

    def __str__(self):
        return f'{self.request_id}, {self.housing_type_id}'


class InstitutionalType(models.Model):
    """ 1.10 Tipo Institucional """
    name = models.CharField(max_length = 50)
    br_request_housingType = models.ManyToManyField(
        'Request', through='BrRequestInstitutionalType', blank=True)

    def __str__(self) -> str:
        return self.name


class BrRequestInstitutionalType(models.Model):
    """ BRIDGE - Request & 1.10 TIPO INSTITUCIONAL """
    request_id = models.ForeignKey(Request,
                                   related_name="Request Id+", on_delete=models.DO_NOTHING)
    institutional_type_id = models.ForeignKey(InstitutionalType,
                                                    related_name="Institutional Type Id+",
                                                    on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(OtherDetail, related_name="Other Detail+",
                                        on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'institutional_type_id', 'other_detail_id')

    def __str__(self):
        return f'{self.request_id}, {self.institutional_type_id}, {self.other_detail_id}'


class CommercialType(models.Model):
    """ 1.11 TIPO DE COMERCIO Y/O SERVICIOS """
    name = models.CharField(max_length = 50)
    br_request_commercialType = models.ManyToManyField(
        'Request', through='BrRequestCommercialType', blank=True)

    def __str__(self) -> str:
        return self.name


class BrRequestCommercialType(models.Model):
    """ BRIDGE - Request & 1.11 TIPO DE COMERCIO """
    request_id = models.ForeignKey(Request,
                                   related_name="Request Id+", on_delete=models.DO_NOTHING)
    commercial_type_id = models.ForeignKey(CommercialType,
                                           related_name="Commercial Type Id+", on_delete=models.DO_NOTHING)
    other_detail_id = models.ForeignKey(OtherDetail,
                                        related_name="Other Detail Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('request_id', 'commercial_type_id', 'other_detail_id')

    def __str__(self):
        return f'{self.request_id}, {self.commercial_type_id}, {self.other_detail_id}'


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
        return f'{self.pk}'


class Property(models.Model):
    """ 2.1, 2.1, 2.3 DIRECCIÓN O NOMENCLATURA,
      MATRICULA INMOBILIARIA, No DE IDENTIFICACIÓN CATASTRAL """
    current_address = models.CharField(max_length=100)
    previous_address = models.CharField(max_length=100)
    real_state_reg_num = models.CharField(max_length=50)
    cadastral_id = models.ForeignKey(Cadastral, on_delete = models.DO_NOTHING)
    br_property_soilClasification = models.ManyToManyField(
        'SoilClasification', through='BrPropertySoilClasification', blank=True)
    br_property_planimetry = models.ManyToManyField(
        'Planimetry', through='BrPropertyPlanimetry', blank=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self) -> str:
        return f'{self.pk}'


class SoilClasification(models.Model):
    """ 2.4 CLASIFICACIÓN DEL SUELO """
    name = models.CharField(max_length=50)
    br_property_soilClasification = models.ManyToManyField(
        'Property', through='BrPropertySoilClasification', blank=True)

    def __str__(self) -> str:
        return self.name


class BrPropertySoilClasification(models.Model):
    """ BRIDGE - PROPERTY & 2.4 CLASIFICACIÓN DEL SUELO """
    property_id = models.ForeignKey(Property,
                                         related_name="Property Id+", on_delete=models.DO_NOTHING)
    soil_clasification_id = models.ForeignKey(SoilClasification,
                                            related_name="Soil Clasification Id+",
                                           on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('property_id', 'soil_clasification_id',)

    def __str__(self):
        return f'{self.property_id}, {self.soil_clasification_id}'


class Planimetry(models.Model):
    """ 2.5 PLANIMETRÍA DEL LOTE """
    name = models.CharField(max_length=50)
    br_property_planimetry = models.ManyToManyField(
        'Property', through='BrPropertyPlanimetry', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Planimetries"


class BrPropertyPlanimetry(models.Model):
    """ BRIDGE - PROPERTY & 2.5 PLANIMETRÍA DEL LOTE """
    property_id = models.ForeignKey(Property,
                                    related_name="Property Id+", on_delete=models.DO_NOTHING)
    planimetry_id = models.ForeignKey(Planimetry,
                                      related_name="Planimetry Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('property_id', 'planimetry_id',)

    def __str__(self):
        return f'{self.property_id}, {self.planimetry_id}'


############# 5. TITULARES Y PROFESIONALES RESPONSABLES #############


class LicenceHolderResponsible(models.Model):
    """ 5.1 TITULAR (ES) DE LA LICENCIA. """
    name = models.CharField(max_length=70)
    identification_num = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    electronic_notification = models.BooleanField(verbose_name="¿Acepta Notificación Electrónica?")
    sign = models.BooleanField(verbose_name="Firma")

    def __str__(self) -> str:
        return f'{self.pk}'


class ProfessionalResponsible(models.Model):
    """ 5.2 PROFESIONALES RESPONSABLES. """
    profession_name_id = models.ForeignKey("ProfessionName", related_name="Profession Name+", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    identification_num = models.CharField(max_length=30)
    professional_licence_num = models.CharField(max_length=30,verbose_name="Prof Lic Num")
    licence_expedition = models.DateField()
    email = models.EmailField(max_length=40)
    required_review = models.BooleanField(verbose_name="¿Exige Supervisión Tecnica?")
    sign = models.BooleanField(verbose_name="Firma")

    def __str__(self) -> str:
        return f'{self.pk}'


class ProfessionName(models.Model):
    """ COMPLEMENT OF THE ProfessionalResponsible CLASS """
    name = models.CharField(max_length=50)
    review_option = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name


class PetitionResponsible(models.Model):
    """ 5.3 RESPONSABLE DE LA SOLICITUD. """
    name = models.CharField(max_length=100)
    identification_num = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    mailing_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    sign = models.BooleanField(verbose_name="Firma")

    def __str__(self) -> str:
        return self.name


############# 6. DOCUMENTOS QUE ACOMPAÑAN LA SOLICITUD. #############


class Document(models.Model):
    """ 6. DOCUMENTOS QUE ACOMPAÑAN LA SOLICITUD. """
    name = models.CharField(max_length=300)
    mandatory = models.BooleanField(verbose_name="¿Obligatorio?")
    description = models.CharField(max_length=600)
    br_document_typeProcedure_modality = models.ManyToManyField(
        'TypeProcedure', through='BrDocumentTypeProcedureModality', blank=True)

    def __str__(self) -> str:
        return f'{self.pk}'


class BrDocumentTypeProcedureModality(models.Model):
    """ BRIDGE - Document & 1.1 TIPO DE TRAMITE, MODALITY """
    document_id = models.ForeignKey(Document,
                                        related_name="Document Id+", on_delete=models.DO_NOTHING)
    type_procedure_id = models.ForeignKey(TypeProcedure,
                                    related_name="TypeProcedure Id+", on_delete=models.DO_NOTHING)
    modality_id =models.ForeignKey(Modality,
                                        related_name="Modality Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('document_id', 'type_procedure_id', 'modality_id')

    def __str__(self):
        return f'{self.document_id}, {self.type_procedure_id}, {self.modality_id}'


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
    petition_responsible = models.ForeignKey(
        PetitionResponsible, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    br_uniqueNatForm_Neighbor = models.ManyToManyField(
        'Neighbor', through='BrUniqueNationalFormNeighbor', blank=True)

    def __str__(self) -> str:
        return f'{self.pk}'


############# 3. INFORMACIÓN DE VECINOS COLINDANTES #############


class Neighbor(models.Model):
    """ 3 INFORMACIÓN DE VECINOS COLINDANTES. """
    housing_address = models.CharField(max_length=80)
    mailing_address = models.CharField(max_length=80)
    br_uniqueNatForm_Neighbor = models.ManyToManyField(
        'UniqueNationalForm', through='BrUniqueNationalFormNeighbor', blank=True)

    def __str__(self) -> str:
        return self.housing_address


class BrUniqueNationalFormNeighbor(models.Model):
    """ BRIDGE - Unique National Form & 3. INFORMACIÓN DE VECINOS COLINDANTES """
    unique_national_form_id = models.ForeignKey(UniqueNationalForm,
                                                     related_name="Unique National Form Id+",
                                                     on_delete=models.DO_NOTHING)
    neighbor_id = models.ForeignKey(Neighbor,
                                related_name="Neighbor Id+", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('unique_national_form_id', 'neighbor_id',)

    def __str__(self):
        return f'{self.unique_national_form_id}, {self.neighbor_id}'


class Neighboring(models.Model):
    """ NEIGHBORING, COMPLEMENT OF THE BorderDimensionAreas CLASS """
    neighbor_id = models.ForeignKey(Neighbor, on_delete=models.DO_NOTHING)
    length = models.CharField(max_length=50)
    borders = models.CharField(max_length=50)
