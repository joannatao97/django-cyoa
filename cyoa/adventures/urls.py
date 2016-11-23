from django.conf.urls import url

from . import views


app_name = 'adventures'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'adventure/(\d+)$', views.adventure, name='adventure'),
    url(r'question/(\d+)$', views.question, name='question'),
]