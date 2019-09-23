from rest_framework.routers import DefaultRouter

from . import views
from worker_app.views import ClientViewSet
router = DefaultRouter()

# Add category, Restoran, Product
router.register('category',views.CategoryViewSet)
router.register('restorans',views.RestoransViewSet, base_name='restoran_lists')
router.register('products', views.ProductViewSet)

# Lists categoryes, products, product detail
router.register('restoran/(?P<restoran_id>\d+)/table_number/(?P<table_number>\d+)',views.RestoranTablesViewSet, base_name='restoran_category')
router.register('restoran/(?P<restoran_id>\d+)/table_number/(?P<table_number>\d+)/category/(?P<c_id>\d+)', views.ProductListViewSet, base_name='product_list')
router.register('restoran/(?P<restoran_id>\d+)/table_number/(?P<table_number>\d+)/category/(?P<c_id>\d+)/product/(?P<p_id>\d+)', views.ProductDetailViewSet, base_name='product_detail')

# Add and lists check
router.register('restoran/(?P<restoran_id>\d+)/table_number/(?P<table_number>\d+)/add_product',views.TableProductsAddViewSet, base_name='table_products')
router.register('restoran/(?P<r_id>\d+)/table_number/(?P<t_id>\d+)/check',views.TableProductsListsViewSet, base_name='table_products_lists')

# router.register('restoran/create',views.RestoranPostViewSet.as_view(), base_name='restoran_create')
router.register('create', ClientViewSet)