from django_filters import FilterSet, filters
from .models import Machine, Maintenance, MaintenanceOrganization, ServiceCompany, Reclamation


class MachineFilter(FilterSet):
    class Meta:
        model = Machine
        fields = {
            'serial_number': ['exact'],
            'technic_model': ['exact'],
            'engine_model': ['exact'],
            'transmission_model': ['exact'],
            'driving_axle_model': ['exact'],
            'steer_axle_model': ['exact']
       }

def get_machines(request):
    if request is None:
        return Machine.objects.none()
    
    user = request.user
    if user.is_superuser or user.groups.filter(name='Manager').exists():
        return Machine.objects.all()
    elif user.groups.filter(name='Service').exists():
        return Machine.objects.filter(service_company=request.user.servicecompany).distinct()
    elif user.groups.filter(name='Client').exists():
        return Machine.objects.filter(client=request.user.client).distinct()
    else:
        None
        
def get_service_company(request):
    if request is None:
        return ServiceCompany.objects.none()
    
    user = request.user
    if user.is_superuser or user.groups.filter(name='Manager').exists():
        return ServiceCompany.objects.all()
    elif user.groups.filter(name='Service').exists():
        return ServiceCompany.objects.filter(id=request.user.servicecompany.id).distinct()
    elif user.groups.filter(name='Client').exists():
        return ServiceCompany.objects.filter(machine__client=request.user.client).distinct()
    else:
        return ServiceCompany.objects.none()
    
def get_maintenance_organizations(request):
    if request is None:
        return MaintenanceOrganization.objects.none()
    
    user = request.user
    if user.is_superuser or user.groups.filter(name='Manager').exists():
        return MaintenanceOrganization.objects.all()
    elif user.groups.filter(name='Service').exists():
        return MaintenanceOrganization.objects.filter(maintenance__machine__service_company=user.servicecompany).distinct()
    elif user.groups.filter(name='Client').exists():
        return MaintenanceOrganization.objects.filter(maintenance__machine__client=request.user.client).distinct()
    else:
        return MaintenanceOrganization.objects.none()

class MaintenanceFilter(FilterSet):
    machine = filters.ModelChoiceFilter(queryset=get_machines)
    maintenance_organization = filters.ModelChoiceFilter(queryset=get_maintenance_organizations)
    service_company = filters.ModelChoiceFilter(queryset=get_service_company)
    
    class Meta:
        model = Maintenance
        fields = {
            'maintenance_type': ['exact'],
            'machine': ['exact'],
            'service_company': ['exact'],
            'maintenance_organization': ['exact'],
       }

class ReclamationFilter(FilterSet):
    machine = filters.ModelChoiceFilter(queryset=get_machines)
    service_company = filters.ModelChoiceFilter(queryset=get_service_company)
    
    class Meta:
        model = Reclamation
        fields = {
            'failure_node': ['exact'],
            'recovery_method': ['exact'],
            'machine': ['exact'],
            'service_company': ['exact'],
       }
