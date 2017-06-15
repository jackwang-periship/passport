'''
Created on May 29, 2017

@author: jwang02
'''
from django.conf.urls import url
from students import views as students_views

urlpatterns = [
    url(r'^$', students_views.students, name='students'),
    url(r'^add_student/$', students_views.add_student, name='add_student'),

]

