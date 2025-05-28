from django.urls import path
from .views.indexView import IndexView
from .views.stockView import StockView, StockDetailsView
from .views.orderView import OrderView, OrderDetailsView
from .views.userView import UserView, UserDetailsView

urlpatterns = [
    path("", IndexView.as_view(), name = "index"),
    path("stocks/", StockView.as_view(), name = "stocks"),
    path("stocks/<int:pk>/", StockDetailsView.as_view(), name="stock"),
    path("orders/", OrderView.as_view(), name = "orders"),
    path("orders/<int:pk>/", OrderDetailsView.as_view(), name = "order"),
    path("users/", UserView.as_view(), name = "users"),
    path("users/<int:pk>/", UserDetailsView.as_view(), name = "users"),
]
