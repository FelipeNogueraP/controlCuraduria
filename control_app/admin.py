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
    fieldsets = [
        (None,{'fields':['name',
                         ]}),]
    list_display = ('name', 'id',)


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



############# NEW ADMIN MODELS #############


class UniqueNationalFormAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['request_id','property_id']}),
        ('Details', {'fields':['general_data_id', 'borders_dimension_areas', 
                               'licence_holder_responsible',
                                'professional_responsible', 'document_id', ]})
        ]
    list_display = ('request_id','property_id','general_data_id', 'borders_dimension_areas',
                     'licence_holder_responsible',
                                'professional_responsible', 'document_id' )
    #list_filter = ('name')
    #ordering = ('date', '-id')
    search_fields = ('property_id')

 
class GeneralDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['responsible_office','filing_number_consecutive']}),
        ('Details', {'fields':['filing_number_location', 'filing_number_curator', 
                               'filing_number_year',
                                'date', 'geographic_location_id', ]})
        ]
    list_display = ('responsible_office','filing_number_consecutive',
                    'filing_number_location', 'filing_number_curator', 
                               'filing_number_year',
                                'date', 'geographic_location_id',
                     )
    #list_filter = ('name')
    #ordering = ('date', '-id')
    search_fields = ('filing_number_consecutive')


class GeographicLocationAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,{'fields':['department','municipality', 'vereda']}),
            #('Details', {'fields':[ , ]})
            ]
    list_display = ('department','municipality', 'vereda',
                     )
    #list_filter = ('name')
    #ordering = ('date', '-id')
    #search_fields = ('department')


class RequestAdmin(admin.ModelAdmin):
    #fieldsets = [(None,{'fields':[,]}),
    #('Details', {'fields':[ , ]})]
    list_display = ('cultural_building, sustainable_declaration_id',
                     )
    #list_filter = ('name')
    #ordering = ('date', '-id')
    #search_fields = ('department')


class TypeProcedureAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class ProcedureObjectiveAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class ModalityAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class UsesAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,{'fields':['name','other_detail_id',]}),]
    list_display = ('name', 'other_detail_id'
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class BuildAreaAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class HousingTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class OtherDetailAdmin(admin.ModelAdmin):
    list_display = ('description',
                     )
    list_filter = ('description')
    ordering = ('description',)
    search_fields = ('description')    

class InstitutionalTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class CommercialTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name') 


class SustainableDeclarationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['ratio_wall_ceiling_id',]}),
        ('Details', {'fields':['water_saving_exp', 'energy_saving_exp', 
                               ]})
        ]
    list_display = ('ratio_wall_ceiling_id','water_saving_exp',
                    'energy_saving_exp', 
                     )
    #list_filter = ('')
    #ordering = ('', '')
    search_fields = ('ratio_wall_ceiling_id')
  

class RatioWallCeilingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['ceiling_height',]}),
        ('Details', {'fields':['north', 'south', 'east', 'west',
                               ]})
        ]
    list_display = ('ceiling_height','north', 'south', 'east', 'west',)
  

class MeasureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['measure_type_id', 'other_detail_id',
                               ]})
        ]
    list_display = ('name','measure_type_id', 'other_detail_id',)
      

class MeasureTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class MaterialityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name',]}),
        ('Details', {'fields':['materiality_type_id', 'other_detail_id',
                               ]})
        ]
    list_display = ('name','materiality_type_id', 'other_detail_id',)
      

class MaterialityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['cadastral_id','real_state_reg_num']}),
        ('Details', {'fields':['current_address', 'previous_address', 
                                ]})
        ]
    list_display = ('cadastral_id','real_state_reg_num','current_address', 'previous_address',
                     )
    list_filter = ('cadastral_id')
    ordering = ('cadastral_id', 'real_state_reg_num',)
    search_fields = ('cadastral_id')


class SoilClasificationAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')    


class PlanimetryAdmin(admin.ModelAdmin):
    list_display = ('name',
                     )
    list_filter = ('name')
    ordering = ('name',)
    search_fields = ('name')    


class CadastralAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['number',]}),
        ('Details', {'fields':['neighborhood', 'vereda', 'comuna','sector','estrato',
                               'corregimiento', 'manzana_number', 'lote_number',
                                ]})
        ]
    list_display = ('number','neighborhood', 'vereda', 'comuna','sector','estrato',
                               'corregimiento', 'manzana_number', 'lote_number',
                     )
    list_filter = ('number')
    ordering = ('neighborhood')
    search_fields = ('number')


