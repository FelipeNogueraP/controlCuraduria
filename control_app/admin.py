"""Admin models for Control App"""

from django.contrib import admin
from .models import (
    UniqueNationalForm, GeneralData, GeographicLocation, Request,
    TypeProcedure, ProcedureObjective, Modality, Uses, BuildArea, HousingType, OtherDetail,
    InstitutionalType, CommercialType, SustainableDeclaration, RatioWallCeiling, Measure,
    MeasureType, Materiality, MaterialityType, Property, SoilClasification, Planimetry, Cadastral,
    Neighbor, BordersDimensionAreas, Neighboring, LicenceHolderResponsible, ProfessionalResponsible,
    ProfessionName, PetitionResponsible, Document,

)


# Register your models here.

class ActionAdmin(admin.ModelAdmin):
    "Admin class for Action"
    fieldsets = [
        (None,{'fields':['name',
                         ]}),]
    list_display = ('name', 'id',)


class EntityUserAdmin(admin.ModelAdmin):
    "Admin class for EntityUser"
    fieldsets = [
        (None,{'fields':['first_name', 'last_name',
                         'tenant_id',
                         ]}),
        ]
    list_display = ('first_name', 'last_name', 'tenant_id', 'id',)
    list_filter = ('id',)
    ordering = ('last_name', '-id',)
    search_fields = ('name',)


class ProcedureAdmin(admin.ModelAdmin):
    "Admin class for Procedure"
    fieldsets = [
        (None,{'fields':['procedure_type',]}),
        ('Details', {'fields':['user_id', 'document',]})
        ]
    list_display = ('procedure_type', 'document', 'user_id', 'id',)
    list_filter = ('name',)
    search_fields = ('name',)


class RoleAdmin(admin.ModelAdmin):
    "Admin class for Role"
    fieldsets = [
        (None,{'fields':['name','description',]}),
        ('Details', {'fields':['permissions',]})
        ]
    list_display = ('name', 'description', 'permissions',)


class RolePermissionsAdmin(admin.ModelAdmin):
    "Admin class for RolePermissions"
    fieldsets = [
        (None,{'fields':['description',]}),
        ('Details', {'fields':['procedure_id','action_id',]})
        ]
    list_display = ('description', 'procedure_id','action_id',)
    list_filter = ('name',)
    search_fields = ('name',)


class TenantAdmin(admin.ModelAdmin):
    "Admin class for Tenant"
    fieldsets = [
        (None,{'fields':['name','user_id']}),
        ('Details', {'fields':['description','address']})
        ]
    list_display = ('name', 'user_id', 'description', 'address','id' )
    list_filter = ('name',)
    ordering = ('name', '-id',)
    search_fields = ('name',)


class TimeStampAdmin(admin.ModelAdmin):
    "Admin class for Timestamp"
    fieldsets = [
        (None,{'fields':['action_id','date']}),
        ('Details', {'fields':['user_id',]})
        ]
    list_display = ('action_id', 'date', 'user_id', 'id', )
    list_filter = ('name',)
    #ordering = ('date', '-id')
    search_fields = ('name',)



############# NEW ADMIN MODELS #############


class UniqueNationalFormAdmin(admin.ModelAdmin):
    "Admin class for UniqueNationalForm"
    fieldsets = [
        (None,{'fields':['request_id','property_id']}),
        ('Details', {'fields':['general_data_id', 'borders_dimension_areas',
                               'licence_holder_responsible',
                                'professional_responsible', 'document_id', ]})
        ]
    list_display = ('request_id','property_id','general_data_id', 'borders_dimension_areas',
                     'licence_holder_responsible',
                                'professional_responsible', 'document_id' )
    list_filter = ('property_id', 'property_id',)
    #ordering = ('date', '-id')
    search_fields = ('property_id',)


class GeneralDataAdmin(admin.ModelAdmin):
    "Admin class for General Data"
    fieldsets = [
        (None,{'fields':['responsible_office',]}),
        ('Details', {'fields':['filing_number_location', 'filing_number_curator',
                               'filing_number_year','filing_number_consecutive',
                                'date', 'geographic_location_id', ]})
        ]
    list_display = ('responsible_office',
                    'filing_number_location', 'filing_number_curator', 
                               'filing_number_year','filing_number_consecutive',
                                'date', 'geographic_location_id',
                     )
    list_filter = ('filing_number_consecutive',)
    #ordering = ('date', '-id')
    search_fields = ('filing_number_consecutive',)
    verbose_name = "General Data"


class GeographicLocationAdmin(admin.ModelAdmin):
    "Admin class for GeographicLocation"
    fieldsets = [
            (None,{'fields':['department','municipality', 'vereda']}),
            #('Details', {'fields':[ , ]})
            ]
    list_display = ('department','municipality', 'vereda',
                     )
    #list_filter = (,)
    #ordering = ('date', '-id')
    search_fields = ('department',)


