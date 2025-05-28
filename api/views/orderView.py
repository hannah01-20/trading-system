from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Order
from ..serializers import OrderSerializer, OrderDetailsSerializer
from rest_framework import status
from rest_framework.serializers import ValidationError
from django.db import DatabaseError

class OrderView(APIView):
    def get(self, request):
        try:
            user = request.user

            orders = Order.objects.filter(user_id = user.id)
            serializer = OrderDetailsSerializer(orders, many=True)

            return Response(serializer.data)
        
        except DatabaseError as e:
            message = {"error": f"Database error occured. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data["user"] = user.id

            serializer = OrderSerializer(data = data)
            if serializer.is_valid():
                serializer.save()

                return Response("Successfully created", status.HTTP_201_CREATED)
            
            raise ValidationError(serializer.errors)
        
        except ValidationError as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderDetailsView(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(id = pk)
            serializer = OrderDetailsSerializer(order)

            return Response(serializer.data, status.HTTP_200_OK)
        
        except Order.DoesNotExist as e:
            message = {"error": f"Order doesn't exist. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk):
        try:
            data = request.data
            order= Order.objects.get(id = pk)
            serializer = OrderSerializer(order, data = data)

            if serializer.is_valid():
                serializer.save()

                return Response("Successfully updated.", status.HTTP_202_ACCEPTED)
            
            raise ValidationError(serializer.errors)
        
        except ValidationError as e:
            message = {"error": f"Invalid data. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except Order.DoesNotExist as e:
            message = {"error": f"Order doesn't exist. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk):
        try:
            stock = Order.objects.get(id = pk)
            stock.delete()

            return Response("Deleted stock", status.HTTP_200_OK)
        
        except Order.DoesNotExist as e:
            message = {"error": f"Data doesn't exist. {e}"}
            return Response(message, status.HTTP_400_BAD_REQUEST)
        
        except DatabaseError as e:
            message = {"error": f"Database error occurred. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            message = {"error": f"Something went wrong. {e}"}
            return Response(message, status.HTTP_500_INTERNAL_SERVER_ERROR) 