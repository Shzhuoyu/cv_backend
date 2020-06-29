from django.db import models


# Create your models here.

class oldperson_info(models.Model):
    ID = models.IntegerField(max_length=11, primary_key=True)
    ORG_ID = models.IntegerField(max_length=11, blank=True)
    CLIENT_ID = models.IntegerField(max_length=11, blank=True)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5) # f/m
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)  # 身份证
    birthday = models.DateTimeField()
    checkin_date = models.DateTimeField()
    checkout_data = models.DateTimeField()
    imgset_dir = models.CharField(max_length=200)
    profile_photo = models.CharField(max_length=200)
    room_number = models.CharField(max_length=50)
    firstguardian_name = models.CharField(max_length=50)
    firstguardian_relationship = models.CharField(max_length=50)
    firstguardian_phone = models.CharField(max_length=50)
    firstguardian_wechat = models.CharField(max_length=50)

    sceondguardian_name = models.CharField(max_length=50)
    secondguardian_relationship = models.CharField(max_length=50)
    secondguardian_phone = models.CharField(max_length=50)
    secondguardian_wechat = models.CharField(max_length=50)
    health_state = models.CharField(max_length=50)
    DESCRIPTION = models.CharField(max_length=50)
    ISACTIVE = models.CharField(max_length=10)
    CREATED = models.DateTimeField()
    CREATEBY = models.IntegerField(max_length=11)
    UPDATED = models.DateTimeField()
    UPDATEBY = models.IntegerField(max_length=11)
    REMOVE = models.CharField(max_length=1)


    def __str__(self):
        return self.username


class employee_info(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    ORG_ID = models.IntegerField(max_length=11)
    CLIENT_ID = models.IntegerField(max_length=11)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=5)  # f/m
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50)  # 身份证
    birthday = models.DateTimeField()
    hire_date = models.DateTimeField()
    resign_date = models.DateTimeField()
    imgset_dir = models.CharField(max_length=200)
    profile_photo = models.CharField(max_length=200)
    DESCRIPTION = models.CharField(max_length=200)
    ISACTIVE = models.CharField(max_length=10)
    CREATED = models.DateTimeField()
    CREATEBY = models.IntegerField(max_length=11)
    UPDATED = models.DateTimeField()
    UPDATEBY = models.IntegerField(max_length=11)
    REMOVE = models.CharField(max_length=1)

    def __str__(self):
        return self.username


class volunteer_info(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    ORG_ID = models.IntegerField(max_length=11)
    CLIENT_ID = models.IntegerField(max_length=11)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=5) # f/m
    phone = models.CharField(max_length=50)
    id_card = models.CharField(max_length=50) # 身份证
    birthday = models.DateTimeField()
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    imgset_dir = models.CharField(max_length=200)
    profile_photo = models.CharField(max_length=200)
    DESCRIPTION = models.CharField(max_length=200)
    ISACTIVE = models.CharField(max_length=10)
    CREATED = models.DateTimeField()
    CREATEBY = models.IntegerField(max_length=11)
    UPDATED = models.DateTimeField()
    UPDATEBY = models.IntegerField(max_length=11)
    REMOVE = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class event_info(models.Model):
    id = models.IntegerField(max_length=11,primary_key=True)
    event_type = models.IntegerField(max_length=11)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=200)
    event_desc = models.CharField(max_length=200)
    oldperson_id = models.IntegerField(max_length=11)
    img_path = models.CharField(max_length=200)

    def __str__(self):
        return self.event_desc


class sys_user(models.Model):
    id = models.IntegerField(max_length=11,primary_key=True)
    ORG_ID = models.IntegerField(max_length=11)
    CLIENT_ID = models.IntegerField(max_length=11)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    REAL_NAME = models.CharField(max_length=50)
    SEX = models.CharField(max_length=20)
    EMAIL = models.CharField(max_length=50)
    PHONE = models.CharField(max_length=50)
    MOBILE = models.CharField(max_length=50)
    DESCRIPTION = models.CharField(max_length=200)
    ISACTIVE = models.CharField(max_length=10)
    CREATED = models.DateTimeField()
    CREATEBY = models.IntegerField(max_length=11)
    UPDATED = models.DateTimeField()
    UPDATEBY = models.IntegerField(max_length=11)
    REMOVE = models.CharField(max_length=1)
    DATAFILTER = models.CharField(max_length=200)
    theme = models.CharField(max_length=45)
    defaultpage = models.CharField(max_length=45)
    logoimage = models.CharField(max_length=45)
    qqopenid = models.CharField(max_length=100)
    appversion = models.CharField(max_length=10)
    jsonauth = models.CharField(max_length=1000)

    def __str__(self):
        return self.UserName

