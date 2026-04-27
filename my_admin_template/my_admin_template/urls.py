"""
URL configuration for my_template_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from admin_pages.views import home,addEmployee,viewEmployee,profile,saveEmployee,viewAllEmployeeList,updateEmployee,updateEmployeeDetails,deleteEmployeeRecord

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    path('addEmployee/', addEmployee, name="addEmployee"),
    path('viewEmployee/', viewEmployee, name="viewEmployee"),
    path('profile/', profile, name="profile"),
    path('saveEmployee/',saveEmployee,name="saveEmployee"),
    path('viewAllEmployeeList/0',viewAllEmployeeList,name="viewAllEmployeeList"),
    path('updateEmployee/<int:empid>/', updateEmployee, name="updateEmployee"),
    path('updateEmployeeDetails/', updateEmployeeDetails, name="updateEmployeeDetails"),
    path('deleteEmployee/<id:empid>/',deleteEmployeeRecord,name="deleteEmployee")

]
