from django.conf.urls import url

from . import views

# for app named adventures
app_name = 'adventures'

# create urls through this pattern
# used djangos's tutorials heavily
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'adventure/(\d+)$', views.adventure, name='adventure'),
    url(r'question/(\d+)$', views.question, name='question'),
]