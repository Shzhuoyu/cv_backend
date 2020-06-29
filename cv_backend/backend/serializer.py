from rest_framework import serializers
from .models import *


class OldPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = oldperson_info
        fields = ('id', 'org_id', 'client_id', 'username')  # TODO


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_info
        fields = ('id', 'org_id', 'client_id', 'username')  # TODO
