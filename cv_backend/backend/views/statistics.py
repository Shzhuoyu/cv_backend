from .cookie import *
import datetime
from .unjson import UnJson
from rest_framework.views import APIView
from rest_framework import status, generics
from django.http import Http404
from django.db.models import Q, Count
import json

from ..models import oldperson_info, volunteer_info, employee_info, event_info, sys_user
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
    """
    get:
    事件列表
    post:
    添加事件
    """

    def get(self, request):
        serialize = EventSerializer(event_info.objects.all(), many=True)
        return Response(serialize.data)

    def post(self, request):
        upload_file = request.FILES['file']
        request.data.pop('file')

        url = './img/event/' + 'ev-' + upload_file.name
        file = open(url, 'wb+')
        for chunk in upload_file.chunks():
            file.write(chunk)

        serializer = EventSerializer(data=request.data)
        data = UnJson(request.data)
        try:
            oldperson_id = data.oldperson_id
            try:
                oldperson = oldperson_info.objects.get(pk=oldperson_id)
            except oldperson_info.DoesNotExist:
                oldperson = None
        except BaseException:
            oldperson = None
        if serializer.is_valid():
            serializer.validated_data['oldperson_id'] = oldperson
            serializer.validated_data['img_path'] = url
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def allTotal(request):
    """
    人员统计
    """
    old = oldperson_info.objects.count()
    employee = employee_info.objects.count()
    volunteer = volunteer_info.objects.count()
    obj = {
        'old': old,
        'employee': employee,
        'volunteer': volunteer
    }
    return HttpResponse(json.dumps(obj, ensure_ascii=False))


@api_view(['GET'])
def oldManAge(request):
    """老人年龄区间"""
    yearList = list(map(datetime.timedelta, [60, 70, 80, 90] * 365))
    today = datetime.date.today()
    age = [
        oldperson_info.objects.filter(birthday__gt=today - yearList[0]).count(),
        oldperson_info.objects.filter(birthday__in=[today - yearList[0], today - yearList[1]]).count(),
        oldperson_info.objects.filter(birthday__in=[today - yearList[1], today - yearList[2]]).count(),
        oldperson_info.objects.filter(birthday__in=[today - yearList[2], today - yearList[3]]).count(),
        oldperson_info.objects.filter(birthday__lt=today - yearList[3]).count()]
    labels = ['<60岁', '60~70岁', '60~70岁', '60~70岁', '>90岁']
    obj = {
        'age': age,
        'labels': labels
    }
    return HttpResponse(json.dumps(obj, ensure_ascii=False))


@api_view(['GET'])
def todayEvent(request):
    """今日事件"""
    today = datetime.date.today()
    smile = event_info.objects.filter(event_date=today, event_type=0).count()
    communication = event_info.objects.filter(event_date=today, event_type=1).count()
    stranger = event_info.objects.filter(event_date=today, event_type=2).count()
    fall = event_info.objects.filter(event_date=today, event_type=3).count()
    forbid = event_info.objects.filter(event_date=today, event_type=4).count()

    obj = [
        ['老人微笑', smile]
        ['老人互动', communication]
        ['陌生人来访', stranger]
        ['老人摔倒', fall]
        ['禁区入侵', forbid]
    ]
    return HttpResponse(json.dumps(obj, ensure_ascii=False))


@api_view(['GET'])
def dailyEvent(request):
    """七日事件"""
    bigList = []
    today = datetime.date.today()
    dayList = list(map(datetime.timedelta, list(range(0, 7))))
    for item in dayList:
        smitem = []
        date = today - item
        smitem.append(str(date))
        smitem.append(event_info.objects.filter(event_date=date, event_type=0).count())
        smitem.append(event_info.objects.filter(event_date=date, event_type=1).count())
        smitem.append(event_info.objects.filter(event_date=date, event_type=2).count())
        smitem.append(event_info.objects.filter(event_date=date, event_type=3).count())
        smitem.append(event_info.objects.filter(event_date=date, event_type=4).count())
        bigList.append(smitem)
    return HttpResponse(json.dumps(bigList, ensure_ascii=False))


@api_view(['GET'])
def smileStar(request):
    """
    微笑之星
    :param request:
    :return:
    """
    date = datetime.date.today() - datetime.timedelta(days=7)
    oldList = oldperson_info.objects.annotate(num_event=Count('person',
                                                              filter=Q(person__event_type=0,
                                                                       person__event_date__gt=date))).order_by(
        '-num_event')[:5]
    result = []
    for item in oldList:
        small = []
        small.append(item.username)
        small.append(item.num_event)
        result.append(small)

    # 这里得到的是微笑前五
    # pubs = oldperson_info.objects.annotate(nums= Count('person'))

    return HttpResponse(json.dumps(result, ensure_ascii=False))


@api_view(['GET'])
def communicateStar(request):
    """
    交际花
    :param request:
    :return:
    """
    date = datetime.date.today() - datetime.timedelta(days=7)
    oldList = oldperson_info.objects.annotate(num_event=Count('person',
                                                              filter=Q(person__event_type=1,
                                                                       person__event_date__gt=date))).order_by(
        '-num_event')[:5]
    result = []
    for item in oldList:
        small = []
        small.append(item.username)
        small.append(item.num_event)
        result.append(small)

    # 这里得到的是微笑前五
    # pubs = oldperson_info.objects.annotate(nums= Count('person'))

    return HttpResponse(json.dumps(result, ensure_ascii=False))


@api_view(['POST'])
def oldAnalysis(request):
    """
    一个老人过去七天的全方面分析
    :param request: id:老人id
    :return:
    """
    result={}
    data = UnJson(request.data)
    Old = oldperson_info.objects.get(pk=data.id)
    result['name']=Old.username

    date7 = datetime.date.today() - datetime.timedelta(days=7)
    eventList = event_info.objects.filter(event_date__gt=date7,oldperson_id = Old)
    result['total'] = {'smile':eventList.filter(event_type=0).count(),'communicate':eventList.filter(event_type=1).count()}
    bigList = []
    today = datetime.date.today()
    dayList = list(map(datetime.timedelta, list(range(0, 7))))
    for item in dayList:
        smitem = []
        date = today - item
        smitem.append(str(date))
        smitem.append(eventList.filter(event_date=date, event_type=0).count())
        smitem.append(eventList.filter(event_date=date, event_type=1).count())
        bigList.append(smitem)
    result['detail'] = bigList
    return HttpResponse(json.dumps(result, ensure_ascii=False))
