from django.db import models

class TblSearchCount(models.Model):
    date = models.DateField(null= False)
    word = models.TextField(null= False)
    count = models.IntegerField(null= False, blank= False, default= 0)