from django.contrib import admin
from django.urls import path
from db.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/<int:id>/<str:name>/<int:age>/<str:gender>/<str:isActive>/', Details, name='details'),
    path('get', Get_all, name='read'),
    path('get/<int:id>/', Get_by_id, name='read'),
    path('update/<int:id>/<str:name>/<int:age>/<str:gender>/<str:isActive>/',Update_by_id,name="update"),
    path('get/<int:id>/del',Delete_by_id,name='Delete')
]
