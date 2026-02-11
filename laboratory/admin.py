from django.contrib import admin
from .models import *

class LabTestAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'department') 
    search_fields = ('name', 'department') 
    list_filter = ('department',)

class LabResultInline(admin.StackedInline): 
    model = LabResult 
    extra = 0    
class LabRequestAdmin(admin.ModelAdmin): 
    list_display = ('patient', 'doctor', 'test', 'date_requested', 'status') 
    list_filter = ('status', 'date_requested', 'test__department') 
    search_fields = ('patient__name', 'doctor__user__first_name', 'doctor__user__last_name', 'test__name') 
    inlines = [LabResultInline] 
class LabResultAdmin(admin.ModelAdmin): 
    list_display = ('request', 'verified_by', 'date_completed') 
    search_fields = ('request__patient__name', 'request__test__name', 'verified_by__user__first_name', 'verified_by__user__last_name') 
    list_filter = ('date_completed',) 
    
admin.site.register(LabTest, LabTestAdmin) 
admin.site.register(LabRequest, LabRequestAdmin) 
admin.site.register(LabResult, LabResultAdmin)    
# Register your models here.
