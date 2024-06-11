from django.urls import path
from . import views

# Khai báo url cho view ở bên file view
# Tham số đầu tiên trong hàm path
# chính là URL tính tại vị trí của app product
# Tương đương với http://127.0.0.1:8000/customers/
urlpatterns = [
    path("", views.customers_dashboard, name="customers-dashboard"),
    path("profile", views.customers_profile, name="customers-profile"),
    path("orders", views.customers_orders, name="customers-orders"),
]
