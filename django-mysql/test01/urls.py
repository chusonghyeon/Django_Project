from django.urls import path
from . import views

urlpatterns = [
    path('test01datas/', views.getTestDatas, name='test01datas'),
    path('test01data/<str:name>', views.getTestData, name='test01data'),
    path('postmember/', views.postMember, name='postmember'),
    path('putmember/<str:pk>', views.putMember, name='putmember'),
    path('putmember/<str:pk>', views.putMember, name='putmember'),
    path('getmembers/', views.getMembers, name='getmembers')
]