class RequestAdmin(admin.ModelAdmin):
    "Admin class for Request"
    fieldsets = [(None,{'fields':['sustainable_declaration_id', 'cultural_building', ]})]
    #('Details', {'fields':[ , ]})]
    list_display = ('cultural_building', 'sustainable_declaration_id',
                     )
    list_filter = ('cultural_building',)
    #ordering = ('date', '-id')
    search_fields = ('department',)


class CulturalTypeAdmin(admin.ModelAdmin):
    "Admin class for CulturalType"
    #fieldsets = [(None,{'fields':[,]}),
    #('Details', {'fields':[ , ]})]
    list_display = ('cultural_building',
                     )
    list_filter = ('cultural_building',)
    #ordering = ('date', '-id')
    search_fields = ()

class TypeProcedureAdmin(admin.ModelAdmin):
    "Admin class for TypeProcedure"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class ProcedureObjectiveAdmin(admin.ModelAdmin):
    "Admin class for ProcedureObective"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class ModalityAdmin(admin.ModelAdmin):
    "Admin class for Modality"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class UsesAdmin(admin.ModelAdmin):
    "Admin class for Uses"
    fieldsets = [
            (None,{'fields':['name',]}),]
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)
    verbose_name = "Uses"


class BuildAreaAdmin(admin.ModelAdmin):
    "Admin class for BuildArea"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class HousingTypeAdmin(admin.ModelAdmin):
    "Admin class for HousingType"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class OtherDetailAdmin(admin.ModelAdmin):
    "Admin class for OtherDetail"
    list_display = ('description',
                     )
    list_filter = ('description',)
    ordering = ('description',)
    search_fields = ('description',)

class InstitutionalTypeAdmin(admin.ModelAdmin):
    "Admin class for InstitutionalType"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class CommercialTypeAdmin(admin.ModelAdmin):
    "Admin class for CommercialType"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class SustainableDeclarationAdmin(admin.ModelAdmin):
    "Admin class for SustainableDeclaration"
    fieldsets = [
        (None,{'fields':['ratio_wall_ceiling_id',]}),
        ('Details', {'fields':['water_saving_exp', 'energy_saving_exp',
                               ]})
        ]
    list_display = ('ratio_wall_ceiling_id','water_saving_exp',
                    'energy_saving_exp', 
                     )
    list_filter = ('ratio_wall_ceiling_id','water_saving_exp',
                    'energy_saving_exp',)
    #ordering = ('', '')
    search_fields = ('ratio_wall_ceiling_id',)


class RatioWallCeilingAdmin(admin.ModelAdmin):
    "Admin class for RatioWallCeiling"
    fieldsets = [
        (None,{'fields':['ceiling_height',]}),
        ('Porcentaje del 0-100', {'fields':['north', 'south', 'east', 'west',
                               ]})
        ]
    list_display = ('id', 'ceiling_height','north', 'south', 'east', 'west',)


class MeasureAdmin(admin.ModelAdmin):
    "Admin class for Measure"
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['measure_type_id', 'other_detail_id',
                               ]})
        ]
    list_display = ('name','measure_type_id', 'other_detail_id',)


class MeasureTypeAdmin(admin.ModelAdmin):
    "Admin class for MeasureType"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class MaterialityAdmin(admin.ModelAdmin):
    "Admin class for Materiality"
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['materiality_type_id', 'other_detail_id',
                               ]})
        ]
    list_display = ('name','materiality_type_id', 'other_detail_id',)


class MaterialityTypeAdmin(admin.ModelAdmin):
    "Admin class for MaterialityType"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class PropertyAdmin(admin.ModelAdmin):
    "Admin class for Property"
    fieldsets = [
        (None,{'fields':['cadastral_id','real_state_reg_num']}),
        ('Details', {'fields':['current_address', 'previous_address',
                                ]})
        ]
    list_display = ('id', 'cadastral_id','real_state_reg_num','current_address', 'previous_address',
                     )
    list_filter = ('cadastral_id',)
    ordering = ('cadastral_id', 'real_state_reg_num',)
    search_fields = ('cadastral_id',)


class SoilClasificationAdmin(admin.ModelAdmin):
    "Admin class for SoilClasification"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class PlanimetryAdmin(admin.ModelAdmin):
    "Admin class for Planimetry"
    list_display = ('name',
                     )
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ('name',)


class CadastralAdmin(admin.ModelAdmin):
    "Admin class for Cadastral"
    fieldsets = [
        (None,{'fields':['number',]}),
        ('Details', {'fields':['neighborhood', 'vereda', 'comuna','sector','estrato',
                               'corregimiento', 'manzana_number', 'lote_number',
                                ]})
        ]
    list_display = ('number','neighborhood', 'vereda', 'comuna','sector','estrato',
                               'corregimiento', 'manzana_number', 'lote_number',
                     )
    list_filter = ('number',)
    ordering = ('neighborhood',)
    search_fields = ('number',)


