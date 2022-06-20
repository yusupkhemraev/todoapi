from rest_framework import routers
from .api import TodoVievSet


router = routers.DefaultRouter()
router.register('api/todo', TodoVievSet, 'todo')


urlpatterns = router.urls