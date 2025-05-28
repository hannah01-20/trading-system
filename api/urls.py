from django.urls import path
from .views.indexView import IndexView
from .views.stockView import StockView
from .views.orderView import OrderView

urlpatterns = [
    path("", IndexView.as_view(), name = "index"),
    path("stocks/", StockView.as_view(), name = "stocks"),
    path("orders/", OrderView.as_view(), name = "orders"),
]
