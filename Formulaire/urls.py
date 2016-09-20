from django.conf.urls import url
from . import views

urlpatterns = [
    # /form/
    url(r'^$', views.accueil, name = 'accueil'),
    url(r'^index', views.index, name = 'index'),
    # /form/id
    
    url(r'^(?P<form_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<form_id>[0-9]+)/pass$', views.check_pass, name = 'pass'),
    url(r'^(?P<form_id>[0-9]+)/edit$',views.edit,name='edit'),
    url(r'^(?P<form_id>[0-9]+)/res',views.res,name='res'),
    url(r'^create', views.create, name = 'create'),
]
