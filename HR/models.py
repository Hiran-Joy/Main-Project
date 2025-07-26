from django.db import models
from Admin.models import *
# Create your models here.

class tbl_role(models.Model):
    role_name = models.CharField(max_length=30)

class tbl_employee(models.Model):
    employee_name = models.CharField(max_length=30)
    employee_email = models.CharField(max_length=30)
    employee_contact = models.CharField(max_length=30)
    employee_address = models.CharField(max_length=50)
    employee_idnumber = models.CharField(max_length=30)
    employee_photo = models.FileField(upload_to="Assets/Employee/Photo/")
    employee_proof = models.FileField(upload_to="Assets/Employee/Proof/")
    role = models.ForeignKey(tbl_role, on_delete=models.CASCADE)
    employee_password = models.CharField(max_length=30)

class tbl_attendence(models.Model):
    employee = models.ForeignKey(tbl_employee, on_delete=models.CASCADE)
    attendence_date = models.DateField(auto_now_add=True)
    attendence_intime = models.TimeField()
    attendence_outtime = models.TimeField()

class tbl_salary(models.Model):
    employee = models.ForeignKey(tbl_employee, on_delete=models.CASCADE)
    salary_amount = models.IntegerField()
    salary_date = models.DateField(auto_now_add=True)

class tbl_schedule(models.Model):
    schedule_date = models.DateField(auto_now_add=True)
    schedule_todate = models.DateField()
    schedule_time = models.TimeField()
    schedule_details = models.CharField(max_length=100)

class tbl_recruitment(models.Model):
    recruitment_content=models.CharField(max_length=500)
    recruitment_lastdate=models.DateField(null=True)
    hr=models.ForeignKey(tbl_hr, on_delete=models.CASCADE)
    recruitment_status=models.IntegerField(default=0)
    recruitment_date = models.DateField(auto_now_add=True) 




