from django.contrib import admin
from first_app.models import Employe, Developer, Designer, BussinesAnalyst


# Register your models here.
@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('EmployeID', 'Name', 'Designation',
                    'Email', 'JoiningDate', 'created_at', 'updated_at')


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('employe', 'Technology', 'DefaultSalary')


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ('employe', 'Technology', 'DefaultSalary')


@admin.register(BussinesAnalyst)
class BaAdmin(admin.ModelAdmin):
    list_display = ('employe', 'Tool', 'DefaultSalary')
