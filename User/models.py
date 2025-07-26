from django.db import models
from HR.models import *
from Guest.models import *
# Create your models here.

class tbl_request(models.Model):
    recruitment = models.ForeignKey(tbl_recruitment, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    request_status = models.IntegerField(default=0)
    request_date = models.DateField(auto_now_add=True)

