"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1',views.fun1),
    path('2',views.fun2),
    path('3',views.fun3),
    path('4',views.fun4),
    path('5',views.fun5),
    path('6',views.fun6),
    path('7',views.fun7),
    path('8',views.fun8),
    path('9',views.fun9),
    path('10',views.fun10),
    path('',views.fun11),
    path('12',views.fun12),
    path('13',views.fun13),
    path('14',views.fun14),
    path('15',views.signup2),
    path('16',views.home),
    path('17',views.logout),
    path('18',views.admin2),
    path('19',views.admin_log2),
    path('20',views.fun15),
    path('21',views.doctor_form),
    path('22',views.reg_docs),
    path('del_doc/<id>',views.del_doc),
    path('23',views.appoint_booking1),
    path('24',views.fun16),
    path('del_app/<id>',views.del_app),
    path('accept_app/<id>',views.accept_app),
    path('25',views.booking_details)
]
