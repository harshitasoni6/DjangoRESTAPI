from django.contrib import admin

# Register your models here.
from api.models import Company,Employee
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_location', 'company_type')
    search_fields = ('name',)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('company',)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
