from .cookie import *
from .unjson import UnJson
from rest_framework.views import APIView
from rest_framework import status, generics
from django.http import Http404

import json

from ..models import oldperson_info, volunteer_info, employee_info, event_info
from ..serializer import OldPersonSerializer, VolunteerSerializer, EmployeeSerializer, EventSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


def checkToken(data):
    try:
        if check_token(data.token):
            return True
        else:
            res = {'code': 402, 'message': '请登入'}
            raise Http404(res)
    except BaseException:
        res = {'code': 402, 'message': '请登入'}
        raise Http404(res)


# class eventList(generics.ListCreateAPIView):
#     """
#     get:获取所有事件
#     post:新加一个事件
#     """
#     queryset = event_info.objects.all()
#     serializer_class = EventSerializer

class eventList(APIView):
    def get(self,request):
        serialize = EventSerializer(event_info.objects.all(),many=True)
        return Response(serialize.data)

    def post(self,request):
        serializer = EventSerializer(data=request.data)
        data =UnJson(request.data)
        try:
            oldperson_id = data.oldperson_id
            try:
                oldperson = oldperson_info.objects.get(pk=oldperson_id)
            except oldperson_info.DoesNotExist:
                pass
        except BaseException:
            print('ku')
        if serializer.is_valid():
            serializer.validated_data['oldperson_id'] = oldperson
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
