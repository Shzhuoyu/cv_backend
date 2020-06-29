from rest_framework import serializers
from .models import *


class OldPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = oldperson_info
        fields = ('id', 'org_id', 'client_id', 'username', 'gender', 'phone', 'id_card', 'birthday', 'checkin_date', 'checkout_date', 'imgset_dir', 'profile_photo', 'room_number',
                  'firstguardian_name', 'firstguardian_relationship', 'firstguardian_phone', 'firstguardian_wechat',
                  'secondguardian_name', 'secondguardian_relationship', 'secondguardian_phone', 'secondguardian_wechat',
                  'health_state', 'description', 'isactive', 'created', 'createby', 'updated', 'updateby', 'remove')  # TODO


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_info
        fields = ('id', 'org_id', 'client_id', 'username', 'gender', 'phone', 'id_card', 'birthday',
                  'hire_date', 'resign_date', 'imgset_dir', 'profile_photo', 'description', 'isactive', 'created', 'createby', 'updated', 'updateby', 'remove')  # TODO


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = volunteer_info
        fields = ('id', 'org_id', 'client_id', 'name', 'gender', 'phone', 'id_card', 'birthday',
                  'checkin_date', 'checkout_date', 'imgset_dir', 'profile_photo', 'description', 'isactive',
                  'created', 'createby', 'updated', 'updateby', 'remove')  # TODO


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event_info
        fields = ('id', 'event_type', 'event_date', 'event_location', 'event_desc', 'oldperson_id', 'img_path')


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = sys_user
        fields = ('id', 'org_id', 'client_id', 'username', 'password', 'real_name', 'sex', 'email', 'phone', 'mobile',
                  'description', 'isactive', 'created', 'createby', 'updated', 'updateby', 'remove', 'datafilter',
                  'theme', 'defaultpage', 'logoimage', 'qqopenid', 'appversion', 'jsonauth')