from django.conf.urls import url
from rest_framework.documentation import include_docs_urls
from .views import base, person, statistics, views

urlpatterns = [

    url('docs/', include_docs_urls(title='API接口文档')),

    # BASE 基本
    url('login', base.LoginIn),
    url('account', base.AccountDetail.as_view()),
    url('base/sysInfo', base.SysUserDetail.as_view()),

    # url('base/changeNotify', ),
    # url('base/entryFace', ),
    # url('base/webSocket'),
    url('base/upload/avatar', views.uploadAvatar),
    # url('base/upload/event', ),
    url('base/getPhoto/(?P<id>.+)/$',views.getImg ),

    # PERSONAL MANAGEMENT 人员管理

    #   Old Man  老人
    url('person/oldManList', person.oldManList.as_view()),
    url('person/oldManDetail', person.oldManDetail.as_view()),
    #   Employee  员工
    url('person/employeeList', person.employeeList.as_view()),
    url('person/employeeDetail', person.employeeDetail.as_view()),
    #   Volunteer  义工
    url('person/volunteerList', person.volunteerList.as_view()),
    url('person/volunteerDetail', person.volunteerDetail.as_view()),

    # EVENT 事件
    url('event/list', statistics.eventList.as_view()),

    # STATISTICS 统计报表
    url('statistics/all', statistics.oldManTotal),  # 所有人员的统计
    # url('statistics/age',),   # 按老人年龄区间
    # url('statistics/emotion',),
    # url('statistics/fall',),
    # url('statistics/foreign')

]
