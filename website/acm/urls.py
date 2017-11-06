from django.conf.urls import url, include
from . import views

apps_name = 'acm'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^upcoming/$', views.upcoming_events, name='upcoming'),

]