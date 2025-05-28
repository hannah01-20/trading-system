from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Order
from ..serializers import OrderSerializer

class OrderView(APIView):
    def get(self, request):
        user_id = request.user.id

        orders = Order.objects.filter(user_id = user_id)
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)