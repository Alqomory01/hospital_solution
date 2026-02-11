from django.contrib import admin
from .models import *

class ServiceItemAdmin(admin.ModelAdmin):
     list_display = ('name', 'price') 
     search_fields = ('name',) 
class InvoiceItemInline(admin.TabularInline): 
    model = InvoiceItem 
    extra = 1 
class InvoiceAdmin(admin.ModelAdmin): 
    list_display = ('id', 'patient', 'doctor', 'date', 'total_amount', 'status') 
    list_filter = ('status', 'date') 
    search_fields = ('patient__name', 'doctor__user__first_name', 'doctor__user__last_name') 
    inlines = [InvoiceItemInline] 
class PaymentAdmin(admin.ModelAdmin): 
    list_display = ('invoice', 'amount_paid', 'method', 'date') 
    list_filter = ('method', 'date') 
    search_fields = ('invoice__patient__name',) 
    
admin.site.register(ServiceItem, ServiceItemAdmin) 
admin.site.register(Invoice, InvoiceAdmin) 
admin.site.register(Payment, PaymentAdmin)
# Register your models here.
