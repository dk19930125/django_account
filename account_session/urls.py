from django.conf.urls import url

import views

urlpatterns = [
    # url(r'^test/$',test,name='register')
    url(r'^regist/$',views.Regist,name='regist'),
    url(r'^login/$',views.Login,name='login'),
    url(r'^index/$',views.Index),
    url(r'^logout/$',views.Logout),
]