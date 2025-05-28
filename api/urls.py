from django.urls import path
from .views.indexView import IndexView
from .views.stockView import StockView

urlpatterns = [
    path("", IndexView.as_view(), name = "index"),
    path("stocks/", StockView.as_view(), name = "stocks"),
]
