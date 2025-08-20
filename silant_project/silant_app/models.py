from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class TechnicModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Модель техники")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('model-detail', args=[str(self.pk)])
    
class EngineModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Модель двигателя")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('engine-detail', args=[str(self.pk)])
    
class TransmissionModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Модель трансмиссии")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('transmission-detail', args=[str(self.pk)])

class DrivingAxleModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Модель ведущего моста")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('drivingaxle-detail', args=[str(self.pk)])
    
class SteerAxleModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Модель управляемого моста")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('steeraxle-detail', args=[str(self.pk)])

class MaintenanceType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Вид ТО")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('maintenancetype-detail', args=[str(self.pk)])
    
class FailureNode(models.Model):
    name = models.CharField(max_length=255, verbose_name="Узел отказа")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('failurenode-detail', args=[str(self.pk)])
    
class RecoveryMethod(models.Model):
    name = models.CharField(max_length=255, verbose_name="Способ восстановления")
    description = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recoverymethod-detail', args=[str(self.pk)])
    
class ServiceCompany(models.Model):
    name = models.CharField(max_length=255, verbose_name="Сервисная компания")
    description = models.TextField(default="Сервисная компания", verbose_name="Описание")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('servicecompany-detail', args=[str(self.pk)])
    
class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя клиента")
    description = models.TextField(default="Клиент", verbose_name="Описание")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.pk)])
    
class MaintenanceOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(default="Организация, проводившая ТО", verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('maintenanceorganization-detail', args=[str(self.pk)])
    
class Machine(models.Model):
    serial_number = models.CharField(unique=True, max_length=255, verbose_name="Заводской № машины")
    technic_model = models.ForeignKey(TechnicModel, on_delete=models.CASCADE, verbose_name="Модель техники")
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE, verbose_name="Модель двигателя")
    engine_number = models.CharField(max_length=255, verbose_name="Заводской № двигателя")
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, verbose_name="Модель трансмиссии")
    transmission_number = models.CharField(max_length=255, verbose_name="Заводской № трансмиссии")
    driving_axle_model = models.ForeignKey(DrivingAxleModel, on_delete=models.CASCADE, verbose_name="Модель ведущего моста")
    driving_axle_number = models.CharField(max_length=255, verbose_name="Заводской № ведущего моста")
    steer_axle_model = models.ForeignKey(SteerAxleModel, on_delete=models.CASCADE, verbose_name="Модель управляемого моста")
    steer_axle_number = models.CharField(max_length=255, verbose_name="Заводской № управляемого моста")
    delivery_contract = models.CharField(max_length=255, verbose_name="Договор поставки (№, дата)")
    shipment_date = models.DateField(verbose_name="Дата отгрузки с завода")
    recipient = models.CharField(max_length=255, verbose_name="Грузополучатель (конечный потребитель)")
    delivery_address = models.CharField(max_length=255, verbose_name="Адрес поставки (эксплуатации)")
    configuration = models.TextField(max_length=80, default="Стандарт", verbose_name="Комплектация (доп. опции)")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name="Сервисная компания")

    def __str__(self):
        return self.serial_number
    
    def get_absolute_url(self):
        return reverse('machine-detail', args=[str(self.id)])
    
class Maintenance(models.Model):
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE, verbose_name="Вид ТО")
    maintenance_date = models.DateField(verbose_name="Дата проведения ТО")
    operating_time = models.IntegerField(default=0, verbose_name="Наработка, м/час")
    order_number = models.CharField(max_length=255, verbose_name="Номер заказ-наряда")
    order_date = models.DateField(verbose_name="Дата заказ-наряда")
    maintenance_organization = models.ForeignKey(MaintenanceOrganization, on_delete=models.CASCADE, verbose_name="Организация, проводившая ТО")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Машина")
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name="Сервисная компания")

    def __str__(self):
        return f"{self.machine.serial_number}/{self.maintenance_type.name}/{self.maintenance_date}"
    
    def get_absolute_url(self):
        return reverse('maintenance-detail', args=[str(self.id)])
    
class Reclamation(models.Model):
    failure_date = models.DateField(verbose_name="Дата отказа")
    operating_time = models.IntegerField(default=0, verbose_name="Наработка, м/час")
    failure_node = models.ForeignKey(FailureNode, on_delete=models.CASCADE, verbose_name="Узел отказа")
    failure_description = models.TextField(verbose_name="Описание отказа")
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE, verbose_name="Способ восстановления")
    spare_parts = models.TextField(blank=True, verbose_name="Используемые запасные части")
    recovery_date = models.DateField(verbose_name="Дата восстановления")
    downtime = models.IntegerField(default=0, verbose_name="Время простоя техники")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="Машина", related_name='reclamations')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name="Сервисная компания")

    def save(self, *args, **kwargs):
        self.downtime = (self.recovery_date - self.failure_date).days
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.machine.serial_number}/{self.failure_date}/{self.failure_node.name}"
    
    def get_absolute_url(self):
        return reverse('reclamation-detail', args=[str(self.pk)])
