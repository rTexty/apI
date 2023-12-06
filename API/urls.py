from django.urls import include
from django.contrib import admin
from django.urls import path
from Cars.views import CreateCarList, UpdateCarList
from Users.views import CreateUserList, GetUserList 
from MyTasks.routers import router
from MyTasks.views import CompletedTasks, ListTasks, create_task


urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/cars/', CreateCarList.as_view()),
    path('api/cars/<int:pk>/', UpdateCarList.as_view()),


    path('api/users/', GetUserList.as_view()),
    path('api/users/create/', CreateUserList.as_view()),

    
    path('api/mytasks/', ListTasks.as_view()),
    path('api/createtask/', create_task, name='createtask'),
    path('api/tasks/completed/', CompletedTasks.as_view({'get': 'comptasks'})),
    path('api/', include(router.urls), name='tasks'),


]
