from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.participantes_list, name='participantes_list'),
    url(r'^participante/(?P<pk>[0-9]+)/$', views.participante_detail, name='participante_detail'),
    url(r'^participante/new/$', views.participante_new, name='participante_new'),
    url(r'^participante/(?P<pk>[0-9]+)/edit/', views.participante_edit, name='participante_edit'),
    ]
