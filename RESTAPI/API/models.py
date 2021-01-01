from django.db import models
import random

# Create your models here.
def fault_number_generator():

    prof_number = str(random.randint(100001, 999999))
    return prof_number

Loadshedding_choices = [('Harare',(('Mbare','Waterfalls','cbd','Belvedere','Kuwadzana','GlenView','Borrowdale','Warren-Park','Budiriro','Epworth'))),
                        ('Mutare',(('Borderview','Murambi','Darlington','Sakubva','Chikanga','Dangamvura','yeovil')))]
Location_choices = [('Harare',(('Mbare','Waterfalls','cbd','Belvedere','Kuwadzana','GlenView','Borrowdale','Warren-Park','Budiriro','Epworth'))),
                        ('Mutare',(('Borderview','Murambi','Darlington','Sakubva','Chikanga','Dangamvura','yeovil')))]  
Status_choices = [('new', 'New'),('current','Current'),('resolved','Resolved'),('stalled','Stalled')]
engagement = [('engaged','Engaged'),('free','Free')]
class Fault_List(models.Model):
    Fault_number = models.IntegerField(primary_key=True,editable=False,default=fault_number_generator)
    Name  = models.CharField(max_length=100)
    Location = models.CharField(max_length=200,choices=Location_choices)
    Duration = models.CharField(max_length=30)
    Description = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=20,choices=Status_choices)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return str(self.Fault_number) + ' - ' + str(self.Name)
class Employees(models.Model):
    Name = models.CharField(max_length=200)
    status = models.CharField(max_length=20,choices=engagement,default='free')
    Fault_Detail = models.ForeignKey(Fault_List, on_delete=models.DO_NOTHING )
    def __str__(self):
        return str(self.id) + ' - ' + str(self.Name)

class LoadShedding(models.Model):
    Area_name = models.CharField(max_length=100,choices=Loadshedding_choices)
    Duration = models.IntegerField()
    Date = models.DateTimeField()
    reason = models.TextField(max_length=None,blank=True,)
    class Meta:
        ordering = ['-id']
    def __str__(self):
        return str(self.id) + ' - ' + str(self.Area_name)
class Incidents(models.Model):
    Location = models.CharField(max_length=200,null=False,blank=False)
    Province = models.CharField(max_length=200,null = True)
    Description = models.TextField(max_length=10000)



