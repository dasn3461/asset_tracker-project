from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from asset import views
from asset.views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceAssignmentViewSet

#Defauult Router

router = routers.DefaultRouter()
#Register View Router
router.register('companies', CompanyViewSet)
router.register('employees', EmployeeViewSet)
router.register('devices', DeviceViewSet)
router.register('device-assignments', DeviceAssignmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
