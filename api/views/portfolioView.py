from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Order
from ..serializers import OrderDetailsSerializer

class PortfolioView(APIView):
    def get(self, request):
        user = request.user

        orders = Order.objects.filter(user = user.id)
        serializer = OrderDetailsSerializer(orders, many = True)

        return Response(serializer.data, status.HTTP_200_OK)