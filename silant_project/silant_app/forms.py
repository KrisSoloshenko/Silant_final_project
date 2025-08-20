from django import forms
from .models import *


class MachineForm(forms.ModelForm):
   class Meta:
       model = Machine
       fields = '__all__'
       
class TechnicModelForm(forms.ModelForm):
   class Meta:
       model = TechnicModel
       fields = '__all__'

class EngineModelForm(forms.ModelForm):
    class Meta:
        model = EngineModel
        fields = '__all__'

class TransmissionModelForm(forms.ModelForm):
    class Meta:
        model = TransmissionModel
        fields = '__all__'

class DrivingAxleModelForm(forms.ModelForm):
    class Meta:
        model = DrivingAxleModel
        fields = '__all__'

class SteerAxleModelForm(forms.ModelForm):
    class Meta:
        model = SteerAxleModel
        fields = '__all__'

class ServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = ServiceCompany
        fields = '__all__'
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets = {
            'operating_time': forms.NumberInput(),
            'order_number': forms.TextInput(),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
            
        if user:
            if user.groups.filter(name='Client').exists():
                self.fields['machine'].queryset = Machine.objects.filter(client__user=user).distinct()
                self.fields['service_company'].queryset = ServiceCompany.objects.filter(machine__client__user=user).distinct()
            elif user.groups.filter(name='Service').exists():
                self.fields['machine'].queryset = Machine.objects.filter(service_company__user=user).distinct()
                self.fields['service_company'].queryset = ServiceCompany.objects.filter(id=user.servicecompany.id).distinct()
            elif user.is_superuser or user.groups.filter(name="Manager").exists():
                self.fields['machine'].queryset = Machine.objects.all()
                self.fields['service_company'].queryset = ServiceCompany.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        maintenance_date = cleaned_data.get('maintenance_date')
        order_date = cleaned_data.get('order_date')
        if maintenance_date and order_date:
            if maintenance_date < order_date:
                self.add_error('order_date',"Дата проведения ТО не может быть раньше даты оформления заказ-наряда")
        return cleaned_data
        
    def save(self, commit=True):
        instance = super().save(commit=False)            
        if commit:
            instance.save()
        return instance
        
class MaintenanceTypeForm(forms.ModelForm):
    class Meta:
        model = MaintenanceType
        fields = '__all__'
        
class MaintenanceOrganizationForm(forms.ModelForm):
    class Meta:
        model = MaintenanceOrganization
        fields = '__all__'

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = '__all__'
        exclude = ['downtime']
        widgets = {
            'operating_time': forms.NumberInput(),
            'failure_description': forms.TextInput(),
            'spare_parts': forms.TextInput(),
        }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
            
        if user:
            if user.groups.filter(name='Client').exists():
                self.fields['machine'].queryset = Machine.objects.filter(client__user=user).distinct()
                self.fields['service_company'].queryset = ServiceCompany.objects.filter(machine__client__user=user).distinct()
            elif user.groups.filter(name='Service').exists():
                self.fields['machine'].queryset = Machine.objects.filter(service_company__user=user).distinct()
                self.fields['service_company'].queryset = ServiceCompany.objects.filter(id=user.servicecompany.id).distinct()
            elif user.is_superuser or user.groups.filter(name="Manager").exists():
                self.fields['machine'].queryset = Machine.objects.all()
                self.fields['service_company'].queryset = ServiceCompany.objects.all()
                
    def clean(self):
        cleaned_data = super().clean()
        recovery_date = cleaned_data.get('recovery_date')
        failure_date = cleaned_data.get('failure_date')
        if recovery_date and failure_date:
            if recovery_date < failure_date:
                self.add_error('recovery_date',"Дата восстановления не может быть раньше даты отказа")
        return cleaned_data
        
    def save(self, commit=True):
        instance = super().save(commit=False)            
        if commit:
            instance.save()
        return instance

class FailureNodeForm(forms.ModelForm):
    class Meta:
        model = FailureNode
        fields = '__all__'
        
class RecoveryMethodForm(forms.ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'