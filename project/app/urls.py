from django.urls import path
from .views import *


urlpatterns=[
    path('',index.as_view(),name='index'),
    path('reg/',manage_reg.as_view(),name='reg'),
    path('log/',manger_log.as_view(),name='log'),
    path('view/',manager_view.as_view(),name='view'),
    path('up/<pk>/',Manager_prof_update.as_view(),name='up'),
    path('delete/<pk>/',managerdelete.as_view(),name='delete'),
    path('userreg/',user_reg.as_view(),name='userreg'),
    path('userlog/',user_log.as_view(),name='userlog'),
    path('user_view/',user_view.as_view(),name='userview'),
    path('pack/',re_pack,name='pack'),
    path('resortupv/',manager_resort_update,name='resortupv'),
    # path('resort/',create_resort.as_view(),name='resort'),
    path('resortv/',resort_view,name='resortv'),
    path('reup/<pk>',reupdate.as_view(),name='reup'),
    path('detv/<int:id>',detailview,name='detv'),
    path('book/<int:id>',book,name='book'),
    # path('payment/',paymaent_summary,name='payment'),
    path('adv/',adv.as_view(),name='admin'),
    path('order/',create_order,name='order'),
    path('gets/',order_get,name='gets'),
    path('data/',Orders,name='datas'),
    path('logout/',user_logout,name='logout'),
    path('adminv/',adminview,name='adminview'),
    path('del/<int:id>',dele,name='delete'),
]