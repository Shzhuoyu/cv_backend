from django.conf.urls import url
from django.views.static import serve
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('pptupload',views.PPTupload),
    ]