class NeighborAdmin(admin.ModelAdmin):
    "Admin class for Neighbor"
    list_display = ('housing_address', 'mailing_address',
                     )
    ordering = ('housing_address',)
    search_fields = ('housing_address',)


class BordersDimensionAreasAdmin(admin.ModelAdmin):
    "Admin class for BordersDimensionAreas"
    fieldsets = [
        (None,{'fields':['total_area',]}),
        ('Details', {'fields':['borders_n', 'borders_s', 'borders_e','borders_w',
                               'area_urbanized', 'area_common', 'area_parking',
                                ]})
        ]
    list_display = ('total_area', 'borders_n', 'borders_s', 'borders_e',
                    'borders_w','area_urbanized',
                    'area_common', 'area_parking',
                     )
    list_filter = ('total_area',)
    ordering = ('total_area',)
    search_fields = ('total_area',)


class NeighboringAdmin(admin.ModelAdmin):
    "Admin class for Neighboring"
    list_display = ('neighbor_id', 'length', 'borders',
                     )
    list_filter = ('neighbor_id',)
    ordering = ('length',)
    search_fields = ('borders',)


class LicenceHolderResponsibleAdmin(admin.ModelAdmin):
    "Admin class for LicenceHolderResponsible"
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['identification_num', 'sign', 'phone_number',
                               'email','electronic_notification'
                            ]})
        ]
    list_display = ('name', 'identification_num', 'sign', 'phone_number','email',
                               'electronic_notification',
                     )
    list_filter = ('name',)
    ordering = ('identification_num',)
    search_fields = ('identification_num',)


class ProfessionalResponsibleAdmin(admin.ModelAdmin):
    "Admin class for ProfessionalREsponsible"
    fieldsets = [
        (None,{'fields':['profession_name_id',]}),
        ('Details', {'fields':['name', 'identification_num', 'professional_licence_num',
                               'licence_expedition', 'sign', 'email', 'required_review',
                            ]})
        ]
    list_display = ('id', 'name', 'profession_name_id', 'identification_num', 'professional_licence_num',
                               'licence_expedition', 'sign', 'email', 'required_review',
                     )
    list_filter = ('profession_name_id',)
    ordering = ('name',)
    search_fields = ('identification_num',)


class ProfessionNameAdmin(admin.ModelAdmin):
    "Admin class for ProfessionName"
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['review_option',
                               ]})
        ]
    list_display = ('id', 'name','review_option',)


class PetitionResponsibleAdmin(admin.ModelAdmin):
    "Admin class for PetitionResponsible"
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['identification_num', 'phone_num',
                               'mailing_address', 'sign', 'email', 
                            ]})
        ]
    list_display = ('name', 'identification_num', 'phone_num',
                               'mailing_address', 'sign', 'email', 
                     )
    list_filter = ('name',)
    ordering = ('identification_num',)
    search_fields = ('identification_num',)


class DocumentAdmin(admin.ModelAdmin):
    "Admin class for Document"
    fieldsets = [
        (None,{'fields':['name', 'description','mandatory'
                         ]}),]
    list_display = ('name', 'description', 'mandatory',)


admin.site.register(BuildArea, BuildAreaAdmin)
admin.site.register(BordersDimensionAreas, BordersDimensionAreasAdmin)
admin.site.register(Cadastral, CadastralAdmin)
admin.site.register(CommercialType, CommercialTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(GeneralData, GeneralDataAdmin)
admin.site.register(GeographicLocation, GeographicLocationAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(InstitutionalType, InstitutionalTypeAdmin)
admin.site.register(LicenceHolderResponsible, LicenceHolderResponsibleAdmin)
admin.site.register(MaterialityType, MaterialityTypeAdmin)
admin.site.register(Materiality, MaterialityAdmin)
admin.site.register(MeasureType, MeasureTypeAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(Modality, ModalityAdmin)
admin.site.register(Neighboring, NeighboringAdmin)
admin.site.register(Neighbor, NeighborAdmin)
admin.site.register(OtherDetail, OtherDetailAdmin)
admin.site.register(PetitionResponsible, PetitionResponsibleAdmin)
admin.site.register(Planimetry, PlanimetryAdmin)
admin.site.register(ProcedureObjective, ProcedureObjectiveAdmin)
admin.site.register(ProfessionName, ProfessionNameAdmin)
admin.site.register(ProfessionalResponsible, ProfessionalResponsibleAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(RatioWallCeiling, RatioWallCeilingAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(SoilClasification, SoilClasificationAdmin)
admin.site.register(SustainableDeclaration, SustainableDeclarationAdmin)
admin.site.register(TypeProcedure, TypeProcedureAdmin)
admin.site.register(UniqueNationalForm, UniqueNationalFormAdmin)
admin.site.register(Uses, UsesAdmin)
