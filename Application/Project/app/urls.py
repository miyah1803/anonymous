from django.urls import path
from . import views
from .views import HomePageView, SalesPageView, InventoryPageView, ExpensesPageView, RecordPageView, SigninPageView, SignupPageView, DashPageView, SalePageView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('sales/', SalesPageView.as_view(), name = 'sales'),
    path('api/sales/', views.get_sales_data),
    path('api/bad-orders/', views.get_bad_orders_data),
    path('api/sales/add/', views.add_sale),
    path('api/bad-orders/add/', views.add_bad_order),
    path('api/sales/update/<int:pk>/', views.update_sale),
    path('api/bad-orders/update/<int:pk>/', views.update_bad_order),
    path('api/sales/delete/<int:pk>/', views.delete_sale),
    path('api/bad-orders/delete/<int:pk>/', views.delete_bad_order),
    path('inventory/', InventoryPageView.as_view(), name = 'inventory'),
    path('inventory/get/', views.get_inventory, name='get_inventory'),
    path('inventory/add/', views.add_inventory, name='add_inventory'),
    path('inventory/update/<int:pk>/', views.update_inventory, name='update_inventory'),
    path('inventory/delete/<int:pk>/', views.delete_inventory, name='delete_inventory'),
    path('expenses/', ExpensesPageView.as_view(), name = 'expenses'),
    path('expenses/delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('expenses/update/<int:pk>/', views.update_expense, name='update_expense'),
    path('record/', RecordPageView.as_view(), name = 'record'),
    path('signin/', SigninPageView.as_view(), name = 'signin'),
    path('signup/', SignupPageView.as_view(), name = 'signup'),
    path('dash/', DashPageView.as_view(), name='dash'),
    path('sale/', SalePageView.as_view(), name='sale'),

]