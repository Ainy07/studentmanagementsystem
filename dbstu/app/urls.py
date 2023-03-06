from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.index),
    path('courses/',views.courses),
    path('dashboard/',views.dashboard),
    path('employees/',views.employees),
    path('notifications/',views.notifications),
    path('pgdashboard/',views.pgdashboard),
    path('profile/',views.profile),
    path('signup/',views.signup),
    path('tables/',views.tables),
    path('tenants/',views.tenants),
    path('viewstudents/',views.viewstudents),
    path('registration/',views.registration),
    path('login/',views.login),
    path('addcourse/',views.addcourse),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete")
]
