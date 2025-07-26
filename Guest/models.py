from django.db import models

# Create your models here.

class tbl_user(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30)
    user_contact = models.CharField(max_length=30)
    usre_address = models.CharField(max_length=50)
    user_photo = models.ImageField(upload_to='Assets/user/photo/', blank=True, null=True)
    user_password = models.CharField(max_length=30)