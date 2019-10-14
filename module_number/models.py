from django.db import models

# Create your models here.


class customerDataBase(models.Model):
    SI_NO = models.AutoField(primary_key=True)
    Number = models.IntegerField()
    Date = models.DateTimeField(auto_now_add=True)
    Monthy_visit = models.IntegerField()
    Visits = models.IntegerField()
