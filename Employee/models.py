from django.db import models
from HR.models import *
# Create your models here.

class tbl_leave(models.Model):
    employee = models.ForeignKey(tbl_employee, on_delete=models.CASCADE)
    leave_content = models.CharField(max_length=100)
    leave_status = models.IntegerField(default=0)
    leave_date = models.DateField(auto_now_add=True)

class tbl_complaint(models.Model):
    complaint_title = models.CharField(max_length=30)
    complaint_content = models.CharField(max_length=200)
    complaint_reply = models.CharField(max_length=200)
    complaint_status = models.IntegerField(default=0)
    employee = models.ForeignKey(tbl_employee, on_delete=models.CASCADE,null=True)
    hr = models.ForeignKey(tbl_hr, on_delete=models.CASCADE,null=True)
    