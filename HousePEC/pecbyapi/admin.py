from django.contrib import admin

from pecbyapi.models import HouseBuilder, HouseBasic, HouseSpec

# Register your models here.

class HouseBasicInline(admin.StackedInline):
    model = HouseBasic
    extra = 0

class HouseBuilderAdmin(admin.ModelAdmin):
    inlines = [HouseBasicInline]
    list_display = ('user', 'name', 'get_date_joined', 'get_registered_houses')
    list_filter = ['user']
    search_fields = ['user']

class HouseSpecInline(admin.StackedInline):
    model = HouseSpec
    extra = 0

class HouseBasicAdmin(admin.ModelAdmin):
    inlines = [HouseSpecInline]
    list_display = (
        'builder', 'name', 'create_date', 'update_date', 
        'region', 'annual_solar_level', 
        'total_area', 'ldk_area', 'oth_area', 
        'total_envelope_area', 'ua_value', 'winter_ha_value', 'summer_ha_value', 
        'get_registered_specs',
        )
    list_filter = ['builder']
    search_fields = ['builder']

class HouseSpecAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 
        'heating_system', 'ldk_heating_type', 'oth_heating_type', 'hotwater_heating_system', 'hotwater_heating_source_type', 
        'cooling_system', 'ldk_cooling_type', 'oth_cooling_type', 
        'ventilation_type', 'ventilation_heatexchanger', 'ventilation_heatexchanger_efficiency', 
        'water_heater_type', 
        'ldk_lighting', 
        'oth_lighting', 
        'nonldk_lighting', 
        'photovoltaic', 
        'cogene', 
        )

admin.site.register(HouseBuilder, HouseBuilderAdmin)
admin.site.register(HouseBasic, HouseBasicAdmin)
admin.site.register(HouseSpec, HouseSpecAdmin)
