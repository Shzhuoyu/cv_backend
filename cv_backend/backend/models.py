from django.db import models


# Create your models here.

class oldperson_info(models.Model):
    ID = models.IntegerField(max_length=11, primary_key=True),
    ORG_ID = models.IntegerField(max_length=11, blank=True),
    CLIENT_ID = models.IntegerField(max_length=11,blank=True),