class NeighborAdmin(admin.ModelAdmin):
    list_display = ('Housing_address', 'Mailing_address',
                     )
    ordering = ('Housing_address',)
    search_fields = ('Housing_address') 
   

class BordersDimensionAreasAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['TotalArea',]}),
        ('Details', {'fields':['Borders_n', 'Borders_s', 'Borders_e','Borders_w','Area_urbanized',
                               'Area_common', 'Area_parking',
                                ]})
        ]
    list_display = ('TotalArea', 'Borders_n', 'Borders_s', 'Borders_e','Borders_w','Area_urbanized',
                               'Area_common', 'Area_parking',
                     )
    list_filter = ('TotalArea')
    ordering = ('TotalArea')
    search_fields = ('TotalArea')


class NeighboringAdmin(admin.ModelAdmin):
    list_display = ('Neighbor_id', 'Length', 'Borders',
                     )
    list_filter = ('Neighbor_id')
    ordering = ('Length')
    search_fields = ('Borders')

   
class LicenceHolderResponsibleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['Name',]}),
        ('Details', {'fields':['Identification_num', 'Sign', 'Phone_number','Email',
                               'Electronic_notification',
                            ]})
        ]
    list_display = ('Name', 'Identification_num', 'Sign', 'Phone_number','Email',
                               'Electronic_notification',
                     )
    list_filter = ('Name')
    ordering = ('Identification_num')
    search_fields = ('Identification_num')


class ProfessionalResponsibleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['Profession_name_id',]}),
        ('Details', {'fields':['name', 'Identification_num', 'Professional_licence_num',
                               'Licence_expedition', 'Sign', 'Email', 'Required_review', 
                            ]})
        ]
    list_display = ('Profession_name_id', 'name', 'Identification_num', 'Professional_licence_num',
                               'Licence_expedition', 'Sign', 'Email', 'Required_review',
                     )
    list_filter = ('Profession_name_id')
    ordering = ('name')
    search_fields = ('Identification_num')


class ProfessionNameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['Name',]}),
        ('Details', {'fields':['Review_option', 
                               ]})
        ]
    list_display = ('name','Review_option',)
      

class PetitionResponsibleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['Name',]}),
        ('Details', {'fields':['Identification_num', 'Phone_num',
                               'mailing_address', 'Sign', 'Email', 
                            ]})
        ]
    list_display = ('Name', 'Profession_name_id', 'Identification_num', 'Phone_num',
                               'mailing_address', 'Sign', 'Email', 
                     )
    list_filter = ('Name')
    ordering = ('Identification_num')
    search_fields = ('Identification_num')


class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['name', 'description','mandatory'
                         ]}),]
    list_display = ('name', 'description', 'mandatory',)






admin.site.register(Action, ActionAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Entity_User, EntityUserAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(RolePermissions, RolePermissionsAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(UniqueNationalForm, UniqueNationalFormAdmin)
admin.site.register(GeneralData, GeneralDataAdmin)
admin.site.register(GeographicLocation, GeographicLocationAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(TypeProcedure, TypeProcedureAdmin)
admin.site.register(ProcedureObjective, ProcedureObjectiveAdmin)
admin.site.register(Modality, ModalityAdmin)
admin.site.register(Uses, UsesAdmin)
admin.site.register(BuildArea, BuildAreaAdmin)
admin.site.register(HousingType, HousingTypeAdmin)
admin.site.register(OtherDetail, OtherDetailAdmin)
admin.site.register(InstitutionalType, InstitutionalTypeAdmin)
admin.site.register(CommercialType, CommercialTypeAdmin)
admin.site.register(SustainableDeclaration, SustainableDeclarationAdmin)
admin.site.register(RatioWallCeiling, RatioWallCeilingAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(MeasureType, MeasureTypeAdmin)
admin.site.register(Materiality, MaterialityAdmin)
admin.site.register(MaterialityType, MaterialityTypeAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(SoilClasification, SoilClasificationAdmin)
admin.site.register(Planimetry, PlanimetryAdmin)
admin.site.register(Cadastral, CadastralAdmin)
admin.site.register(Neighbor, NeighborAdmin)
admin.site.register(Neighboring, NeighboringAdmin)
admin.site.register(LicenceHolderResponsible, LicenceHolderResponsibleAdmin)
admin.site.register(ProfessionalResponsible, ProfessionalResponsibleAdmin)
admin.site.register(ProfessionName, ProfessionNameAdmin)
admin.site.register(PetitionResponsible, PetitionResponsibleAdmin)


