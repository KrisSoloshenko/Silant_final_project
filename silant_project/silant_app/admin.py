from django.contrib import admin
from .models import *

admin.site.register(TechnicModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DrivingAxleModel)
admin.site.register(SteerAxleModel)
admin.site.register(MaintenanceType)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
admin.site.register(ServiceCompany)
admin.site.register(MaintenanceOrganization)
admin.site.register(Client)

class MachineAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Manager').exists():
            return qs
        elif hasattr(request.user, 'client'):
            return qs.filter(client__user=request.user)
        elif hasattr(request.user, 'servicecompany'):
            return qs.filter(service_company__user=request.user)

admin.site.register(Machine, MachineAdmin)

class MaintenanceAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Manager').exists():
            return qs
        if hasattr(request.user, 'client'):
            return qs.filter(machine__client__user=request.user)
        elif hasattr(request.user, 'servicecompany'):
            return qs.filter(machine__service_company__user=request.user)

admin.site.register(Maintenance, MaintenanceAdmin)

class ReclamationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Manager').exists():
            return qs
        if hasattr(request.user, 'client'):
            return qs.filter(machine__client__user=request.user)
        elif hasattr(request.user, 'servicecompany'):
            return qs.filter(machine__service_company__user=request.user)

admin.site.register(Reclamation, ReclamationAdmin)
