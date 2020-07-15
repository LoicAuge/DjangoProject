from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<idC>[0-9]+)$', views.detail, name='detail'),
    url(r'^student/create/', views.StudentCreateView.as_view(), name='create_eleve'),
    url(r'^student/update/(?P<pk>[0-9]+)$', views.StudentUpdateView.as_view(), name='update_eleve'),
    url(r'^cursus/create/', views.CursusCreateView.as_view(), name='create_cursus'),
    url(r'^cursus/update/(?P<pk>[0-9]+)$', views.CursusUpdateView.as_view(), name='update_cursus'),
    url(r'^student/(?P<idS>[0-9]+)$', views.detail_Student, name='detail_student')
]