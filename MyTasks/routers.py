from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TasksFunc,)

urlpatterns = router.urls