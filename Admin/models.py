from django.db import models

# Create your models here.

class tbl_hr(models.Model):
    hr_name = models.CharField(max_length=30)
    hr_email = models.CharField(max_length=30)
    hr_contact = models.CharField(max_length=30)
    hr_password = models.CharField(max_length=30)
    hr_photo = models.FileField(upload_to='Assets/HR/Photo/')
    
class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)