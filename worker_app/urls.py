from rest_framework.routers import DefaultRouter

from client_app.views import TableListViewSet

from worker_app.views import UserViewSet

router1 = DefaultRouter()

router1.register('table_lists', TableListViewSet)
router1.register('user/create', UserViewSet)

