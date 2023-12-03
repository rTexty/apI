from django.urls import include
from django.contrib import admin
from django.urls import path
from Cars.views import CreateCarList, UpdateCarList
from Users.views import CreateUserList, GetUserList 
from MyTasks.routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cars/', CreateCarList.as_view()),
    path('api/cars/<int:pk>/', UpdateCarList.as_view()),
    path('api/users/', GetUserList.as_view()),
    path('api/users/create/', CreateUserList.as_view()),
    path('api/', include(router.urls)),

]
