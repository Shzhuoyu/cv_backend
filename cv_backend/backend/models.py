from django.db import models


# Create your models here.

class oldperson_info(models.Model):
    ID = models.IntegerField(max_length=11, primary_key=True),
    ORG_ID = models.IntegerField(max_length=11, blank=True),
    CLIENT_ID = models.IntegerField(max_length=11, blank=True),
    username = models.CharField(max_length=50),
    gender = models.CharField(max_length=5),  # f/m
    phone = models.CharField(max_length=50),
    id_card = models.CharField(max_length=50),  # 身份证
    birthday = models.DateTimeField(),
    checkin_date = models.DateTimeField(),
    checkout_data = models.DateTimeField(),
    imgset_dir = models.CharField(max_length=200),
    profile_photo = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class employee_info(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
