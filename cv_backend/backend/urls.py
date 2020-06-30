from django.conf.urls import url
from django.views.static import serve
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    # BASE 基本
    url('login', ),
    url('signup', ),
    url('base/changePassword', ),
    url('base/getSelf', ),
    url('base/changeSelf', ),
    url('base/changeNotify', ),
    url('base/entryFace', ),
    url('base/webSocket'),
    url('base/upload/avatar', ),
    url('base/upload/event', ),
    url('base/getPhoto/(?P<id>.+)/$', ),

    # PERSONAL MANAGEMENT 人员管理

    #   Old Man  老人
    url('person/oldman/list', ),
    url('person/oldman/detail', ),
    url('person/oldman/delete', ),
    url('person/oldman/add', ),
    url('person/oldman/update', ),
    #   Employee  员工
    url('person/employee/list', ),
    url('person/employee/detail', ),
    url('person/employee/delete', ),
    url('person/employee/add', ),
    url('person/employee/update', ),
    #   Volunteer  义工
    url('person/volunteer/list', ),
    url('person/volunteer/detail', ),
    url('person/volunteer/delete', ),
    url('person/volunteer/add', ),
    url('person/volunteer/update', ),

    # EVENT 事件
    url('event/list'),

    # STATISTICS 统计报表
    url('statistics/all', ),  # 所有人员的统计
    url('statistics/age',),   # 按老人年龄区间
    url('statistics/emotion',),
    url('statistics/fall',),
    url('statistics/foreign')

]
