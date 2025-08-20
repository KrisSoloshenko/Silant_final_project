from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions

from .models import *
from .filters import *
from .forms import *
from .serializers import *


class MachineListView(ListView):
    model = Machine
    template_name = 'machine/machine_list.html'
    context_object_name = 'machines'
    ordering = ['shipment_date'] 
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            queryset = queryset
        elif user.groups.filter(name='Service').exists():
            queryset = queryset.filter(service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            queryset = queryset.filter(client=user.client)
        else:
            queryset = queryset
            
        self.filterset = MachineFilter(self.request.GET, queryset)
        
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       
       return context

class LoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name ='login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('machine-list')

    def form_invalid(self, form):
        messages.error(self.request,'Неправильный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))

def logout_view(request):  
    logout(request)  
    return redirect('/')

def error_view(request):
    return render(request, 'error.html')
    
class MachineDetailView(LoginRequiredMixin, DetailView):
    model = Machine
    template_name = 'machine/machine_detail.html'
    context_object_name = 'machine'
    
class MachineCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_machine'
    form_class = MachineForm
    model = Machine
    template_name = 'machine/machine_create.html'
    
class MachineUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_machine'
    form_class = MachineForm
    model = Machine
    template_name = 'machine/machine_create.html'

class MachineDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_machine'
    model = Machine
    success_url = reverse_lazy('machine-list')
    template_name = 'machine/machine_delete.html'
    
class TechnicModelDetailView(LoginRequiredMixin, DetailView):
    model = TechnicModel
    template_name = 'technic_model/technic_model_detail.html'
    context_object_name = 'technic_model'
    
class TechnicModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_technicmodel'
    form_class = TechnicModelForm
    model = TechnicModel
    template_name = 'technic_model/technic_model_create.html'

class TechnicModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_technicmodel'
    form_class = TechnicModelForm
    model = TechnicModel
    template_name = 'technic_model/technic_model_create.html'

class TechnicModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_technicmodel'
    model = TechnicModel
    success_url = reverse_lazy('machine-list')
    template_name = 'technic_model/technic_model_delete.html'
    context_object_name = 'technic_model_delete'
    
class EngineModelDetailView(LoginRequiredMixin, DetailView):
    model = EngineModel
    template_name = 'engine_model/engine_model_detail.html'
    context_object_name = 'engine_model'
    
class EngineModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_enginemodel'
    form_class = EngineModelForm
    model = EngineModel
    template_name = 'engine_model/engine_model_create.html'

class EngineModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_enginemodel'
    form_class = EngineModelForm
    model = EngineModel
    template_name = 'engine_model/engine_model_create.html'

class EngineModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_enginemodel'
    model = EngineModel
    success_url = reverse_lazy('machine-list')
    template_name = 'engine_model/engine_model_delete.html'
    context_object_name = 'engine_model_delete'
    
class TransmissionModelDetailView(LoginRequiredMixin, DetailView):
    model = TransmissionModel
    template_name = 'transmission_model/transmission_model_detail.html'
    context_object_name = 'transmission_model'
    
class TransmissionModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_transmissionmodel'
    form_class = TransmissionModelForm
    model = TransmissionModel
    template_name = 'transmission_model/transmission_model_create.html'

class TransmissionModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_transmissionmodel'
    form_class = TransmissionModelForm
    model = TransmissionModel
    template_name = 'transmission_model/transmission_model_create.html'

class TransmissionModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_transmissionmodel'
    model = TransmissionModel
    success_url = reverse_lazy('machine-list')
    template_name = 'transmission_model/transmission_model_delete.html'
    context_object_name = 'transmission_model_delete'
    
class DrivingAxleModelDetailView(LoginRequiredMixin, DetailView):
    model = DrivingAxleModel
    template_name = 'driving_axle/driving_axle_detail.html'
    context_object_name = 'driving_axle'
    
class DrivingAxleModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_drivingaxlemodel'
    form_class = DrivingAxleModelForm
    model = DrivingAxleModel
    template_name = 'driving_axle/driving_axle_create.html'

class DrivingAxleModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_drivingaxlemodel'
    form_class = DrivingAxleModelForm
    model = DrivingAxleModel
    template_name = 'driving_axle/driving_axle_create.html'

class DrivingAxleModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_drivingaxlemodel'
    model = DrivingAxleModel
    success_url = reverse_lazy('machine-list')
    template_name = 'driving_axle/driving_axle_delete.html'
    context_object_name = 'driving_axle_delete'
    
class SteerAxleModelDetailView(LoginRequiredMixin, DetailView):
    model = SteerAxleModel
    template_name = 'steer_axle/steer_axle_detail.html'
    context_object_name = 'steer_axle'
    
class SteerAxleModelCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_steeraxlemodel'
    form_class = SteerAxleModelForm
    model = SteerAxleModel
    template_name = 'steer_axle/steer_axle_create.html'

class SteerAxleModelUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_steeraxlemodel'
    form_class = SteerAxleModelForm
    model = SteerAxleModel
    template_name = 'steer_axle/steer_axle_create.html'

class SteerAxleModelDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_steeraxlemodel'
    model = SteerAxleModel
    success_url = reverse_lazy('machine-list')
    template_name = 'steer_axle/steer_axle_delete.html'
    context_object_name = 'steer_axle_delete'
    
class ServiceCompanyDetailView(LoginRequiredMixin, DetailView):
    model = ServiceCompany
    template_name = 'service_company/service_company_detail.html'
    context_object_name = 'service_company'
    
class ServiceCompanyCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_servicecompany'
    form_class = ServiceCompanyForm
    model = ServiceCompany
    template_name = 'service_company/service_company_create.html'

class ServiceCompanyUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_servicecompany'
    form_class = ServiceCompanyForm
    model = ServiceCompany
    template_name = 'service_company/service_company_create.html'

class ServiceCompanyDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_servicecompany'
    model = ServiceCompany
    success_url = reverse_lazy('machine-list')
    template_name = 'service_company/service_company_delete.html'
    context_object_name = 'service_company_delete'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client/client_detail.html'
    context_object_name = 'client'
    
class ClientCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_client'
    form_class = ClientForm
    model = Client
    template_name = 'client/client_create.html'

class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_client'
    form_class = ClientForm
    model = Client
    template_name = 'client/client_create.html'

class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_client'
    model = Client
    success_url = reverse_lazy('machine-list')
    template_name = 'client/client_delete.html'
    context_object_name = 'client_delete'

class MaintenanceListView(LoginRequiredMixin, ListView):
    model = Maintenance
    template_name = 'maintenance/maintenance_list.html'
    context_object_name = 'maintenances'
    ordering = ['maintenance_date'] 
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()

        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            queryset = queryset
        elif user.groups.filter(name='Service').exists():
            queryset = queryset.filter(machine__service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            queryset = queryset.filter(machine__client=user.client)
        else:
            queryset = queryset.none
            
        self.filterset = MaintenanceFilter(self.request.GET, queryset, request=self.request)
        
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       
       return context

class MaintenanceDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'silant_app.view_maintenance'
    model = Maintenance
    template_name = 'maintenance/maintenance_detail.html'
    context_object_name = 'maintenance'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(machine__service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
class MaintenanceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_maintenance'
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'maintenance/maintenance_create.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(machine__service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
class MaintenanceUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_maintenance'
    form_class = MaintenanceForm
    model = Maintenance
    template_name = 'maintenance/maintenance_create.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(machine__service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
class MaintenanceDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_maintenance'
    model = Maintenance
    success_url = reverse_lazy('maintenance-list')
    template_name = 'maintenance/maintenance_delete.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(machine__service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
class MaintenanceTypeDetailView(LoginRequiredMixin, DetailView):
    model = MaintenanceType
    template_name = 'maintenance_type/maintenance_type_detail.html'
    context_object_name = 'maintenance_type'
    
class MaintenanceTypeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_maintenancetype'
    form_class = MaintenanceTypeForm
    model = MaintenanceType
    template_name = 'maintenance_type/maintenance_type_create.html'

class MaintenanceTypeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_maintenancetype'
    form_class = MaintenanceTypeForm
    model = MaintenanceType
    template_name = 'maintenance_type/maintenance_type_create.html'

class MaintenanceTypeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_maintenancetype'
    model = MaintenanceType
    success_url = reverse_lazy('maintenance-list')
    template_name = 'maintenance_type/maintenance_type_delete.html'
    context_object_name = 'maintenance_type_delete'
    
class MaintenanceOrganizationDetailView(LoginRequiredMixin, DetailView):
    model = MaintenanceOrganization
    template_name = 'maintenance_organization/maintenance_organization_detail.html'
    context_object_name = 'maintenance_organization'
    
class MaintenanceOrganizationCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_maintenanceorganization'
    form_class = MaintenanceOrganizationForm
    model = MaintenanceOrganization
    template_name = 'maintenance_organization/maintenance_organization_create.html'

class MaintenanceOrganizationUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_maintenanceorganization'
    form_class = MaintenanceOrganizationForm
    model = MaintenanceOrganization
    template_name = 'maintenance_organization/maintenance_organization_create.html'

class MaintenanceOrganizationDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_maintenanceorganization'
    model = MaintenanceOrganization
    success_url = reverse_lazy('maintenance-list')
    template_name = 'maintenance_organization/maintenance_organization_delete.html'
    context_object_name = 'maintenance_organization_delete'
    
class ReclamationListView(LoginRequiredMixin, ListView):
    model = Reclamation
    template_name = 'reclamation/reclamation_list.html'
    context_object_name = 'reclamations'
    ordering = ['failure_date'] 
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()

        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            queryset = queryset
        elif user.groups.filter(name='Service').exists():
            queryset = queryset.filter(service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            queryset = queryset.filter(machine__client=user.client)
        else:
            queryset = queryset
            
        self.filterset = ReclamationFilter(self.request.GET, queryset, request=self.request)
        
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       
       return context
   
class ReclamationDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'silant_app.view_reclamation'
    model = Reclamation
    template_name = 'reclamation/reclamation_detail.html'
    context_object_name = 'reclamation'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
class ReclamationCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_reclamation'
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'reclamation/reclamation_create.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
class ReclamationUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_reclamation'
    form_class = ReclamationForm
    model = Reclamation
    template_name = 'reclamation/reclamation_create.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ReclamationDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_reclamation'
    model = Reclamation
    success_url = reverse_lazy('reclamation-list')
    template_name = 'reclamation/reclamation_delete.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Manager').exists():
            return queryset
        elif user.groups.filter(name='Service').exists():
            return queryset.filter(service_company=user.servicecompany)
        elif user.groups.filter(name='Client').exists():
            return queryset.filter(machine__client=user.client)
        else:
            return queryset.none

class FailureNodeDetailView(LoginRequiredMixin, DetailView):
    model = FailureNode
    template_name = 'failure_node/failure_node_detail.html'
    context_object_name = 'failure_node'
    
class FailureNodeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_failurenode'
    form_class = FailureNodeForm
    model = FailureNode
    template_name = 'failure_node/failure_node_create.html'

class FailureNodeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_failurenode'
    form_class = FailureNodeForm
    model = FailureNode
    template_name = 'failure_node/failure_node_create.html'

class FailureNodeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_failurenode'
    model = FailureNode
    success_url = reverse_lazy('reclamation-list')
    template_name = 'failure_node/failure_node_delete.html'
    context_object_name = 'failure_node_delete'
    
class RecoveryMethodDetailView(LoginRequiredMixin, DetailView):
    model = RecoveryMethod
    template_name = 'recovery_method/recovery_method_detail.html'
    context_object_name = 'recovery_method'
    
class RecoveryMethodCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'silant_app.add_recoverymethod'
    form_class = RecoveryMethodForm
    model = RecoveryMethod
    template_name = 'recovery_method/recovery_method_create.html'

class RecoveryMethodUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'silant_app.change_recoverymethod'
    form_class = RecoveryMethodForm
    model = RecoveryMethod
    template_name = 'recovery_method/recovery_method_create.html'

class RecoveryMethodDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'silant_app.delete_recoverymethod'
    model = RecoveryMethod
    success_url = reverse_lazy('reclamation-list')
    template_name = 'recovery_method/recovery_method_delete.html'
    context_object_name = 'recovery_method_delete'

class MachineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [permissions.IsAuthenticated]

class MaintenanceViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = Maintenance.objects.all()
   serializer_class = MaintenanceSerializer
   permission_classes = [permissions.IsAuthenticated]


class ReclamationViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = Reclamation.objects.all()
   serializer_class = ReclamationSerializer
   permission_classes = [permissions.IsAuthenticated]
